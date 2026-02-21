from src.infra.Database.Models.cotacao_b3 import CotacaoB3
from src.Entities.Base_entity import Base_entity
from datetime import date
from typing import Any
from decimal import Decimal

class Cotacao_b3_entity(Base_entity):

    id: int

    tipo_registro: str
    data_pregao: date

    codigo_bdi: str | None
    codigo_negociacao: str | None
    mercado: str | None
    nome_empresa: str | None
    especificacao_papel: str | None
    prazo_termo: str | None
    moeda: str | None

    preco_abertura: Decimal
    preco_maximo: Decimal
    preco_minimo: Decimal
    preco_medio: Decimal
    preco_fechamento: Decimal
    preco_melhor_compra: Decimal
    preco_melhor_venda: Decimal

    numero_negocios: int | None
    quantidade_negociada: int | None
    volume_financeiro: Decimal | None

    preco_exercicio: Decimal | None
    indicador_correcao: str | None
    data_vencimento: date | None
    fator_cotacao: str | None
    preco_exercicio_pontos: Decimal | None

    isin: str | None
    distribuicao: str | None

    def to_model(self) -> Any:
        obj = CotacaoB3()

        obj.id = self.id
        obj.tipo_registro = self.tipo_registro
        obj.data_pregao = self.data_pregao

        obj.codigo_bdi = self.codigo_bdi
        obj.codigo_negociacao = self.codigo_negociacao
        obj.mercado = self.mercado
        obj.nome_empresa = self.nome_empresa
        obj.especificacao_papel = self.especificacao_papel
        obj.prazo_termo = self.prazo_termo
        obj.moeda = self.moeda

        obj.preco_abertura = self.preco_abertura
        obj.preco_maximo = self.preco_maximo
        obj.preco_minimo = self.preco_minimo
        obj.preco_medio = self.preco_medio
        obj.preco_fechamento = self.preco_fechamento
        obj.preco_melhor_compra = self.preco_melhor_compra
        obj.preco_melhor_venda = self.preco_melhor_venda

        obj.numero_negocios = self.numero_negocios
        obj.quantidade_negociada = self.quantidade_negociada
        obj.volume_financeiro = self.volume_financeiro

        obj.preco_exercicio = self.preco_exercicio
        obj.indicador_correcao = self.indicador_correcao
        obj.data_vencimento = self.data_vencimento
        obj.fator_cotacao = self.fator_cotacao
        obj.preco_exercicio_pontos = self.preco_exercicio_pontos

        obj.isin = self.isin
        obj.distribuicao = self.distribuicao

        return obj

    def to_dict(self) -> dict[str, Any]:
        return {
            # "id": self.id,
            # "tipo_registro": self.tipo_registro,
            "data_pregao": self.data_pregao,

            # "codigo_bdi": self.codigo_bdi,
            # "codigo_negociacao": self.codigo_negociacao,
            # "mercado": self.mercado,
            # "nome_empresa": self.nome_empresa,
            # "especificacao_papel": self.especificacao_papel,
            # "prazo_termo": self.prazo_termo,
            # "moeda": self.moeda,

            # "preco_abertura": self.preco_abertura,
            # "preco_maximo": self.preco_maximo,
            # "preco_minimo": self.preco_minimo,
            # "preco_medio": self.preco_medio,
            "preco_fechamento": self.preco_fechamento,
            # "preco_melhor_compra": self.preco_melhor_compra,
            # "preco_melhor_venda": self.preco_melhor_venda,

            # "numero_negocios": self.numero_negocios,
            # "quantidade_negociada": self.quantidade_negociada,
            # "volume_financeiro": self.volume_financeiro,

            # "preco_exercicio": self.preco_exercicio,
            # "indicador_correcao": self.indicador_correcao,
            # "data_vencimento": self.data_vencimento,
            # "fator_cotacao": self.fator_cotacao,
            # "preco_exercicio_pontos": self.preco_exercicio_pontos,

            # "isin": self.isin,
            # "distribuicao": self.distribuicao,
        }






