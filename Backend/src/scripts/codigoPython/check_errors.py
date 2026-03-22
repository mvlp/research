from decimal import Decimal
from pathlib import Path
import pandas as pd
from sqlalchemy import create_engine
from main import app
from sqlalchemy.orm import Session
from sqlalchemy import Engine, select, text
from src.scripts.codigoPython.url_db import url_db
BASE_DIR = Path(__file__).resolve().parent  # Isso dá "CodigoPython/"

with app.app_context():
    from src.services.Cotacao_b3_service import Cotacao_b3_service


class check_errors:
    def __init__(self,engine) -> None:
        self.engine = engine

    def importar(self):
        df = pd.read_excel(
            str(BASE_DIR) + '/01_cotacoes.xlsx',
            header=3,    
        )
        df = df.rename(columns={df.columns[0]: "data"})
                # limpa os headers: pega só a última linha
        df.columns = [
            col.split("\n")[-1].strip() if col != "data" else col
            for col in df.columns
        ]
        df_long = df.melt(
            id_vars="data",
            var_name="codigo_negociacao",
            value_name="valor"
        )
        df_long = df_long[
            (df_long["valor"].notna()) &
            (df_long["valor"] != "-")
        ]
        df_long["data"] = pd.to_datetime(df_long["data"], dayfirst=True)
        df_long["valor"] = df_long["valor"].astype(float)
        df_long.to_sql(
            "cotacao_economatica",
            engine,
            if_exists="replace",
            index=False
        )

    def comparar_empresas(self,code:str):
        print("Comparando resultados da empresa: ",code)
        with Session(self.engine) as session:
            dado = session.execute(text("select isin from cotacao_b3 where data_pregao > '2000-01-01' and codigo_negociacao = :code order by data_pregao desc limit 1;"),{"code":code}).mappings().all()
            dados_economatica = session.execute(text("select * from cotacao_economatica where data > '2000-01-01' and codigo_negociacao = :code order by data asc;"),{"code":code}).mappings().all()    
        dados_economatica = [dict(row) for row in dados_economatica]
        if not dado or not dados_economatica: return 0
        isin = dado[0]["isin"]
        service = Cotacao_b3_service()
        dados_b3 = service.getCorrigido(isin,code)

        econ_por_data = {}
        for row in dados_economatica:
            data = row["data"].date()
            econ_por_data[data] = Decimal(row["valor"])


        b3_por_data = {
            row.data_pregao: row.preco_fechamento
            for row in dados_b3
        }

        datas_comuns = {
            k: (econ_por_data[k], b3_por_data[k])
            for k in econ_por_data.keys() & b3_por_data.keys()
        }

        if not datas_comuns:
            return 0
        erros = []

        for data in sorted(datas_comuns):
            preco_econ = econ_por_data[data]
            preco_b3   = b3_por_data[data]
    
            diff_abs = abs(preco_b3 - preco_econ)
            if diff_abs > 0.01:
                print(f"{data}: {diff_abs} = |{preco_b3} - {preco_econ}")            
        

        if not erros:
            return 0
        else:
            maximo = max(erros)
            print(maximo)
            return maximo
            
    
    def get_piores_empresas(self):
        with Session(self.engine) as session:
            dados = session.execute(text("select distinct on (codigo_negociacao) * from cotacao_economatica where data > '2000-01-01';")).mappings().all()
        print(len(dados), " Empresas")
        arrumadas = ["AERI3"]
        bao = 0
        ruim = 0
        for codigo in dados:
            codigo = codigo["codigo_negociacao"]
            maximo = self.comparar_empresas(codigo)
            if maximo == 0:
                bao += 1
            else: 
                ruim += 1

        print(bao,ruim)




if __name__ == "__main__":
    engine = create_engine(url_db)
    checador = check_errors(engine)
    checador.comparar_empresas("BALM4")
    # importador.get_piores_empresas()

  