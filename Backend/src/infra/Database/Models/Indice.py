from  src.infra.Database.extensions import db

class Indice(db.Model):
    __tablename__ = "Indice"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_grupo = db.Column(db.Integer, db.ForeignKey("Indice.id"))
    grupo = db.relationship("Grupo", back_populates="Indice_grupo")

    perguntas_indice = db.relationship(
        "Pergunta_indice",
        back_populates="indice",
        cascade="all, delete-orphan"
    )