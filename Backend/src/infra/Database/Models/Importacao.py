from src.infra.Database.extensions import db

class Importacao(db.Model):
    __tablename__ = "Importacao"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    data_importacao = db.Column(db.Date, nullable=False)
    nome_arquivo = db.Column(db.String(50), nullable=False)
    tabela = db.Column(db.String(50), nullable=False)
