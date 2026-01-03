
from pathlib import Path
from src.scripts.codigoPython.dataMiner.url_db import url_db
from .DataMiner import DataMiner
from sqlalchemy import create_engine
BASE_DIR = Path(__file__).resolve().parent  # Isso dá "src/"


if __name__ == "__main__":
  engine = create_engine(url_db)
  bases = DataMiner.pegar_nomes_arquivos("https://dados.cvm.gov.br/dados/CIA_ABERTA/DOC/")
  bases = ["FRE","DFP","FCA","IPE","ITR","VLMO","CGVN"]
  for base in bases:
    miner = DataMiner(engine,base)
    miner.importar_tabela()

    
  