from  src.infra.Database.extensions import db

class Pergunta(db.Model):
    __tablename__ = "Pergunta"
    id = db.Column(db.String(10), nullable=False,primary_key=True)
    texto = db.Column(db.Text, nullable=False)


    Dimensaos_pergunta = db.relationship(
        "Pergunta_Dimensao",
        back_populates="pergunta",
        cascade="all, delete-orphan"
    )