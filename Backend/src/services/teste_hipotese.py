"""
Teste de hipótese: o índice de governança difere entre empresas
grandes e pequenas?

H0: media(indice_grande) == media(indice_pequena)
H1: media(indice_grande) != media(indice_pequena)

"""

from collections import defaultdict

import numpy as np
from scipy import stats
from sqlalchemy import text, create_engine
from sqlalchemy.orm import Session

from src.scripts.codigoPython.url_db import url_db

engine = create_engine(url_db)

ID_INDICE_PADRAO = 2  # fixo, mesmo índice usado na validação do BARMA



# =========================================================
# Busca do índice geral por empresa/ano, com porte
# =========================================================

SQL_INDICE_POR_EMPRESA = text("""
    WITH base_dimensao AS (
        SELECT
            d.id AS dimensao_id,
            d.sigla
        FROM "Dimensao" d
        JOIN "Indice" i
            ON d."idIndice" = i.id
        WHERE i.id = :id_indice
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
    ),
    indice_por_dimensao AS (
        SELECT
            c."CNPJ_Companhia" AS cnpj,
            p.dimensao_id,
            EXTRACT(YEAR FROM c."Data_Referencia"::date) AS ano,
            t.porte,
            (SUM(c.gc_value * p.peso) - l.valor_minimo_possivel)
                / (l.valor_maximo_possivel - l.valor_minimo_possivel) AS normalizacao
        FROM cgvn_praticas c
        JOIN perguntas p
            ON c."ID_Item" = p.id_pergunta
        JOIN limites_dimensao l
            ON l.dimensao_id = p.dimensao_id
        JOIN tamanho_empresa_b3_expandido_anual t
            ON regexp_replace(c."CNPJ_Companhia", '[^0-9]', '', 'g') = t.cnpj
            AND EXTRACT(YEAR FROM c."Data_Referencia"::date) = EXTRACT(YEAR FROM t.ano)
        GROUP BY
            c."CNPJ_Companhia",
            p.dimensao_id,
            l.valor_minimo_possivel,
            l.valor_maximo_possivel,
            EXTRACT(YEAR FROM c."Data_Referencia"::date),
            t.porte
    )
    SELECT
        cnpj,
        ano,
        porte,
        AVG(normalizacao) AS indice_geral
    FROM indice_por_dimensao
    GROUP BY cnpj, ano, porte;
""")


def buscar_indice_por_empresa(sql_engine, id_indice: int) -> list[dict]:
    with Session(sql_engine) as session:
        linhas = session.execute(SQL_INDICE_POR_EMPRESA, {"id_indice": id_indice}).mappings().all()
    return [dict(linha) for linha in linhas]


# =========================================================
# Separação em grupos (grande vs pequena)
# =========================================================

def separar_grupos(linhas: list[dict]) -> tuple[np.ndarray, np.ndarray]:
    grupos = defaultdict(list)
    for linha in linhas:
        porte = linha["porte"]
        valor = linha["indice_geral"]
        if porte is None or valor is None:
            continue
        grupos[str(porte).strip().lower()].append(float(valor))

    grande = np.array(grupos.get("grande", []))
    pequena = np.array(grupos.get("pequena", []))
    return grande, pequena


# =========================================================
# Teste de hipótese
# =========================================================

def rodar_teste_hipotese(grande: np.ndarray, pequena: np.ndarray) -> None:
    ALPHA = 0.05
    print(f"n (grande)  = {len(grande)}")
    print(f"n (pequena) = {len(pequena)}\n")

    if len(grande) < 3 or len(pequena) < 3:
        print("Amostra pequena demais para rodar o teste (mínimo 3 por grupo).")
        return

    print("\n=> Ao menos um grupo não parece normal (p <= 0.05). Usando Mann-Whitney U.\n")
    estatistica, p_valor = stats.mannwhitneyu(grande, pequena, alternative="two-sided")
    nome_teste = "Mann-Whitney U (não-paramétrico)"

    print(f"Estatística: {estatistica:.4f}")
    print(f"p-valor: {p_valor:.4f}")

    print(f"\nMédia índice geral (grande):  {np.mean(grande):.4f}")
    print(f"Média índice geral (pequena): {np.mean(pequena):.4f}")

    print("\n===== CONCLUSÃO =====")
    if p_valor < ALPHA:
        print(
            f"p-valor ({p_valor:.4f}) < alpha ({ALPHA}) -> rejeita-se H0.\n"
            "Há evidência estatística de que o índice de governança difere "
            "entre empresas grandes e pequenas."
        )
    else:
        print(
            f"p-valor ({p_valor:.4f}) >= alpha ({ALPHA}) -> não se rejeita H0.\n"
            "Não há evidência estatística suficiente de diferença no índice "
            "de governança entre empresas grandes e pequenas."
        )


def main():
    linhas = buscar_indice_por_empresa(engine, ID_INDICE_PADRAO)
    print(f"Registros (empresa x ano) encontrados: {len(linhas)}\n")

    grande, pequena = separar_grupos(linhas)
    rodar_teste_hipotese(grande, pequena)


if __name__ == "__main__":
    print("asdasd")
    main()
