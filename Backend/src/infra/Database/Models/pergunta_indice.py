from  src.infra.Database.extensions import db

class Pergunta_indice(db.Model):
    __tablename__ = "Pergunta_indice"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_indice = db.Column(db.Integer, db.ForeignKey("Indice.id"))
    indice = db.relationship("Indice", back_populates="perguntas_indice")

    id_pergunta = db.Column(db.Integer, db.ForeignKey("Pergunta.id"))
    pergunta = db.relationship("Pergunta", back_populates="indices_pergunta")

