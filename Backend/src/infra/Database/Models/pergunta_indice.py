from  src.infra.Database.extensions import db

class Pergunta_indice(db.Model):
    __tablename__ = "Pergunta_indice"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_indice = db.Column(db.ForeignKey("Indice.id"))
    indice = db.relationship("Indice",back_populates="Pergunta_indice")

    id_pergunta = db.Column(db.ForeignKey("Pergunta.id"))
    pergunta = db.relationship("Pergunta",back_populates="Pergunta_indice")

