from src.Entities.Fator_b3 import Fator_b3
from src.Entities.Cotacao_b3_entity import Cotacao_b3_entity
from src.services.Base_service import Base_service


class Cotacao_b3_service(Base_service):
    def __init__(self) -> None:
        super().__init__(Cotacao_b3_entity)
    def getCorrigido(self,isin:str, codigo):
        correcoes: list[Fator_b3] = self.repo.get_correcoes(isin)
        cotacoes: list[Cotacao_b3_entity] = self.repo.get_hist(codigo)
        i = len(cotacoes) -1
        for correcao in correcoes:
            for indexCotacao in range(i,-1,-1):
                print(i)
                cotacao = cotacoes[indexCotacao]
                if (cotacao.data_pregao <= correcao.last_date_prior):
                    # i = indexCotacao
                    cotacoes[indexCotacao] =  Cotacao_b3_entity({
                        "id": cotacao.id,
                        "preco_abertura": cotacao.preco_abertura * correcao.rate,
                        "preco_maximo": cotacao.preco_maximo * correcao.rate,
                        "preco_minimo": cotacao.preco_minimo * correcao.rate,
                        "preco_medio": cotacao.preco_medio * correcao.rate,
                        "preco_fechamento": cotacao.preco_fechamento * correcao.rate,
                        "preco_melhor_compra": cotacao.preco_melhor_compra * correcao.rate,
                        "preco_melhor_venda": cotacao.preco_melhor_venda * correcao.rate,

                        "tipo_registro": cotacao.tipo_registro,
                        "data_pregao": cotacao.data_pregao,

                        "codigo_bdi": cotacao.codigo_bdi,
                        "codigo_negociacao": cotacao.codigo_negociacao,
                        "mercado": cotacao.mercado,
                        "nome_empresa": cotacao.nome_empresa,
                        "especificacao_papel": cotacao.especificacao_papel,
                        "prazo_termo": cotacao.prazo_termo,
                        "moeda": cotacao.moeda,


                        "numero_negocios": cotacao.numero_negocios,
                        "quantidade_negociada": cotacao.quantidade_negociada,
                        "volume_financeiro": cotacao.volume_financeiro,

                        "preco_exercicio": cotacao.preco_exercicio,
                        "indicador_correcao": cotacao.indicador_correcao,
                        "data_vencimento": cotacao.data_vencimento,
                        "fator_cotacao": cotacao.fator_cotacao,
                        "preco_exercicio_pontos": cotacao.preco_exercicio_pontos,

                        "isin": cotacao.isin,
                        "distribuicao": cotacao.distribuicao
                })
        
        return cotacoes


        
