from sqlalchemy import Integer,Date,Column
from src.infra.Database.extensions import db

class Indice_grupo(db.Model):
    __tablename__ = "Indice_grupo"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    data_ini = db.Column(db.Date, nullable=False)
    data_fim = db.Column(db.Date, nullable=False)
    indices = db.relationship("Indice", back_populates="Indice_grupo")
    