from src.infra.Database.extensions import db

class Indice(db.Model):
    __tablename__ = "Indice"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    data_ini = db.Column(db.Date, nullable=False)
    data_fim = db.Column(db.Date, nullable=True)
    nome = db.Column(db.String(200), nullable=True)

    Dimensaos = db.relationship(
        "Dimensao",
        back_populates="Indice",
        cascade="all, delete-orphan"
    )
