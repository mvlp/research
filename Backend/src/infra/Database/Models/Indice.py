from  src.infra.Database.extensions import db

class Indice(db.Model):
    __tablename__ = "Indice"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    data_ini = db.Column(db.Date, nullable=False)
    data_fim = db.Column(db.Date, nullable=False)


    perguntas_indice = db.relationship(
        "Pergunta_indice",
        back_populates="indice",
        cascade="all, delete-orphan"
    )