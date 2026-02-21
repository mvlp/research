from datetime import date
from decimal import Decimal
from os import listdir
from pathlib import Path
from requests import get
from sqlalchemy import Engine, create_engine, select, text
from sqlalchemy.orm import Session

from src.scripts.codigoPython.DataMiner_utils import DataMinerUtil, Empresa, Codigo_negociacao
from src.infra.Database.Models.approved_cash_dividends_b3 import Approved_cash_dividends_b3
from src.infra.Database.Models.stock_dividends_b3 import Stock_dividends_b3
from src.infra.Database.Models.Importacao import Importacao
from src.infra.Database.Models.cotacao_b3 import CotacaoB3
from src.scripts.codigoPython.url_db import url_db

BASE_DIR = Path(__file__).resolve().parent  # Isso dá "CodigoPython/"



class Dataminer_B3:
    engine: Engine
    dir: str
    def __init__(self,engine: Engine) -> None:
        self.engine = engine
        self.dir = f"{str(BASE_DIR)}/B3_data/"
    
    def importar_dados(self):
        self.importar_eventos_empresariais()
        # self.importar_cotacoes_historicas()



    def importar_cotacoes_historicas(self):
        print("IMPORTANDO TODOS OS DADOS DA B3 NA PASTA")
        print("onde encontrar: https://www.b3.com.br/pt_br/market-data-e-indices/servicos-de-dados/market-data/historico/mercado-a-vista/series-historicas/")
        print()
        arquivos = listdir(self.dir)
        importados = self.pegar_dados_importados()
        nomes_importados = [res.nome_arquivo for res in importados]
        
        arquivo_para_importar: list[str] = []
        for arquivo in arquivos:
            if not arquivo in nomes_importados: ## significa que ele não foi importado ainda
                print("Não importado: ",arquivo)
                arquivo_para_importar.append(arquivo)
                continue
        print(arquivo_para_importar)

        for arquivo in arquivo_para_importar:
            print(f'IMPORTANDO {arquivo}')
            self.ler_arquivo(arquivo)
            print(f'{arquivo} IMPORTADO')

    def importar_eventos_empresariais(self):
        empresas = DataMinerUtil.get_empresas_http()
        erros = []
        for empresa in empresas:
            req = DataMinerUtil.get_proventos_aprovados_http(empresa)
            if req == None: 
                erros.append(empresa.issuingCompany)
                continue
            if len(req) == 0: continue
            req = req[0]

            dividendos = req["stockDividends"]
            empresaNome = req["tradingName"].replace(" ","")
            proventos_dinheiros = self.import_proventos_dinheiro(empresa,empresaNome)
            proventos_dinheiros.extend(req["cashDividends"])
            print(empresa.issuingCompany,dividendos,proventos_dinheiros)
            with Session(self.engine) as session:
                for dividendo in dividendos:
                    event = Stock_dividends_b3()
                    event.assetIssued = dividendo["assetIssued"]
                    event.cnpj = empresa.cnpj
                    event.factor = Decimal(dividendo["factor"].replace('.', '').replace(',', '.'))
                    event.approvedOn = dividendo["approvedOn"]
                    event.isinCode = dividendo["isinCode"]
                    event.label = dividendo["label"]
                    event.lastDatePrior = dividendo["lastDatePrior"]
                    event.remarks = dividendo["remarks"]
                    session.add(event)
                for dinheiros_aprovado in proventos_dinheiros:
                    event = Approved_cash_dividends_b3()
                    event.assetIssued = dinheiros_aprovado["assetIssued"]
                    event.paymentDate = dinheiros_aprovado["paymentDate"]
                    event.rate = Decimal(dinheiros_aprovado["rate"].replace('.', '').replace(',', '.'))
                    event.relatedTo = dinheiros_aprovado["relatedTo"]
                    event.isinCode = dinheiros_aprovado["isinCode"]
                    event.approvedOn = dinheiros_aprovado["approvedOn"]
                    event.label = dinheiros_aprovado["label"]
                    event.lastDatePrior = dinheiros_aprovado["lastDatePrior"]
                    event.remarks = dinheiros_aprovado["remarks"]
                    session.add(event)
                session.commit()

                session.execute(text("""
                    DELETE FROM approved_cash_dividends_b3 a
                    USING approved_cash_dividends_b3 b
                    WHERE a.ctid > b.ctid
                    AND a."isinCode"      = b."isinCode"
                    AND a."lastDatePrior" = b."lastDatePrior"
                    AND a.rate            = b.rate;
                """))
                session.commit()


        print(erros)


    def import_proventos_dinheiro(self,empresa:Empresa,empresaNome:str):
        codes = DataMinerUtil.get_codes_http(empresa)

        if (len(codes) == 0): return []
        req = DataMinerUtil.get_proventos_dinheiro_http(empresaNome,1)
        if (not req): return []
        paginas_totais = req["page"]["totalPages"]
        results = []
        for i in range(1,paginas_totais + 1):
            req = DataMinerUtil.get_proventos_dinheiro_http(empresaNome,i) 
            for provento in req["results"]:
                for code in codes:
                    if code.is_equal(provento["typeStock"]):
                        results.append({
                            "assetIssued": code.code,
                            "isinCode": code.isin,
                            "rate": provento["valueCash"],
                            "approvedOn": provento["dateApproval"],
                            "lastDatePrior": provento["lastDatePriorEx"],
                            "label": provento["corporateAction"],
                            "paymentDate": None,
                            "relatedTo": None,
                            "remarks": ""

                        })
        return results


    


    

    def ler_arquivo(self,nome_arquivo:str):
        with Session(self.engine) as session:
            with open(self.dir + nome_arquivo, "r",encoding="latin1") as f:
                for linha in f:
                    if linha.startswith("01"):  # ignora header/trailer
                        cotacao = self.processar_linha(linha)
                        session.add(cotacao)
            importacao = Importacao()
            importacao.data_importacao = date.today() 
            importacao.nome_arquivo = nome_arquivo
            importacao.tabela = "cotacao_b3"
            session.add(importacao)
            session.commit()


    def processar_linha(self,linha: str):
        def preco(pos_ini, pos_fim):
            return int(linha[pos_ini:pos_fim]) / 100
        linha = linha.replace('\x00',' ')
        cotacao = CotacaoB3()
        cotacao.tipo_registro=int(linha[0:2]),
        cotacao.data_pregao=date(
            int(linha[2:6]),
            int(linha[6:8]),
            int(linha[8:10])
        ),

        cotacao.codigo_bdi=int(linha[10:12])
        cotacao.codigo_negociacao=linha[12:24].strip()
        cotacao.mercado = linha[24:27]
        cotacao.nome_empresa=linha[27:39].strip()
        cotacao.especificacao_papel=linha[39:49].strip()
        cotacao.prazo_termo=linha[49:52].strip()
        cotacao.moeda=linha[52:56].strip()
        cotacao.preco_abertura=preco(56, 69)
        cotacao.preco_maximo=preco(69, 82)
        cotacao.preco_minimo=preco(82, 95)
        cotacao.preco_medio=preco(95, 108)
        cotacao.preco_fechamento=preco(108, 121)
        cotacao.preco_melhor_compra=preco(121, 134)
        cotacao.preco_melhor_venda=preco(134, 147)
        cotacao.numero_negocios=int(linha[147:152])
        cotacao.quantidade_negociada=int(linha[152:170])
        cotacao.volume_financeiro=int(linha[170:188]) / 100,
        cotacao.preco_exercicio = Decimal(linha[188:201]) / Decimal("100")
        cotacao.indicador_correcao = linha[201:202]
        datven = linha[202:210]
        cotacao.data_vencimento = None if datven == "00000000" else date(int(datven[0:4]), int(datven[4:6]), int(datven[6:8]))
        cotacao.fator_cotacao = int(linha[210:217])
        cotacao.preco_exercicio_pontos = Decimal(linha[217:230]) / Decimal("1000000")
        isin = linha[230:242].strip()
        cotacao.isin = None if isin == "000000000000" else isin
        cotacao.distribuicao = int(linha[242:245])
        return cotacao
    

    def pegar_dados_importados(self) -> list[Importacao]:
        with Session(self.engine) as session:
            query = select(Importacao).where(Importacao.tabela == "cotacao_b3").order_by(Importacao.data_importacao.desc())
            resultados = session.execute(query).scalars().all()
            return list(resultados)


if __name__ == "__main__":
  engine = create_engine(url_db)
  b3 = Dataminer_B3(engine)
  b3.importar_dados()
  