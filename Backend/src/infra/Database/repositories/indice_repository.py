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

                WITH base_dimensao AS (
                    SELECT
                        d.id AS dimensao_id,
                        d.sigla
                    FROM "Dimensao" d
                    JOIN "Indice" i
                        ON d."idIndice" = i.id
                    WHERE i.id = :idIndice
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
                    (SUM(c.gc_value * peso) - l.valor_minimo_possivel * COUNT(DISTINCT("CNPJ_Companhia")))/( l.valor_maximo_possivel * COUNT(DISTINCT("CNPJ_Companhia")) - l.valor_minimo_possivel * COUNT(DISTINCT("CNPJ_Companhia"))) as normalizacao_global,
                    EXTRACT(YEAR FROM c."Data_Referencia"::date) AS dt
                FROM cgvn_praticas c
                JOIN perguntas p
                    ON c."ID_Item" = p.id_pergunta
                JOIN limites_dimensao l
                    ON l.dimensao_id = p.dimensao_id
                GROUP BY 
                    p.dimensao_id,
                    p.sigla,
                    l.valor_minimo_possivel,
                    l.valor_maximo_possivel,
                    EXTRACT(YEAR FROM c."Data_Referencia"::date)
                ORDER BY dt, p.dimensao_id;
            """)
        
        dados: dict[str, Grafico_chart_entity]= {}

        with Session(self.sql_engine) as session:
            empresa_dado = session.execute(
                empresa_sql,
                {"idIndice": idIndice, "cnpj_empresa":cnpj_empresa}
            ).mappings().all()
            media_dado =  session.execute(
                media_sql,
                {"idIndice": idIndice, "cnpj_empresa":cnpj_empresa}
            ).mappings().all()

        for e,m in zip(empresa_dado,media_dado):
            data = str(e["dt"])
            if not (dados.get(data)):
                dados[data] = Grafico_chart_entity([],[Dataset("Média geral"),Dataset(e["nome"])])
            grafico = dados[data]
            grafico.labels.append(str(m["sigla"]))
            grafico.datasets[0].data.append(m["normalizacao_global"])
            grafico.datasets[1].data.append(e["normalizacao"])

        return dados