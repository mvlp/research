from pathlib import Path
from requests import get
from os import listdir, remove, removedirs
from zipfile import ZipFile
import pandas as pd
from .ReportProcessor import ReportProcessor

from sqlalchemy import create_engine, text

BASE_DIR = Path(__file__).resolve().parent  # Isso dá "src/"
class DataMiner:
  url = "https://dados.cvm.gov.br/dados/CIA_ABERTA/DOC/CGVN/DADOS/"

  
  def pegar_nomes_arquivos(self)-> list[str]:
    html = get(self.url).text # Pega o HTML da página
    index_inicial = html.find("<pre>")
    index_final = html.find("</pre>") #seleciona onde tem os links
    hyperlinks = html[index_inicial:index_final].split("\n")
    hyperlinks.pop(0)
    hyperlinks.pop(-1)
    for i in range(len(hyperlinks)): #extrai os links
      start_link = hyperlinks[i].find('href="') + len('href="')
      end_link = hyperlinks[i].find('">', start_link)
      hyperlinks[i] = hyperlinks[i][start_link:end_link]
    return hyperlinks

  def baixar_zips(self, nomes_arquivos: list[str]) -> None:
    for nome in nomes_arquivos:
      zip = get(self.url + nome).content
      with open(f"{BASE_DIR}/data/zip/{nome}", "wb") as arquivo:
        arquivo.write(zip)

  def descompactar_e_unificar_zips(self,nomes_arquivos: list[str]) -> None:
    dataset = pd.DataFrame()
    
    for nome in nomes_arquivos:
      with ZipFile(f"{BASE_DIR}/data/zip/{nome}", 'r') as zip_ref:
        zip_ref.extractall(f"{BASE_DIR}/data/{nome}")
        csvs = listdir(f"{BASE_DIR}/data/{nome}/")
        with zip_ref.open(csvs[0]) as f1, zip_ref.open(csvs[1]) as f2:
          first_dataset = pd.read_csv(f1, sep=';', encoding='latin1')
          second_dataset = pd.read_csv(f2, sep=';', encoding='latin1')
      second_dataset = second_dataset.merge(
          first_dataset[['ID_Documento', 'Data_Entrega']],
          on='ID_Documento',
          how='left'
      )
      dataset = pd.concat([dataset, second_dataset], ignore_index=True)
      remove(f"{BASE_DIR}/data/{nome}/{csvs[0]}")
      remove(f"{BASE_DIR}/data/{nome}/{csvs[1]}")
      removedirs(f"{BASE_DIR}/data/{nome}/")
      dataset.to_csv(f"{BASE_DIR}/docs/dataset_CGVN.csv",index=False, sep=';', encoding='latin1')

if __name__ == "__main__":
  
  miner = DataMiner()
  nomes_arquivos: list[str] = miner.pegar_nomes_arquivos()
  miner.baixar_zips(nomes_arquivos)
  miner.descompactar_e_unificar_zips(nomes_arquivos)

  processor = ReportProcessor()
  engine = create_engine("postgresql://guilhermedesouzafornaciari:Ga05112002@localhost:5432/research")
  processor.tratar_dados(f"{BASE_DIR}/docs/dataset_CGVN.csv",engine)
  # processor.gerar_relatorios(nomes_arquivos)
  # result = conn.execute(text("SELECT 1"))
  # print("Conexão bem-sucedida! Resultado:", result.scalar())
