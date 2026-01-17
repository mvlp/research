from pathlib import Path
import pandas as pd
from pandas.core.groupby.generic import DataFrameGroupBy
from src.infra.Database.Models.ajustes_auto.cgvn_praticas import cgvn_praticas
from src.Entities.Grafico_entity import Grafico_entity
from sqlalchemy.engine.base import Engine
BASE_DIR = Path(__file__).resolve().parent

class ReportProcessor:
  nomes_capitulos = 'AC','CA','DR','OFC','ECI'
  
  def tratar_dados(self, csv_url: str, engine: Engine):
    dataset = pd.read_csv(csv_url,encoding='latin1', sep=";")
    # Escala artigo => Enanpad 2024
    ordem_levels = ["Não se Aplica", "Não", "Parcialmente", "Sim"]
    
    dataset["gc_factor"] = pd.Categorical(
        dataset["Pratica_Adotada"],
        categories=ordem_levels,
        ordered=True
    )
    dataset["Data_Entrega"] = pd.to_datetime(dataset['Data_Entrega'])
    dataset["gc_value"] = dataset["gc_factor"].cat.codes
    dataset.loc[dataset["gc_value"] == -1, "gc_value"] = pd.NA
    error_df = dataset.loc[
        dataset["gc_value"].isna(),
        ["CNPJ_Companhia", "Data_Entrega", "Data_Referencia", "Versao", "Nome_Empresarial"]
    ]
    # Remover duplicados
    error_df = error_df.drop_duplicates()

    # Ordenar por nome
    error_df = error_df.sort_values(by="Nome_Empresarial")
    error_df.to_json(f"{BASE_DIR}/assets/data/error_log.json", orient="records", force_ascii=False, indent=4)
    dataset.to_csv(f"{BASE_DIR}/docs/dataset_CGVN.csv",index=False, sep=';', encoding='latin1')
    dataset.to_sql("cgvn_praticas", engine, if_exists="replace", index=False)



  def gerar_relatorios(self, nomes_arquivos: list[str]) -> None:
    dataset = pd.read_csv(f"{BASE_DIR}/docs/dataset_CGVN.csv", sep=';', encoding='latin1')
    dataset = dataset.dropna(subset=['gc_value'])
    # for i in range(1,len(self.nomes_capitulos) + 1):
    #   chapter_dataset = dataset.loc[dataset['ID_Item'].str.startswith(f"{1}.", na=False)]
    #   grafico_percentual: Grafico_entity = self.gerar_grafico_percentual(self.nomes_capitulos[1-1], chapter_dataset)
    #   grafico_quantidade: Grafico_entity = self.gerar_grafico_quantidade(self.nomes_capitulos[1-1], chapter_dataset)



