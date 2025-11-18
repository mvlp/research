# from pathlib import Path
# import pandas as pd
# from pandas.core.groupby.generic import DataFrameGroupBy
# from Entities.Grafico import Grafico

# BASE_DIR = Path(__file__).resolve().parent
# print(BASE_DIR)

# class ReportProcessor:
#   nomes_capitulos = 'AC','CA','DR','OFC','ECI'
#   def calcular_dados(self, chapter_number: int, dataset: pd.DataFrame)-> pd.DataFrame:
#     chapter_dataset = dataset.loc[dataset['ID_Item'].str.startswith(f"{chapter_number}.", na=False)].copy()
#     print(len(chapter_dataset))
#     chapter_dataset["Data_Entrega"] = pd.to_datetime(chapter_dataset["Data_Entrega"])
#     chapter_dataset = chapter_dataset.groupby(["CNPJ_Companhia", "Data_Entrega", "ID_Documento", "Pratica_Adotada"]).size().reset_index(name='cnt')
#     chapter_dataset['freq'] = chapter_dataset.groupby(["CNPJ_Companhia", "Data_Entrega", "ID_Documento"])['cnt'].transform(
#         lambda x: x / x.sum()
#     )
    
#     chapter_dataset["Trimestre"] = chapter_dataset["Data_Entrega"].dt.to_period("Q")
#     summary_dataset = chapter_dataset.groupby(["Trimestre", "Pratica_Adotada"]).agg(
#         cnt=("cnt", "sum"),
#         freq=("freq", "sum")
#     ).reset_index()
      
#     summary_dataset.to_csv(f"{BASE_DIR}/docs/chapter_{chapter_number}_data.csv", index=False, sep=';', encoding='latin1')
    
#     return summary_dataset
  
#   def tratar_dados(self, csv_url: str):
#     dataset = pd.read_csv(csv_url, sep=';', encoding='latin1')
#     # Escala artigo => Enanpad 2024
#     ordem_levels = ["Não se Aplica", "Não", "Parcialmente", "Sim"]
#     dataset["gc_factor"] = pd.Categorical(
#         dataset["Pratica_Adotada"],
#         categories=ordem_levels,
#         ordered=True
#     )
#     dataset["gc_value"] = dataset["gc_factor"].cat.codes
#     dataset.loc[dataset["gc_value"] == -1, "gc_value"] = pd.NA
#     error_df = dataset.loc[
#         dataset["gc_value"].isna(),
#         ["CNPJ_Companhia", "Data_Entrega", "Data_Referencia", "Versao", "Nome_Empresarial"]
#     ]
#     # Remover duplicados
#     error_df = error_df.drop_duplicates()

#     # Ordenar por nome
#     error_df = error_df.sort_values(by="Nome_Empresarial")
#     error_df.to_json(f"{BASE_DIR}/assets/data/error_log.json", orient="records", force_ascii=False, indent=4)
#     dataset.to_csv(f"{BASE_DIR}/docs/dataset_CGVN.csv", index=False, sep=';', encoding='latin1')

#   # def gerar_grafico_percentual(self, chapter: str, group: pd.DataFrame) -> Grafico:
#   #   data = group["freq"]
#   #   medias = data
#   #   print(medias)

#   #   desvio_padrao = data.std().tolist()
#   #   datas = group["Trimestre"].unique().tolist()
#   #   return Grafico(
#   #     chapter,
#   #     labels=[str(data) for data in datas],
#   #     dado=medias,
#   #     limite_superior=[medias[i] + desvio_padrao[i] for i in range(len(medias))],
#   #     limite_inferior=[medias[i] - desvio_padrao[i] for i in range(len(medias))],
#   #   )

#   # def gerar_grafico_quantidade(self, chapter: str, group: pd.DataFrame) -> Grafico:
#   #   data = group["cnt"]
#   #   dado = data.sum().tolist()
#   #   datas = group["Trimestre"].unique().tolist()
#   #   return Grafico(
#   #     chapter,
#   #     labels=[str(data) for data in datas],
#   #     dado= dado,
#   #     limite_inferior = None,
#   #      limite_superior = None
#   #   )

#   def gerar_relatorios(self, nomes_arquivos: list[str]) -> None:
#     dataset = pd.read_csv(f"{BASE_DIR}/docs/dataset_CGVN.csv", sep=';', encoding='latin1')
#     for i in range(1,len(self.nomes_capitulos) + 1):
#       chapter_dataset = self.calcular_dados(i, dataset)
#       # grafico_percentual: Grafico = self.gerar_grafico_percentual(self.nomes_capitulos[i-1], chapter_dataset)
#       # grafico_quantidade: Grafico = self.gerar_grafico_quantidade(self.nomes_capitulos[i-1], chapter_dataset)