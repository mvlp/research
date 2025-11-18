from sqlalchemy import Integer,Date,Column
from src.infra.Database.extensions import db

class Indice_grupo(db.Model):
    __tablename__ = "Indice_grupo"
    id = Column(Integer, primary_key=True, autoincrement=True)
    data_ini = Column(Date, nullable=False)
    data_fim = Column(Date, nullable=False)
    indices = db.relationship("Indice", back_populates="Indice_grupo")
    