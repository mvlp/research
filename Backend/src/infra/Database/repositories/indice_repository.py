from typing import Any
from sqlalchemy import Engine, text
from sqlalchemy.orm import Session
from src.Entities.Grafico_chart_entity import Dataset, Grafico_chart_entity
from src.Entities.Grafico_entity import Grafico_entity
from src.Entities.Indice_entity import Indice_entity
from src.infra.Database.Models.Indice import Indice
from src.infra.Database.repositories.Base_repository import BaseRepository


class Indice_repository(BaseRepository):
    def __init__(self, engine: Engine):
        super().__init__(Indice_entity, Indice, engine)
    
    def getIndiceOverview(self,idIndice: int, cnpj_empresa: str) -> dict[str, Grafico_chart_entity]:
        empresa_sql = text("""

            WITH base_dimensao AS (
                SELECT
                    d.id AS dimensao_id
                FROM "Dimensao" d
                JOIN "Indice" i
                    ON d."idIndice" = i.id
                WHERE i.id = :idIndice
            ),
            perguntas AS (
                SELECT
                    p.id_pergunta,
                    p.peso,
                    b.dimensao_id
                FROM "Pergunta_Dimensao" p
                JOIN base_dimensao b
                    ON p."id_Dimensao" = b.dimensao_id
            ),
            limites_dimensao AS (
                SELECT
                    dimensao_id,
                    SUM(LEAST(peso * 0, peso * 3)) AS valor_minimo_possivel,
                    SUM(GREATEST(peso * 0, peso * 3)) AS valor_maximo_possivel
                FROM perguntas
                GROUP BY dimensao_id
            )
            SELECT 
                p.dimensao_id,
                (SUM(c.gc_value * peso) - l.valor_minimo_possivel)/( l.valor_maximo_possivel - l.valor_minimo_possivel) as normalizacao,
                EXTRACT(YEAR FROM c."Data_Referencia"::date) AS dt,
                c."CNPJ_Companhia",
				c."Nome_Empresarial" as nome
				
            FROM cgvn_praticas c
            JOIN perguntas p
                ON c."ID_Item" = p.id_pergunta
            JOIN limites_dimensao l
                ON l.dimensao_id = p.dimensao_id
            WHERE c."CNPJ_Companhia" = :cnpj_empresa
            GROUP BY 
                p.dimensao_id,
                l.valor_minimo_possivel,
                l.valor_maximo_possivel,
				c."Nome_Empresarial", 
                EXTRACT(YEAR FROM c."Data_Referencia"::date),
                c."CNPJ_Companhia"
            ORDER BY dt, p.dimensao_id;
            """)
        media_sql = text(
            """
			DROP TABLE IF EXISTS tamanho_empresa_b3_expandido_anual;

CREATE TABLE tamanho_empresa_b3_expandido_anual AS

WITH anual AS (

    SELECT DISTINCT ON (
        cnpj,
        date_trunc('year', trimestre)
    )

        cnpj,

        porte,

        date_trunc('year', trimestre)::date AS ano,

        trimestre

    FROM tamanho_empresa_b3

    ORDER BY
        cnpj,
        date_trunc('year', trimestre),
        trimestre DESC
),

base AS (

    SELECT
        cnpj,

        porte,

        ano,

        LEAD(ano)
        OVER (
            PARTITION BY cnpj
            ORDER BY ano
        ) AS proximo_ano

    FROM anual
),

expandido AS (

    SELECT
        b.cnpj,

        b.porte,

        generate_series(
            b.ano,

            COALESCE(
                b.proximo_ano - interval '1 year',
                date_trunc('year', CURRENT_DATE)
            ),

            interval '1 year'
        )::date AS ano

    FROM base b
)

SELECT DISTINCT
    cnpj,
    porte,
    ano

FROM expandido;

-- ###################3
			WITH base_dimensao AS (
                    SELECT
                        d.id AS dimensao_id,
                        d.sigla
                    FROM "Dimensao" d
                    JOIN "Indice" i
                        ON d."idIndice" = i.id
                    WHERE i.id = 2
                ),
                perguntas AS (
                    SELECT
                        p.id_pergunta,
                        p.peso,
                        b.dimensao_id,
                        b.sigla
                    FROM "Pergunta_Dimensao" p
                    JOIN base_dimensao b
                        ON p."id_Dimensao" = b.dimensao_id
                ),
                limites_dimensao AS (
                    SELECT
                        dimensao_id,
                        SUM(LEAST(peso * 0, peso * 3)) AS valor_minimo_possivel,
                        SUM(GREATEST(peso * 0, peso * 3)) AS valor_maximo_possivel
                    FROM perguntas
                    GROUP BY dimensao_id
                )

                SELECT 
                    p.dimensao_id,
                    p.sigla,
					l.valor_minimo_possivel,
					l.valor_maximo_possivel,
					SUM(c.gc_value * peso),
					COUNT(DISTINCT("CNPJ_Companhia")),
                    (SUM(c.gc_value * peso) - l.valor_minimo_possivel * COUNT(DISTINCT("CNPJ_Companhia")))/( l.valor_maximo_possivel * COUNT(DISTINCT("CNPJ_Companhia")) - l.valor_minimo_possivel * COUNT(DISTINCT("CNPJ_Companhia"))) as normalizacao_global,
                    porte,
                    EXTRACT(YEAR FROM c."Data_Referencia"::date) AS dt
                FROM cgvn_praticas c
                JOIN perguntas p
                    ON c."ID_Item" = p.id_pergunta
                JOIN limites_dimensao l
                    ON l.dimensao_id = p.dimensao_id
                JOIN tamanho_empresa_b3_expandido_anual t ON regexp_replace(c."CNPJ_Companhia", '[^0-9]', '', 'g') = t.cnpj 
				AND EXTRACT(YEAR FROM c."Data_Referencia"::date) = EXTRACT(YEAR FROM t.ano)
                GROUP BY 
                    p.dimensao_id,
                    p.sigla,
                    l.valor_minimo_possivel,
                    l.valor_maximo_possivel,
                    porte,
                    EXTRACT(YEAR FROM c."Data_Referencia"::date)
                ORDER BY dt, p.dimensao_id;

            """)

        dados: dict[str, Grafico_chart_entity] = {}

        with Session(self.sql_engine) as session:

            empresa_dado = session.execute(
                empresa_sql,
                {
                    "idIndice": idIndice,
                    "cnpj_empresa": cnpj_empresa
                }
            ).mappings().all()

            media_dado = session.execute(
                media_sql,
                {
                    "idIndice": idIndice
                }
            ).mappings().all()

        # =========================
        # monta estrutura base
        # =========================

        for row in media_dado:

            data = str(row["dt"])

            if data not in dados:

                dados[data] = Grafico_chart_entity(
                    [],
                    [
                        Dataset("Pequena empresa", "rgb(85, 190, 122,0.6)"),
                        Dataset("Média empresa","rgb(72, 176, 150,0.6)"),
                        Dataset("Grande empresa","rgb(64, 160, 190,0.6)"),
                        Dataset("Empresa","rgb(214, 92, 92,0.8)"),
                    ]
                )

            grafico = dados[data]

            sigla = str(row["sigla"])

            if sigla not in grafico.labels:
                grafico.labels.append(sigla)

            indice_sigla = grafico.labels.index(sigla)

            for dataset in grafico.datasets:
                while len(dataset.data) < len(grafico.labels):
                    dataset.data.append(0)

            porte = row["porte"]
            valor = float(row["normalizacao_global"])

            if porte == "pequena":
                grafico.datasets[0].data[indice_sigla] = valor

            elif porte == "media":
                grafico.datasets[1].data[indice_sigla] = valor

            elif porte == "grande":
                grafico.datasets[2].data[indice_sigla] = valor

        # =========================
        # adiciona empresa
        # =========================

        for row in empresa_dado:

            data = str(row["dt"])

            if data not in dados:
                continue

            grafico = dados[data]

            dimensao_id = row["dimensao_id"]
            valor = float(row["normalizacao"])

            # precisa mapear dimensao -> sigla
            # porque empresa_sql não retorna sigla
            # ideal é incluir sigla no SQL

            sigla_map = {
                21: "AC",
                22: "CA",
                23: "DI",
                24: "OFC",
                25: "ECI"
            }

            sigla = sigla_map.get(dimensao_id)

            if sigla is None:
                continue

            if sigla not in grafico.labels:
                grafico.labels.append(sigla)

                for dataset in grafico.datasets:
                    while len(dataset.data) < len(grafico.labels):
                        dataset.data.append(0)

            indice_sigla = grafico.labels.index(sigla)

            grafico.datasets[3].data[indice_sigla] = valor

            # opcional: coloca nome real da empresa
            grafico.datasets[3].label = row["nome"]

        return dados