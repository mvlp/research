from typing import Any, Set, Type

from sqlalchemy import Engine, select, text
from src.Entities.SelectDataEntity import SelectDataEntity
from src.Entities.Percentuais_CGVN_entity import Percentuais_CGVN_Entity
from src.Entities.Grafico_entity import Grafico_entity
from src.Entities.Governanca_entity import Governanca_entity
from src.infra.Database.Models.auto.cgvn_praticas import cgvn_praticas
from  src.infra.Database.repositories.Base_repository import E, M, BaseRepository
from sqlalchemy.orm import Session
import pandas as pd

class Governanca_repository(BaseRepository):
    def __init__(self, engine: Engine):
        super().__init__(Governanca_entity, cgvn_praticas, engine)

    def get_dados_importacao(self):
        sql = text("""
            select 
                count(distinct "ID_Documento") as documento_total,
                count(distinct "CNPJ_Companhia") as cnpj_total,
                min("Data_Entrega") as data_entrega_min,
                max("Data_Entrega") as data_entrega_max,
                min("Data_Referencia") as data_referencia_min,
                max("Data_Referencia") as data_referencia_max
            from cgvn_praticas;
        """)

        with Session(self.sql_engine) as session:
            result = session.execute(sql).mappings().all()
        result = result[0]
        return {
            "documento_total": result["documento_total"] ,
            "cnpj_total": result["cnpj_total"] ,
            "data_entrega_min": result["data_entrega_min"] ,
            "data_entrega_max": result["data_entrega_max"] ,
            "data_referencia_min": result["data_referencia_min"] ,
            "data_referencia_max": result["data_referencia_max"] ,
        }


    def get_empresa(self,empresa:str):
        sql = text("""
            SELECT DISTINCT "CNPJ_Companhia", "Nome_Empresarial"
            FROM cgvn_praticas
            WHERE
                "CNPJ_Companhia" LIKE :cnpj
                OR unaccent(lower("Nome_Empresarial"))
                LIKE unaccent(lower(:empresa))
        """)
        params = {
            "empresa": "%" + empresa.lower().replace(" ", "%") + "%",
            "cnpj": f"%{empresa}%"
        }

        with Session(self.sql_engine) as session:
            result = session.execute(sql,params).mappings().all()
        tabela = []
        for r in result:
            tabela.append(SelectDataEntity(str(r["Nome_Empresarial"]),str(r["CNPJ_Companhia"])))
        return tabela
    
    def get_dados_faltantes(self):
        sql = text("SELECT * FROM cgvn_dados_faltantes;")
        with Session(self.sql_engine) as session:
            result = session.execute(sql).mappings().all()
        lista = []
        return [Governanca_entity(dict(r)) for r in result]

    def get_tabela_percentuais(self) -> list[Percentuais_CGVN_Entity]:
        sql = text("""
                WITH counted AS (
                    SELECT
                        "ID_Item",
                        "Capitulo",
                        "Pratica_Recomendada",
                        "Pratica_Adotada",
                        "Principio",
                        COUNT("ID_Documento") AS qtd
                    FROM cgvn_praticas
                    GROUP BY
                        "ID_Item",
                        "Capitulo",
                        "Pratica_Recomendada",
                        "Pratica_Adotada",
                        "Principio"
                ),
                fractions AS (
                    SELECT
                        "ID_Item",
                        "Capitulo",
                        "Pratica_Recomendada",
                        "Pratica_Adotada",
                        "Principio",
                        CEILING(
                            1000.0 * qtd
                            / SUM(qtd) OVER (PARTITION BY "ID_Item")
                        ) / 10 AS fracao
                    FROM counted
                )
                SELECT
                    "ID_Item",
                    "Capitulo",
                    "Pratica_Recomendada",
                    "Principio",

                    COALESCE(MAX(fracao) FILTER (WHERE "Pratica_Adotada" = 'Sim'), 0)           AS perc_sim,
                    COALESCE(MAX(fracao) FILTER (WHERE "Pratica_Adotada" = 'Não'), 0)           AS perc_nao,
                    COALESCE(MAX(fracao) FILTER (WHERE "Pratica_Adotada" = 'Parcialmente'), 0)  AS perc_parcialmente,
                    COALESCE(MAX(fracao) FILTER (WHERE "Pratica_Adotada" = 'Não se Aplica'), 0) AS perc_nao_se_aplica

                FROM fractions
                GROUP BY
                    "ID_Item",
                    "Capitulo",
                    "Pratica_Recomendada",
                    "Principio"
                ORDER BY
                    "ID_Item";

                   """)

        with Session(self.sql_engine) as session:
            result = session.execute(sql).mappings().all()
        tabela = []
        for r in result:
            row = Percentuais_CGVN_Entity(
                str(r["ID_Item"]),
                str(r["Principio"]),
                str(r["Pratica_Recomendada"]),
                float(r["perc_nao"]),
                float(r["perc_nao_se_aplica"]),
                float(r["perc_parcialmente"]),
                float(r["perc_sim"])
            )
            tabela.append(row)
        return tabela

    def get_grafico_percentual2(self, chapter: str,resposta: str) -> Grafico_entity:
        sql = text("""
WITH tamanho_anual AS (

    SELECT DISTINCT ON (
        cnpj,
        EXTRACT(YEAR FROM trimestre)
    )

        cnpj,

        porte,

        EXTRACT(YEAR FROM trimestre) AS ano,

        trimestre

    FROM tamanho_empresa_b3

    ORDER BY
        cnpj,
        EXTRACT(YEAR FROM trimestre),
        trimestre DESC
),
base AS (
    SELECT
        "CNPJ_Companhia",
        date_trunc('quarter', "Data_Entrega")::date AS data_entrega,
        "ID_Documento",
        "Pratica_Adotada",
		tamanho_anual.porte
    FROM cgvn_praticas
	JOIN tamanho_anual on regexp_replace(cgvn_praticas."CNPJ_Companhia", '[^0-9]', '', 'g') = tamanho_anual.cnpj 
	AND EXTRACT(YEAR FROM cgvn_praticas."Data_Entrega"::date) = EXTRACT(YEAR FROM tamanho_anual.trimestre)
    WHERE "Capitulo" = :chapter
),
doc_cnts AS (
	SELECT
		"CNPJ_Companhia",
		data_entrega,
		"ID_Documento",
		"Pratica_Adotada",
		base.porte,
		COUNT(*) AS cnt
	FROM base
	GROUP BY
		"CNPJ_Companhia",
		data_entrega,
		"ID_Documento",
		"Pratica_Adotada",
		porte
),
doc_totals AS (
	SELECT
		"CNPJ_Companhia",
		data_entrega,
		"ID_Documento",
		doc_cnts.porte,
		SUM(cnt) AS total_doc
	FROM doc_cnts
	GROUP BY
		"CNPJ_Companhia",
		data_entrega,
		"ID_Documento",
		doc_cnts.porte
),
freq AS (

	SELECT
		c."CNPJ_Companhia",
		c.data_entrega,
		c."Pratica_Adotada",
		c."ID_Documento",
		t.porte,
		c.cnt::numeric / t.total_doc AS freq
	FROM doc_cnts c
	JOIN doc_totals t
	ON t."CNPJ_Companhia" = c."CNPJ_Companhia"
	AND t.data_entrega     = c.data_entrega
	AND t."ID_Documento"   = c."ID_Documento"
)

SELECT
	data_entrega,
	freq.porte,
	"Pratica_Adotada",
	100 * AVG(freq) AS ybar,
	COUNT(*) AS n
FROM freq WHERE "Pratica_Adotada" = :resposta
GROUP BY
	data_entrega,
	"Pratica_Adotada",
	freq.porte
ORDER BY
	data_entrega,
	"Pratica_Adotada";
    """)
        with Session(self.sql_engine) as session:
            result = session.execute(
                sql,
                {"chapter": chapter, "resposta":resposta}
            ).mappings().all()
        labels = sorted({
            str(r["data_entrega"])
            for r in result
        })
        dados = {}

        for r in result:
            chave = (
                str(r["data_entrega"]),
                r["porte"]
            )

            dados[chave] = float(r["ybar"])

        pequena = []
        media = []
        grande = []

        for label in labels:

            pequena.append(
                dados.get((label, "pequena"))
            )

            media.append(
                dados.get((label, "media"))
            )

            grande.append(
                dados.get((label, "grande"))
            )

        grafico = Grafico_entity(
            "2",
            labels,
            media,
            grande,
            pequena,
        )
        return grafico


    def get_grafico_percentual(self, chapter: str,resposta: str) -> Grafico_entity:
        ## ESSE deu trabalho
        sql = text("""
            WITH base AS (
                SELECT
                    "CNPJ_Companhia",
                    date_trunc('quarter', "Data_Entrega")::date AS data_entrega,
                    "ID_Documento",
                    "Pratica_Adotada"
                FROM cgvn_praticas
                WHERE "Capitulo" = :chapter
            ),
            doc_cnts AS (
                SELECT
                    "CNPJ_Companhia",
                    data_entrega,
                    "ID_Documento",
                    "Pratica_Adotada",
                    COUNT(*) AS cnt
                FROM base
                GROUP BY
                    "CNPJ_Companhia",
                    data_entrega,
                    "ID_Documento",
                    "Pratica_Adotada"
            ),
            doc_totals AS (
                SELECT
                    "CNPJ_Companhia",
                    data_entrega,
                    "ID_Documento",
                    SUM(cnt) AS total_doc
                FROM doc_cnts
                GROUP BY
                    "CNPJ_Companhia",
                    data_entrega,
                    "ID_Documento"
            ),
            freq AS (

                SELECT
                    c."CNPJ_Companhia",
                    c.data_entrega,
                    c."Pratica_Adotada",
                    c."ID_Documento",
                    c.cnt::numeric / t.total_doc AS freq
                FROM doc_cnts c
                JOIN doc_totals t
                ON t."CNPJ_Companhia" = c."CNPJ_Companhia"
                AND t.data_entrega     = c.data_entrega
                AND t."ID_Documento"   = c."ID_Documento"
            )

            SELECT
                data_entrega,
                "Pratica_Adotada",
                100 * AVG(freq) AS ybar,
                100 * percentile_cont(0.05)
                    WITHIN GROUP (ORDER BY freq) AS ylow,
                100 * percentile_cont(0.95)
                    WITHIN GROUP (ORDER BY freq) AS yhigh,
                COUNT(*) AS n
            FROM freq WHERE "Pratica_Adotada" = :resposta
            GROUP BY
                data_entrega,
                "Pratica_Adotada"
            ORDER BY
                data_entrega,
                "Pratica_Adotada";
                """)
        
        with Session(self.sql_engine) as session:
            result = session.execute(
                sql,
                {"chapter": chapter, "resposta":resposta}
            ).mappings().all()
        grafico = Grafico_entity(chapter,[],[],[],[])
        for r in result:
            grafico.labels.append(str(r["data_entrega"]))
            grafico.Dado.append(float(r["ybar"]))
            grafico.Limite_inferior.append(float(r["ylow"]))
            grafico.Limite_superior.append(float(r["yhigh"]))
        return grafico

    def get_grafico_quantidade(self, chapter: str, resposta: str) -> Grafico_entity:

        sql = text("""
                   select data_entrega, "Pratica_Adotada", count("ID_Documento") as quantidade 
                    from(
                        select distinct
                            "CNPJ_Companhia",
                            date_trunc('quarter', "Data_Entrega")::date AS data_entrega,
                            "ID_Documento",
                            "Pratica_Adotada"
                            from cgvn_praticas where "Capitulo" = :chapter and "Pratica_Adotada" = :resposta
                        )
                        group by data_entrega,"Pratica_Adotada" order by data_entrega;
                   """)
        with Session(self.sql_engine) as session:
            result = session.execute(
                sql,
                {"chapter": chapter, "resposta":resposta}
            ).mappings().all()
        grafico = Grafico_entity(chapter,[],[],[],[])
        for r in result:
            grafico.labels.append(str(r["data_entrega"]))
            grafico.Dado.append(float(r["quantidade"]))
        return grafico

    def get_grafico_quantidade2(self, chapter: str, resposta: str) -> Grafico_entity:

        sql = text("""
                   select porte, data_entrega, "Pratica_Adotada", count("ID_Documento") as quantidade 
                    from(
                        select distinct
                            "CNPJ_Companhia",
                            date_trunc('quarter', "Data_Entrega")::date AS data_entrega,
                            "ID_Documento",
                            "Pratica_Adotada",
                            tamanho_empresa_b3.porte
                            from cgvn_praticas 
                            JOIN tamanho_empresa_b3 on regexp_replace(cgvn_praticas."CNPJ_Companhia", '[^0-9]', '', 'g') = tamanho_empresa_b3.cnpj 
                            AND EXTRACT(YEAR FROM cgvn_praticas."Data_Entrega"::date) = EXTRACT(YEAR FROM tamanho_empresa_b3.trimestre) 
                            where "Capitulo" = :chapter and "Pratica_Adotada" = :resposta
                        )
                        group by data_entrega,"Pratica_Adotada", porte order by data_entrega, porte;
                   """)

        with Session(self.sql_engine) as session:
            result = session.execute(
                sql,
                {"chapter": chapter, "resposta":resposta}
            ).mappings().all()
        labels = sorted({
            str(r["data_entrega"])
            for r in result
        })
        dados = {}

        for r in result:
            chave = (
                str(r["data_entrega"]),
                r["porte"]
            )

            dados[chave] = float(r["quantidade"])

        pequena = []
        media = []
        grande = []

        for label in labels:

            pequena.append(
                dados.get((label, "pequena"))
            )

            media.append(
                dados.get((label, "media"))
            )

            grande.append(
                dados.get((label, "grande"))
            )

        grafico = Grafico_entity(
            "2",
            labels,
            media,
            grande,
            pequena,
        )
        return grafico
