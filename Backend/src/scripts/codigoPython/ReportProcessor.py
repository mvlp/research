from pathlib import Path
import pandas as pd
from pandas.core.groupby.generic import DataFrameGroupBy
from src.infra.Database.Models.Governanca import Governanca
from src.Entities.Grafico import Grafico
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

  def gerar_grafico_percentual(self, chapter: str, chapter_dataset: pd.DataFrame) -> Grafico:
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
    return Grafico(
      chapter,
      labels=[str(data) for data in datas],
      dado=medias,
      limite_superior= superior, 
      limite_inferior= inferior,
    )

  def gerar_grafico_quantidade(self, chapter: str, chapter_dataset: pd.DataFrame) -> Grafico:
    ## Não é absolutamente necessário a linha abaixo, mas previne alguns erros se o código for alterado (a data não pode ser alterada 2x, por isso que estou clonando os dados)
    dataset = chapter_dataset.copy() 
    dataset["Data_Entrega"] = pd.to_datetime(dataset["Data_Entrega"])
    dataset["Data_Entrega"] = dataset["Data_Entrega"].dt.to_period("M")
    dataset = dataset.groupby(["CNPJ_Companhia", "Data_Entrega", "ID_Documento", "Pratica_Adotada"]).size().reset_index(name='cnt')
    dados = dataset.groupby(["Data_Entrega", "Pratica_Adotada"])
    datas = dados["Data_Entrega"].unique().to_list()
    dados = dados.agg(n=("ID_Documento", "count"))
    dado = dados["n"].to_list()
    return Grafico(
      chapter,
      labels=[str(data) for data in datas],
      dado= dado,
      limite_inferior = None,
       limite_superior = None
    )


  def calcular_indices(self, dataset: pd.DataFrame, id_matriz: int) -> None:
    pesos = None
    if (id_matriz == None): # é teste
      pesos = pd.DataFrame([       ### OBTIDO a partir do BD
        [1,1,1,1,1,1,1,1,1,1,1,1],  # AC: 1.1.1 a 1.8.2
        [1,1,1,1,1,1,1,1,1,1,1,1],  # CA: 2.1.1 a 2.9.3
        [1,1,1,1,1,1,1,1],  # DR: 3.1.1 a 3.4.3
        [1,1,1,1,1,1,1,1,1,1], # OFC: 4.1.1 a 4.5.3
        [1,1,1,1,1,1,1,1,1,1,1,1], # ECI: 5.1.1 a 5.5.3
      ])
    else:
      # Buscar pesos no BD
      pass
    
    dataset["ID_Item"] = dataset["ID_Item"].str.extract(r"^(\d+)").astype(int) ## Pega só o número do capítulo
    dataset_matriz = (
        dataset.groupby(["CNPJ_Companhia", "ID_Item","Data_Referencia"])["gc_value"]
          .apply(list)  # transforma os valores em lista
          .reset_index()
    ) 
    dataset_matriz = dataset_matriz.sort_values(by=["Data_Referencia","CNPJ_Companhia","ID_Item"]) ## Ordena para garantir a consistência na multiplicação matricial
    print(dataset_matriz.head(5))
    print(dataset_matriz.head(5)["gc_value"].apply(len).to_list())

  def gerar_relatorios(self, nomes_arquivos: list[str]) -> None:
    dataset = pd.read_csv(f"{BASE_DIR}/docs/dataset_CGVN.csv", sep=';', encoding='latin1')
    print(dataset.columns)
    dataset = dataset.dropna(subset=['gc_value'])
    self.calcular_indices(dataset, 1)
    # for i in range(1,len(self.nomes_capitulos) + 1):
    #   chapter_dataset = dataset.loc[dataset['ID_Item'].str.startswith(f"{1}.", na=False)]
    #   grafico_percentual: Grafico = self.gerar_grafico_percentual(self.nomes_capitulos[1-1], chapter_dataset)
    #   grafico_quantidade: Grafico = self.gerar_grafico_quantidade(self.nomes_capitulos[1-1], chapter_dataset)





def operacao_matricial(matriz_a: pd.DataFrame, matriz_b: pd.DataFrame) -> pd.DataFrame:
  resultado = matriz_a.dot(matriz_b)
  return resultado