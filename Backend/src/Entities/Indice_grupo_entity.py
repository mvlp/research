from  src.Entities.Base_entity import Base_entity
from src.infra.Database.extensions import db
from  datetime import date

class Indice_grupo_entity(Base_entity):
    data_ini = date
    data_fim = date
    