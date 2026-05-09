from src.infra.Database.extensions import db

class Empresa_b3(db.Model):
    __tablename__ = "empresa_b3"
    id = db.Column(db.Integer, primary_key=True)

    codigo_negociacao = db.Column(db.String(15))
    isin = db.Column(db.String(15))
    cnpj = db.Column(db.String(15))
