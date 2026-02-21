from dataclasses import dataclass
from datetime import date
from src.infra.Database.extensions import db

class CotacaoB3(db.Model):
    __tablename__ = "cotacao_b3"

    id = db.Column(db.Integer, primary_key=True)

    tipo_registro = db.Column(db.String(2), nullable=False)
    data_pregao = db.Column(db.Date, nullable=False)

    codigo_bdi = db.Column(db.String(2))
    codigo_negociacao = db.Column(db.String(12))
    mercado = db.Column(db.String(3))
    nome_empresa = db.Column(db.String(15))
    especificacao_papel = db.Column(db.String(10))
    prazo_termo = db.Column(db.String(3))
    moeda = db.Column(db.String(4))

    preco_abertura = db.Column(db.Numeric(24, 10))
    preco_maximo = db.Column(db.Numeric(24, 10))
    preco_minimo = db.Column(db.Numeric(24, 10))
    preco_medio = db.Column(db.Numeric(24, 10))
    preco_fechamento = db.Column(db.Numeric(24, 10))
    preco_melhor_compra = db.Column(db.Numeric(24, 10))
    preco_melhor_venda = db.Column(db.Numeric(24, 10))

    numero_negocios = db.Column(db.BigInteger)
    quantidade_negociada = db.Column(db.BigInteger)
    volume_financeiro = db.Column(db.Numeric(18, 4))


    preco_exercicio = db.Column(db.Numeric(24, 10))
    indicador_correcao = db.Column(db.String(1))
    data_vencimento = db.Column(db.Date)
    fator_cotacao = db.Column(db.String(7))
    preco_exercicio_pontos = db.Column(db.Numeric(24, 10))

    isin = db.Column(db.String(12))
    distribuicao = db.Column(db.String(10))
