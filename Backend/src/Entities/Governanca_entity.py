from typing import Any
from Backend.src.Entities.Base_entity import Base_entity
from  src.infra.Database.extensions import db
from  datetime import date

class Governanca_entity(Base_entity):
    CNPJ_Companhia: str
    Data_Referencia: date
    Nome_Empresarial: str
    ID_Documento: str
    ID_Item: str
    Capitulo: str
    Principio: str
    Pratica_Recomendada: str 
    Pratica_Adotada: str
    Explicacao: str
    Data_Entrega: date 
    gc_factor: str
    gc_value: int
    