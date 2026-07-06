from src.Entities.Fator_b3 import Fator_b3
from src.Entities.Cotacao_b3_entity import Cotacao_b3_entity
from src.services.Base_service import Base_service


class Cotacao_b3_service(Base_service):
    def __init__(self) -> None:
        super().__init__(Cotacao_b3_entity)
        
    def getCorrigido(self, isin: str, codigo: str, data_fim: str):
        correcoes: list[Fator_b3] = self.repo.get_correcoes(isin, data_fim)
        subscricoes: list = self.repo.get_subscricoes(isin, data_fim)  # NOVO: busca só percentage e priceUnit
        cotacoes: list[Cotacao_b3_entity] = self.repo.get_hist(codigo, data_fim)

        # Primeiro aplica todas as correções que já existem (dividendos, splits)
        # — mesma lógica de antes, sem subscrições no SQL
        i = len(cotacoes) - 1
        for correcao in correcoes:
            for indexCotacao in range(i, -1, -1):
                cotacao = cotacoes[indexCotacao]
                if cotacao.data_pregao <= correcao.last_date_prior:
                    cotacoes[indexCotacao] = Cotacao_b3_entity({
                        **cotacao.__dict__,
                        "preco_abertura":    cotacao.preco_abertura    * correcao.rate,
                        "preco_maximo":      cotacao.preco_maximo      * correcao.rate,
                        "preco_minimo":      cotacao.preco_minimo      * correcao.rate,
                        "preco_medio":       cotacao.preco_medio       * correcao.rate,
                        "preco_fechamento":  cotacao.preco_fechamento  * correcao.rate,
                    })

        # Depois aplica subscrições usando o preço JÁ CORRIGIDO do dia
        for sub in subscricoes:
            # Acha o preço corrigido na data da subscrição
            preco_corrigido = next(
                (c.preco_fechamento for c in cotacoes if c.data_pregao == sub.lastDatePrior),
                None
            )
            if preco_corrigido is None or preco_corrigido <= 0:
                continue

            rate = (
                (preco_corrigido + (sub.percentage / 100) * sub.priceUnit)
                / ((1 + sub.percentage / 100) * preco_corrigido)
            )

            # Aplica retroativamente em todos os preços anteriores à data
            for indexCotacao in range(len(cotacoes) - 1, -1, -1):
                cotacao = cotacoes[indexCotacao]
                if cotacao.data_pregao <= sub.lastDatePrior:
                    cotacoes[indexCotacao] = Cotacao_b3_entity({
                        **cotacao.__dict__,
                        "preco_abertura":   cotacao.preco_abertura   * rate,
                        "preco_maximo":     cotacao.preco_maximo     * rate,
                        "preco_minimo":     cotacao.preco_minimo     * rate,
                        "preco_medio":      cotacao.preco_medio      * rate,
                        "preco_fechamento": cotacao.preco_fechamento * rate,
                    })

        return cotacoes


        
