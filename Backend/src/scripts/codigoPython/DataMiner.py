from datetime import date, datetime
from datetime import date
from os import listdir, mkdir
import re
from shutil import copy
from zipfile import ZipFile
import pandas as pd
from sqlalchemy.orm import Session
from src.infra.Database.Models.Importacao import Importacao
from pathlib import Path
from zipfile import ZipFile

import pandas as pd
from requests import get
from sqlalchemy import Engine, delete, select, text

def log_bad_lines(bad_line):
    print("Linha descartada:", bad_line)
    return None


BASE_DIR = Path(__file__).resolve().parent  # Isso dá "CodigoPython/"
class DataMiner:
  def __init__(self,engine: Engine, dir: str) -> None:
    self.dir = dir
    self.engine = engine

  def tratar_nome(self, txt:str):
    nome = txt.split("_")
    nome.pop(-1)
    nome.pop(1)
    nome.pop(1)
    if len(nome) == 1:
        nome.append("principal")
    return "_".join(nome)   
  def importar_tabela(self):
    url = f"https://dados.cvm.gov.br/dados/CIA_ABERTA/DOC/{self.dir}/DADOS/"
    dados = self.pegar_dados_arquivos(url)
    importados = self.pegar_dados_importados()
    nomes_importados = [res.nome_arquivo for res in importados]
    
    zip_para_importar: list[str] = []
    zip_para_apagar: list[str] = []
    for arquivo in dados.keys():
      if not arquivo in nomes_importados: ## significa que ele não foi importado ainda
        print("Não importado: ",arquivo)
        zip_para_importar.append(arquivo)
        continue
      index = nomes_importados.index(arquivo)
      if importados[index].data_importacao < dados[arquivo]:
        print("atualizar importação: ",arquivo)
        zip_para_apagar.append(arquivo)
        zip_para_importar.append(arquivo)
    self.baixar_zips(url,self.dir, zip_para_importar)
    print(zip_para_importar)
    for zip in zip_para_apagar:
      self.apagar_zip(zip)
    for zip in zip_para_importar:
      self.importar_zip(zip)
    self.exec_final()

  def exec_final(self):
    pass



  def pegar_dados_importados(self) -> list[Importacao]:
    with Session(self.engine) as session:
      query = select(Importacao).where(Importacao.tabela == self.dir).order_by(Importacao.data_importacao.desc())
      resultados = session.execute(query).scalars().all()
      return list(resultados)

  def apagar_zip(self,zip:str):
    print("APAGANDO ZIP: ",zip)
    url_arquivo = f"{str(BASE_DIR)}/data/zip/{self.dir}/{zip}"
    with ZipFile(url_arquivo, 'r') as zip_ref:
      arquivos = zip_ref.namelist()
      for arquivo in arquivos:
        nome_database = self.tratar_nome(arquivo)
        print("APAGANDO ARQUIVO: ",arquivo)
        stmt = text(f"DELETE  FROM {nome_database} WHERE arquivo_origem = :zip")
        with Session(self.engine) as session:
            session.execute(
                stmt,
                {"zip": zip}
            )
            session.commit()
        


  def importar_zip(self, zip:str):
    print("IMPORTANDO ZIP: ",zip)
    url_arquivo = f"{str(BASE_DIR)}/data/zip/{self.dir}/{zip}"
    with ZipFile(url_arquivo, 'r') as zip_ref:
      arquivos = zip_ref.namelist()


      for arquivo in arquivos:
        print("IMPORTANDO ARQUIVO: ",arquivo)
        nome_database = self.tratar_nome(arquivo)
        with zip_ref.open(arquivo) as f1:
          df = pd.read_csv(f1, sep=';', encoding='latin1',engine="python",on_bad_lines=log_bad_lines)
          if nome_database.endswith("_con"):
            df["tipo_csv"] = "con"
            nome_database = nome_database[0:-len("_con")]
          elif nome_database.endswith("_ind"):
            df["tipo_csv"] = "ind"
            nome_database = nome_database[0:-len("_ind")]
          df["arquivo_origem"] = zip
          df.to_sql(nome_database,self.engine, if_exists="append",index=False)
    with Session(self.engine) as session:
      importacao = Importacao()
      importacao.data_importacao = date.today() 
      importacao.nome_arquivo = zip
      importacao.tabela = self.dir
      session.add(importacao)
      session.commit()
    print("CRIADO REGISTRO DE IMPORTAÇÃO NO BD: ",zip)
  

  @staticmethod
  def pegar_dados_arquivos(url:str)-> dict[str,date]:
    html = get(url).text # Pega o HTML da página
    index_inicial = html.find("<pre>")
    index_final = html.find("</pre>") #seleciona onde tem os links
    hyperlinks = html[index_inicial:index_final].split("\n")
    hyperlinks.pop(0)
    hyperlinks.pop(-1)
    resultados: dict[str,date] = {}
    for i in range(len(hyperlinks)): #extrai os links
      start_link = hyperlinks[i].find('href="') + len('href="')
      end_link = hyperlinks[i].find('">', start_link)
      match = re.search(r'\b\d{2}-[A-Za-z]{3}-\d{4}\b', hyperlinks[i])
      if not match:
        raise ValueError("O sistema não conseguiu extrair a data da string")
      data_arquivo = match.group()
      nome_arquivo = hyperlinks[i][start_link:end_link]
      data = datetime.strptime(data_arquivo, "%d-%b-%Y")
      resultados[nome_arquivo] = data.date()
    return resultados

  @staticmethod
  def pegar_nomes_arquivos(url:str)-> list[str]:
    html = get(url).text # Pega o HTML da página
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

  @staticmethod
  def baixar_zips(url:str,dir:str, nomes_arquivos: list[str]) -> None:
    diretorios = listdir(f"{str(BASE_DIR)}/data/zip/")
    if (not dir in diretorios):
      mkdir(f"{str(BASE_DIR)}/data/zip/{dir}")
    for nome in nomes_arquivos:
      if nome == "fre_cia_aberta_2024.zip":
        copy(f"{BASE_DIR}/data/ajustes/fre_cia_aberta_2024.zip",f"{str(BASE_DIR)}/data/zip/{dir}/{nome}")
        continue
      zip = get(url + nome).content
      with open(f"{str(BASE_DIR)}/data/zip/{dir}/{nome}", "wb") as arquivo:
        arquivo.write(zip)



