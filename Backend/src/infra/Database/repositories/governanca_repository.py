from typing import Any, Type

from sqlalchemy import Engine, select, text
from src.Entities.Grafico_entity import Grafico_entity
from src.Entities import Governanca_entity
from src.infra.Database.Models.auto.cgvn_praticas import cgvn_praticas
from  src.infra.Database.repositories.Base_repository import E, M, BaseRepository
from sqlalchemy.orm import Session

class Governanca_repository(BaseRepository):
    def __init__(self, engine: Engine):
        super().__init__(Governanca_entity, cgvn_praticas, engine)

    def get_grafico_quantidade(self, capitulo: str):
        stmt = text("""
            SELECT *
            FROM gerar_grafico_quantidade(:capitulo)
        """)
        
        with Session(self.sql_engine) as session:
            result = session.execute(
                stmt,
                {"capitulo": capitulo}
            ).mappings().all()
        grafico = Grafico_entity(capitulo,[],[],[],[])
        for r in result:
            grafico.labels.append(str(r["data_entrega"]))
            grafico.Dado.append(float(r["quantidade"]))
        return grafico

        

    def gerar_grafico_percentual(self,capitulo: str) -> Grafico_entity:
        stmt = text("""
            SELECT *
            FROM gerar_grafico_percentual(:capitulo)
        """)
        
        with Session(self.sql_engine) as session:
            result = session.execute(
                stmt,
                {"capitulo": capitulo}
            ).mappings().all()
        grafico = Grafico_entity(capitulo,[],[],[],[])
        for r in result:
            grafico.labels.append(str(r["data_entrega"]))
            grafico.Dado.append(float(r["media"]))
            grafico.Limite_superior.append(float(r["limite_superior"]))
            grafico.Limite_inferior.append(float(r["limite_inferior"]))
        return grafico
