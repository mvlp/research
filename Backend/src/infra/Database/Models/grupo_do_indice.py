

from  src.infra.Database.extensions import db

class Indice(db.Model):
    __tablename__ = "Grupo_do_indice"
    data_ini = db.Column(db.Date, nullable=False)
    data_fim = db.Column(db.Date, nullable=True)
    nome = db.Column(db.String(200), nullable=True)

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    Indice_grupo = db.relationship("Indice", back_populates="grupo")
