from  src.infra.Database.extensions import db


class Pergunta_Dimensao(db.Model):
    __tablename__ = "Pergunta_Dimensao"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    peso = db.Column(db.Integer)
    id_Dimensao = db.Column(db.Integer, db.ForeignKey("Dimensao.id"))
    Dimensao = db.relationship("Dimensao", back_populates="perguntas_Dimensao")

    id_pergunta = db.Column(db.String(10), db.ForeignKey("Pergunta.id"))
    pergunta = db.relationship("Pergunta", back_populates="Dimensaos_pergunta")

