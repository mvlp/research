from pathlib import Path
from requests import get
from os import listdir, remove, removedirs
from zipfile import ZipFile
import pandas as pd
from src.scripts.codigoPython.dataMiner.ReportProcessor_CGVN import ReportProcessor
from src.scripts.codigoPython.dataMiner.DataMiner import DataMiner
from sqlalchemy import create_engine, text
from src.scripts.codigoPython.dataMiner.url_db import url_db

BASE_DIR = Path(__file__).resolve().parent  # Isso dá "src/"
class DataMinerCGVN(DataMiner):
  def descompactar_e_unificar_zips(self,nomes_arquivos: list[str]) -> None:
    dataset = pd.DataFrame()
    
    for nome in nomes_arquivos:
      with ZipFile(f"{BASE_DIR}/data/zip/{self.dir}/{nome}", 'r') as zip_ref:
        zip_ref.extractall(f"{BASE_DIR}/data/{self.dir}/{nome}")
        ano = nome.split("_")[-1].split(".")[0]
        principal = f"cgvn_cia_aberta_{ano}.csv"
        praticas = f"cgvn_cia_aberta_praticas_{ano}.csv"
        with zip_ref.open(principal) as f1, zip_ref.open(praticas) as f2:
          first_dataset = pd.read_csv(f1, sep=';', encoding='latin1')
          second_dataset = pd.read_csv(f2, sep=';', encoding='latin1')
          print(f"{nome}: 1",first_dataset.columns)
          print(second_dataset.columns)
          second_dataset = second_dataset.merge(
              first_dataset[['ID_Documento', 'Data_Entrega']],
              on='ID_Documento',
              how='left'
          )
      dataset = pd.concat([dataset, second_dataset], ignore_index=True)
      remove(f"{BASE_DIR}/data/{self.dir}/{nome}/{principal}")
      remove(f"{BASE_DIR}/data/{self.dir}/{nome}/{praticas}")
      removedirs(f"{BASE_DIR}/data/{self.dir}/{nome}/")
    dataset.to_csv(f"{BASE_DIR}/docs/{self.dir}.csv",index=False, sep=';', encoding='latin1')

if __name__ == "__main__":
  url = "https://dados.cvm.gov.br/dados/CIA_ABERTA/DOC/CGVN/DADOS/"
  dir = "CGVN"
  miner = DataMinerCGVN(url,dir)
  nomes_arquivos: list[str] = miner.pegar_nomes_arquivos()
  print(nomes_arquivos)
  # miner.baixar_zips(nomes_arquivos)
  miner.descompactar_e_unificar_zips(nomes_arquivos)
  print()

  processor = ReportProcessor()
  engine = create_engine(url_db)
  processor.tratar_dados(f"{BASE_DIR}/docs/{dir}.csv",engine)
  # processor.gerar_relatorios(nomes_arquivos)
  # result = conn.execute(text("SELECT 1"))
  # print("Conexão bem-sucedida! Resultado:", result.scalar())
