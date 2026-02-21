from src.infra.Database.extensions import db

class Dimensao(db.Model):
    __tablename__ = "Dimensao"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    sigla = db.Column(db.Text, nullable=False)
    idIndice = db.Column(
        db.Integer,
        db.ForeignKey("Indice.id"),
        nullable=False
    )

    Indice = db.relationship(
        "Indice",
        back_populates="Dimensaos"
    )

    perguntas_Dimensao = db.relationship(
        "Pergunta_Dimensao",
        back_populates="Dimensao",
        cascade="all, delete-orphan"
    )
