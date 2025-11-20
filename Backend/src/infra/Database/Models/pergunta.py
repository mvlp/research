from  src.infra.Database.extensions import db

class Pergunta(db.Model):
    __tablename__ = "Pergunta"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    texto = db.Column(db.String(200), nullable=False)
    identificador = db.Column(db.String(10), nullable=False)


    indices_pergunta = db.relationship(
        "Pergunta_indice",
        back_populates="pergunta",
        cascade="all, delete-orphan"
    )