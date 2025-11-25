from src.infra.Database.extensions import db

class Grupo_do_indice(db.Model):
    __tablename__ = "Grupo_do_indice"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    data_ini = db.Column(db.Date, nullable=False)
    data_fim = db.Column(db.Date, nullable=True)
    nome = db.Column(db.String(200), nullable=True)

    indices = db.relationship(
        "Indice",
        back_populates="grupo",
        cascade="all, delete-orphan"
    )
