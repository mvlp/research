

from datetime import date
from typing import Any
from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session
from src.infra.Database.Models.Indice import Indice
from src.infra.Database.Models.Dimensao import Dimensao
from src.infra.Database.Models.pergunta import Pergunta
from src.infra.Database.Models.pergunta_dimensao import Pergunta_Dimensao
from src.scripts.codigoPython.url_db import url_db


def monta_dimensao(sigla: str, id_indice:int):
    dimensao = Dimensao()
    dimensao.idIndice = id_indice
    dimensao.sigla = sigla
    return dimensao

def cria_indices(engine):
    with Session(engine) as session:
        indice = Indice()
        indice.data_ini = date.today()
        indice.data_fim = None
        indice.nome = "Padrão"
        session.add(indice)
        session.commit()
        session.refresh(indice)
        dimensoes: list[Any] = [None]
        ac = monta_dimensao("AC",indice.id)
        session.add(ac)
        dimensoes.append(ac)
        ca = monta_dimensao("CA",indice.id)
        session.add(ca)
        dimensoes.append(ca)
        dr = monta_dimensao("DR",indice.id)
        session.add(dr)
        dimensoes.append(dr)
        ofc = monta_dimensao("OFC",indice.id)
        session.add(ofc)
        dimensoes.append(ofc)
        eci = monta_dimensao("ECI",indice.id)
        session.add(eci)
        dimensoes.append(eci)
        session.commit()
        for i in range(1,6):
            session.refresh(dimensoes[i])
            sql = text("""SELECT * FROM "Pergunta" WHERE id LIKE :IdItem;""")
            result = session.execute(sql,{"IdItem":str(i) +"%"}).unique().mappings().all()
            print(result.__len__())
            for registro in result:
                pd = Pergunta_Dimensao()
                pd.id_Dimensao = dimensoes[i].id
                pd.id_pergunta = registro["id"]
                session.add(pd)
            session.commit()

if __name__ == "__main__":
  engine = create_engine(url_db)
  cria_indices(engine)