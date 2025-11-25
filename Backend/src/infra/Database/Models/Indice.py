from src.infra.Database.extensions import db

class Indice(db.Model):
    __tablename__ = "Indice"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    idGrupo = db.Column(
        db.Integer,
        db.ForeignKey("Grupo_do_indice.id"),
        nullable=False
    )

    grupo = db.relationship(
        "Grupo_do_indice",
        back_populates="indices"
    )

    perguntas_indice = db.relationship(
        "Pergunta_indice",
        back_populates="indice",
        cascade="all, delete-orphan"
    )
