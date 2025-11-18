from  src.infra.Database.extensions import db

class Indice(db.Model):
    __tablename__ = "Indice"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_grupo = db.Column(db.ForeignKey("Indice_grupo.id"))
    grupo = db.relationship("Indice_grupo",back_populates="Indice")

