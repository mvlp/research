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
    from src.infra.Database.Models.cotacao_b3_relativa import CotacaoB3Corrigida


class Gera_indices:
    def __init__(self,engine: Engine) -> None:
        self.engine = engine
    def preco_para_porcentagem(self):
        service = Cotacao_b3_service()
        with Session(self.engine) as session:
            session.query(CotacaoB3Corrigida).delete()
            session.commit()
            empresas = session.execute(text("select distinct(codigo_negociacao)  from cotacao_b3 where data_pregao > '2000-01-01' and codigo_bdi = '2';")).mappings().all()
            # empresas = ['BGIP4']
            total = len(empresas)
            count_empresa = 1
            for empresa in empresas:
                codigo = empresa.codigo_negociacao
                print(f"{codigo}: {count_empresa}/{total} ")
                count_empresa+= 1
                dado = session.execute(text("select isin from cotacao_b3 where data_pregao > '2000-01-01' and codigo_negociacao = :code order by data_pregao desc limit 1;"),{"code":codigo}).mappings().all()
                dados_b3 = service.getCorrigido(dado[0].isin,codigo,"2026-01-01")
                for i in range(1,len(dados_b3)):
                    dado = dados_b3[i]
                    anterior = dados_b3[i-1]
                    corrigido = CotacaoB3Corrigida()
                    corrigido.tipo_registro = dado.tipo_registro 
                    corrigido.data_pregao = dado.data_pregao
                    corrigido.codigo_bdi = dado.codigo_bdi 
                    corrigido.codigo_negociacao = dado.codigo_negociacao 
                    corrigido.mercado = dado.mercado 
                    corrigido.nome_empresa = dado.nome_empresa 
                    corrigido.especificacao_papel = dado.especificacao_papel 
                    corrigido.prazo_termo = dado.prazo_termo
                    corrigido.moeda = dado.moeda
                    
                    if (dado.preco_abertura and anterior.preco_abertura): corrigido.preco_abertura = dado.preco_abertura
                    if (dado.preco_maximo and anterior.preco_maximo): corrigido.preco_maximo = dado.preco_maximo
                    if (dado.preco_minimo and anterior.preco_minimo): corrigido.preco_minimo = dado.preco_minimo
                    if (dado.preco_medio and anterior.preco_medio): corrigido.preco_medio = dado.preco_medio
                    if (dado.preco_fechamento and anterior.preco_fechamento): corrigido.preco_fechamento = dado.preco_fechamento

                    if (dado.preco_abertura and anterior.preco_abertura): corrigido.preco_abertura_relativo = (dado.preco_abertura - anterior.preco_abertura) / anterior.preco_abertura
                    if (dado.preco_maximo and anterior.preco_maximo): corrigido.preco_maximo_relativo = (dado.preco_maximo - anterior.preco_maximo) / anterior.preco_maximo
                    if (dado.preco_minimo and anterior.preco_minimo): corrigido.preco_minimo_relativo = (dado.preco_minimo - anterior.preco_minimo) / anterior.preco_minimo
                    if (dado.preco_medio and anterior.preco_medio): corrigido.preco_medio_relativo = (dado.preco_medio - anterior.preco_medio) / anterior.preco_medio
                    if (dado.preco_fechamento and anterior.preco_fechamento): corrigido.preco_fechamento_relativo = (dado.preco_fechamento - anterior.preco_fechamento) / anterior.preco_fechamento
                    
                    corrigido.numero_negocios = dado.numero_negocios 
                    corrigido.quantidade_negociada = dado.quantidade_negociada 
                    corrigido.volume_financeiro = dado.volume_financeiro 
                    corrigido.preco_exercicio = dado.preco_exercicio 
                    corrigido.indicador_correcao = dado.indicador_correcao
                    corrigido.data_vencimento = dado.data_vencimento 
                    corrigido.fator_cotacao = dado.fator_cotacao
                    corrigido.preco_exercicio_pontos = dado.preco_exercicio_pontos 
                    corrigido.isin = dado.isin 
                    corrigido.distribuicao = dado.distribuicao
                    session.add(corrigido)
                session.commit()

    def RendaMedia(self):

        pass
        
                
if __name__ == "__main__":
    engine = create_engine(url_db)
    gerador = Gera_indices(engine)
    gerador.preco_para_porcentagem()
    gerador.RendaMedia()

  