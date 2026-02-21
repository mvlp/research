from datetime import date
from pathlib import Path
from typing import Any
from requests import get
from os import listdir, remove, removedirs
from zipfile import ZipFile
import pandas as pd
from src.infra.Database.Models.Indice import Indice
from src.infra.Database.Models.Dimensao import Dimensao
from src.infra.Database.Models.pergunta import Pergunta
from src.infra.Database.Models.pergunta_dimensao import Pergunta_Dimensao

from src.infra.Database.Models.Importacao import Importacao
from src.scripts.codigoPython.DataMiner import DataMiner
from sqlalchemy.orm import Session
from sqlalchemy import Engine, create_engine, select, text
from src.scripts.codigoPython.url_db import url_db

BASE_DIR = Path(__file__).resolve().parent  # Isso dá "CodigoPython/"
class DataMinerCGVN(DataMiner):
  def __init__(self, engine: Engine) -> None:
    super().__init__(engine, "CGVN")
    self.dataset = pd.DataFrame()
  dataset: pd.DataFrame

  def importar_zip(self,zip: str) -> None:
    print("IMPORTANDO ZIP: ",zip)
    with ZipFile(f"{BASE_DIR}/data/zip/CGVN/{zip}", 'r') as zip_ref:
      zip_ref.extractall(f"{BASE_DIR}/data/CGVN/{zip}")
      ano = zip.split("_")[-1].split(".")[0]
      principal = f"cgvn_cia_aberta_{ano}.csv"
      praticas = f"cgvn_cia_aberta_praticas_{ano}.csv"
      with zip_ref.open(principal) as f1, zip_ref.open(praticas) as f2:
        first_dataset = pd.read_csv(f1, sep=';', encoding='latin1')
        second_dataset = pd.read_csv(f2, sep=';', encoding='latin1')
        second_dataset = second_dataset.merge(
            first_dataset[['ID_Documento', 'Data_Entrega']],
            on='ID_Documento',
            how='left'
        )
        second_dataset["arquivo_origem"] = zip
      self.dataset = pd.concat([self.dataset, second_dataset], ignore_index=True)
      remove(f"{BASE_DIR}/data/CGVN/{zip}/{principal}")
      remove(f"{BASE_DIR}/data/CGVN/{zip}/{praticas}")
      removedirs(f"{BASE_DIR}/data/CGVN/{zip}/")
    with Session(self.engine) as session:
      importacao = Importacao()
      importacao.data_importacao = date.today() 
      importacao.nome_arquivo = zip
      importacao.tabela = self.dir
      session.add(importacao)
      session.commit()

  def exec_final(self):
    if self.dataset.__len__() == 0: return

    # Escala artigo => Enanpad 2024
    ordem_levels = ["Não se Aplica", "Não", "Parcialmente", "Sim"]
    self.dataset["gc_factor"] = pd.Categorical(
        self.dataset["Pratica_Adotada"],
        categories=ordem_levels,
        ordered=True
    )
    self.dataset["Data_Entrega"] = pd.to_datetime(self.dataset['Data_Entrega'])
    self.dataset["gc_value"] = self.dataset["gc_factor"].cat.codes
    self.dataset.loc[self.dataset["gc_value"] == -1, "gc_value"] = pd.NA
    error_df = self.dataset.loc[
        self.dataset["gc_value"].isna(),
        ["CNPJ_Companhia", "Data_Entrega", "Data_Referencia", "Versao", "Nome_Empresarial"]
    ]
    # Remover duplicados
    error_df = error_df.drop_duplicates()

    # Ordenar por nome
    error_df = error_df.sort_values(by="Nome_Empresarial")
    error_df.to_sql("cgvn_dados_faltantes", self.engine, if_exists="replace", index=False)
    self.dataset = self.dataset.dropna(subset=["gc_value"])
    self.dataset.to_csv(f"{BASE_DIR}/docs/dataset_CGVN.csv",index=False, sep=';', encoding='latin1')
    self.dataset.to_sql("cgvn_praticas", self.engine, if_exists="replace", index=False)
    perguntas = (self.dataset[["ID_Item", "Pratica_Recomendada"]].drop_duplicates().to_dict(orient="records"))
    with Session(self.engine) as session:
      query = select(Importacao).where(Importacao.tabela == "perguntas").order_by(Importacao.data_importacao.desc())
      importacao = session.execute(query).scalars().first()
      if importacao != None: return
      for obj in perguntas:
        pergunta = Pergunta()
        pergunta.id = obj["ID_Item"]
        pergunta.texto = obj["Pratica_Recomendada"]
        session.add(pergunta)
      importacao = Importacao()
      importacao.data_importacao = date.today() 
      importacao.nome_arquivo = ''
      importacao.tabela = "perguntas"
      session.add(importacao)
      session.commit()

