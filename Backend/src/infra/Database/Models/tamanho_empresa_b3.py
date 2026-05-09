from src.infra.Database.extensions import db
from sqlalchemy import DateTime
class Tamanho_empresa_b3(db.Model):
    __tablename__ = "tamanho_empresa_b3"
    id = db.Column(db.Integer, primary_key=True)

    codigo_negociacao = db.Column(db.String(15))
    isin = db.Column(db.String(15))
    cnpj = db.Column(db.String(15))
    trimestre = db.Column(DateTime(timezone=True))
    preco_fechamento = db.Column(db.Numeric(50, 25))
    qtd_acoes = db.Column(db.BigInteger)
    porte = db.Column(db.String(15))