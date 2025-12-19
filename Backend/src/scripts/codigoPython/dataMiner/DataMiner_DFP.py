from pathlib import Path
from requests import get
from os import listdir, remove, removedirs
from zipfile import ZipFile
import pandas as pd

from src.scripts.codigoPython.dataMiner.url_db import url_db
from .DataMiner import DataMiner
from sqlalchemy import create_engine, text

BASE_DIR = Path(__file__).resolve().parent  # Isso dá "src/"
class DataMinerDFP(DataMiner):
    def importar_dados(self,nomes_arquivos: list[str]):
       pass


if __name__ == "__main__":
  url = "https://dados.cvm.gov.br/dados/CIA_ABERTA/DOC/DFP/DADOS/"
  dir = "DFP"
  miner = DataMinerDFP(url,dir)
  engine = create_engine(url_db)
  nomes_arquivos: list[str] = miner.pegar_nomes_arquivos()
  miner.baixar_zips(nomes_arquivos)

      with ZipFile(f"{BASE_DIR}/data/zip/{self.dir}/{nome}", 'r') as zip_ref: