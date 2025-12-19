from os import listdir, remove, removedirs
import os
from pathlib import Path
from zipfile import ZipFile

import pandas as pd
from requests import get


BASE_DIR = Path(__file__).resolve().parent  # Isso dá "src/"
class DataMiner:
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
    for nome in nomes_arquivos:
      zip = get(url + nome).content
      with open(dir + nome, "wb") as arquivo:
        arquivo.write(zip)

