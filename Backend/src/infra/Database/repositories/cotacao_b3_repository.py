from typing import Any, Type

from sqlalchemy import Engine, select, text
from src.infra.Database.Models.subscriptions_b3 import Subscriptions_b3
from src.Entities.Fator_b3 import Fator_b3
from src.infra.Database.Models.cotacao_b3 import CotacaoB3
from src.Entities.SelectDataEntity import SelectDataEntity
from src.Entities.Percentuais_CGVN_entity import Percentuais_CGVN_Entity
from src.Entities.Grafico_entity import Grafico_entity
from src.Entities.Cotacao_b3_entity import Cotacao_b3_entity
from src.infra.Database.Models.auto.cgvn_praticas import cgvn_praticas
from  src.infra.Database.repositories.Base_repository import E, M, BaseRepository
from sqlalchemy.orm import Session
import pandas as pd

class Cotacao_b3_repository(BaseRepository):
    def __init__(self, engine: Engine):
        super().__init__(Cotacao_b3_entity, CotacaoB3, engine)


	
	

    def get_subscricoes(self,codigo:str, data_fim:str):
        with Session(self.sql_engine) as session:
            query = select(Subscriptions_b3).where(Subscriptions_b3.isinCode == codigo, Subscriptions_b3.lastDatePrior < data_fim).order_by(Subscriptions_b3.lastDatePrior.desc())
            results = session.execute(query).scalars().all()
            lista = []
            for r in results:
                lista.append(self.entity_class.from_model(r))
            return lista

    def get_hist(self,codigo:str, data_fim:str):
        with Session(self.sql_engine) as session:
            query = select(CotacaoB3).where(CotacaoB3.codigo_negociacao == codigo, CotacaoB3.data_pregao < data_fim).order_by(CotacaoB3.data_pregao.asc())
            results = session.execute(query).scalars().all()
            lista = []
            for r in results:
                lista.append(self.entity_class.from_model(r))
            return lista


    def get_correcoes(self,codigo:str,data_fim:str):
        sql = text(""" 


WITH base AS (
    -- TABELA 1 (já agregada)
    SELECT 
        a."isinCode"      AS isin,
        a."lastDatePrior" AS last_date_prior,
        SUM(a.rate)       AS total_rate,
        c.preco_fechamento,
        1 AS prioridade
    FROM cash_dividends_b3 a
    JOIN cotacao_b3 c
        ON c.isin = a."isinCode"
        AND c.data_pregao = a."lastDatePrior"
    WHERE c.preco_fechamento > 0
      AND a."isinCode" = :code
      AND c.codigo_bdi = '2'
	  AND a."lastDatePrior" < :data_fim
    GROUP BY a."isinCode", a."lastDatePrior", c.preco_fechamento

    UNION ALL

    -- TABELA 2 (já agregada)
    SELECT 
        a."isinCode"      AS isin,
        a."lastDatePrior" AS last_date_prior,
        SUM(a.rate)       AS total_rate,
        c.preco_fechamento,
        2 AS prioridade
    FROM approved_cash_dividends_b3 a
    JOIN cotacao_b3 c
        ON c.isin = a."isinCode"
        AND c.data_pregao = a."lastDatePrior"
    WHERE c.preco_fechamento > 0
      AND a."isinCode" = :code
      AND c.codigo_bdi = '2'
	  AND a."lastDatePrior" < :data_fim
    GROUP BY a."isinCode", a."lastDatePrior", c.preco_fechamento
),

ranked AS (
    SELECT *,
        ROW_NUMBER() OVER (
            PARTITION BY isin, last_date_prior
            ORDER BY prioridade
        ) AS rn
    FROM base
),


total_cash_dividends AS (

	SELECT 
	    isin,
	    last_date_prior,
	    (preco_fechamento - total_rate) / preco_fechamento AS rate,
		total_rate,
		preco_fechamento
	FROM ranked
	WHERE rn = 1
	ORDER BY last_date_prior
),


stock_dividends AS (
	SELECT 
		s."isinCode"      AS isin,
		s."lastDatePrior" AS last_date_prior,
		CASE
			WHEN s.label IN ('BONIFICACAO', 'DESDOBRAMENTO') THEN
				1 / (1 + (s.factor / 100))

			WHEN s.label = 'GRUPAMENTO' THEN
				1 / s.factor

			ELSE
				1
		END AS rate
	FROM stock_dividends_b3 s
	WHERE s."isinCode" = :code AND s."lastDatePrior" < :data_fim
),
SELECT
	isin,
	last_date_prior,
	rate
FROM total_cash_dividends

UNION ALL

SELECT
	isin,
	last_date_prior,
	rate
FROM stock_dividends

ORDER BY last_date_prior;

                   """)

        with Session(self.sql_engine) as session:
            parametros = {"code": codigo,"data_fim": data_fim}
            result = session.execute(sql,parametros).mappings().all()
        tabela = []
        for r in result:
            tabela.append(Fator_b3.from_model(dict(r)))
        return tabela

   