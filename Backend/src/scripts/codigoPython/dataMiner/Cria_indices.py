

from datetime import date
from typing import Any
from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session
from Backend.src.infra.Database.Models.Indice import Indice
from Backend.src.infra.Database.Models.Dimensao import Dimensao
from Backend.src.infra.Database.Models.pergunta_dimensao import Pergunta_Dimensao
from Backend.src.scripts.codigoPython.dataMiner.url_db import url_db


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
            sql = text("""SELECT * FROM cgvn_praticas WHERE "ID_Item" LIKE :IdItem;""")
            result = session.execute(sql,{"IdItem":str(i) +"%"}).mappings().all()
            print(result)
            for registro in result:
                pd = Pergunta_Dimensao()
                pd.id_Dimensao = dimensoes[i].id
                pd.id_pergunta = registro["ID_Item"]
                session.add(pd)
            session.commit()

if __name__ == "__main__":
  engine = create_engine(url_db)
  cria_indices(engine)