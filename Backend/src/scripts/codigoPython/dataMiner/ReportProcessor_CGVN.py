from pathlib import Path
import pandas as pd
from pandas.core.groupby.generic import DataFrameGroupBy
from src.infra.Database.Models.Governanca import Governanca
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
    dataset.to_sql("governanca", engine, if_exists="replace", index=False)

  def gerar_grafico_percentual(self, chapter: str, chapter_dataset: pd.DataFrame) -> Grafico_entity:
    dataset = chapter_dataset.copy() ## Necessário para não alterar o dataframe original
    dataset["Data_Entrega"] = pd.to_datetime(dataset["Data_Entrega"])
    dataset["Data_Entrega"] = dataset["Data_Entrega"].dt.to_period("Q") 
    dataset = dataset.groupby(["CNPJ_Companhia", "Data_Entrega", "ID_Documento", "Pratica_Adotada"]).size().reset_index(name='cnt')
    total = dataset.groupby(["Data_Entrega", "ID_Documento"])['cnt'].transform('sum')
    dataset['freq'] = dataset['cnt'] / total
    summary = dataset.groupby(["Data_Entrega", "Pratica_Adotada"])
    medias = summary["freq"].mean().transform(lambda x: x *100).to_list()
    inferior = summary["freq"].quantile(0.05).transform(lambda x: x *100).to_list()
    superior = summary["freq"].quantile(0.95).transform(lambda x: x *100).to_list()

    datas = summary["Data_Entrega"].unique().tolist()
    return Grafico_entity(
      chapter,
      labels=[str(data) for data in datas],
      dado=medias,
      limite_superior= superior, 
      limite_inferior= inferior,
    )

  def gerar_grafico_quantidade(self, chapter: str, chapter_dataset: pd.DataFrame) -> Grafico_entity:
    ## Não é absolutamente necessário a linha abaixo, mas previne alguns erros se o código for alterado (a data não pode ser alterada 2x, por isso que estou clonando os dados)
    dataset = chapter_dataset.copy() 
    dataset["Data_Entrega"] = pd.to_datetime(dataset["Data_Entrega"])
    dataset["Data_Entrega"] = dataset["Data_Entrega"].dt.to_period("M")
    dataset = dataset.groupby(["CNPJ_Companhia", "Data_Entrega", "ID_Documento", "Pratica_Adotada"]).size().reset_index(name='cnt')
    dados = dataset.groupby(["Data_Entrega", "Pratica_Adotada"])
    datas = dados["Data_Entrega"].unique().to_list()
    dados = dados.agg(n=("ID_Documento", "count"))
    dado = dados["n"].to_list()
    return Grafico_entity(
      chapter,
      labels=[str(data) for data in datas],
      dado= dado,
      limite_inferior = None,
       limite_superior = None
    )


  def gerar_relatorios(self, nomes_arquivos: list[str]) -> None:
    dataset = pd.read_csv(f"{BASE_DIR}/docs/dataset_CGVN.csv", sep=';', encoding='latin1')
    print(dataset.columns)
    dataset = dataset.dropna(subset=['gc_value'])
    # for i in range(1,len(self.nomes_capitulos) + 1):
    #   chapter_dataset = dataset.loc[dataset['ID_Item'].str.startswith(f"{1}.", na=False)]
    #   grafico_percentual: Grafico_entity = self.gerar_grafico_percentual(self.nomes_capitulos[1-1], chapter_dataset)
    #   grafico_quantidade: Grafico_entity = self.gerar_grafico_quantidade(self.nomes_capitulos[1-1], chapter_dataset)



