"""
Validação do modelo BARMA por holdout (leave-last-year-out), rodando
para TODAS as empresas do banco e gerando uma pontuação única agregada.

A ideia: para cada empresa, e para cada série histórica dela (dimensão x
porte, e dimensão x empresa) obtida via getIndiceOverview, remove-se o
último ano, treina-se o modelo com o restante e faz-se a previsão de
1 passo à frente. Depois compara-se o valor previsto com o valor real
que foi removido. No final, todos os erros (de todas as empresas, de
todas as séries) são agregados em uma única pontuação (MAE/RMSE/MAPE)
do modelo.

Os resultados são gravados em duas tabelas no próprio banco:
  - validacao_barma_detalhe: uma linha por série validada, por empresa
  - validacao_barma_resumo:  uma linha por execução, com a pontuação geral

USO
---
    python validar_barma.py

(cada execução cria uma nova leva de linhas nessas tabelas, marcada com
o timestamp da execução em data_execucao)
"""

from collections import defaultdict
from datetime import datetime

import numpy as np
from sqlalchemy import text, create_engine
from sqlalchemy.orm import Session

from src.infra.Database.repositories.indice_repository import Indice_repository
from src.services.BARMA_service import BARMA_service
from src.scripts.codigoPython.url_db import url_db

engine = create_engine(url_db)

ID_INDICE_PADRAO = 2  # fixo, conforme solicitado


# =========================================================
# Busca de todas as empresas (CNPJs) presentes no banco
# =========================================================

def listar_cnpjs(sql_engine) -> list[str]:
    """Retorna todos os CNPJs distintos presentes em cgvn_praticas."""
    sql = text('SELECT DISTINCT "CNPJ_Companhia" FROM cgvn_praticas ORDER BY 1;')
    with Session(sql_engine) as session:
        linhas = session.execute(sql).all()
    return [linha[0] for linha in linhas]


# =========================================================
# Extração de séries planas a partir do dicionário retornado
# por getIndiceOverview
# =========================================================

def extrair_series_de_overview(overview: dict) -> dict[str, list[float]]:
    """
    Recebe o dicionário {ano_ou_'previsao X': Grafico_chart_entity, ...}
    retornado por getIndiceOverview e devolve séries planas por
    (label do dataset + sigla), já ordenadas por ano e SEM incluir
    anos de previsão (chaves que começam com 'previsao'), para não
    vazar a previsão para dentro do treino/validação.
    """
    anos_reais = sorted(
        ano for ano in overview.keys() if not str(ano).startswith("previsao")
    )

    series: dict[str, list[float]] = defaultdict(list)

    for ano in anos_reais:
        grafico = overview[ano]
        for dataset in grafico.datasets:
            for sigla in grafico.labels:
                idx = grafico.labels.index(sigla)
                valor = dataset.data[idx] if idx < len(dataset.data) else 0.0
                chave = f"{dataset.label}_{sigla}"
                series[chave].append(float(valor))

    return dict(series)


# =========================================================
# Validação (holdout do último ano)
# =========================================================

def validar_serie(serie: list[float]) -> dict | None:
    """
    Remove o último ponto, treina com o restante, prevê 1 passo à frente
    e retorna a comparação com o valor real removido.
    """
    if len(serie) < 4:
        # precisa de pelo menos 3 pontos para treino + 1 para validar
        return None

    treino = serie[:-1]
    valor_real = serie[-1]

    previsao = BARMA_service.fit_and_forecast(treino, steps=1)
    if previsao is None:
        return None

    valor_previsto = previsao[0]
    erro_absoluto = abs(valor_real - valor_previsto)
    erro_percentual = (
        erro_absoluto / valor_real * 100 if valor_real != 0 else None
    )

    return {
        "valor_real": valor_real,
        "valor_previsto": valor_previsto,
        "erro_absoluto": erro_absoluto,
        "erro_percentual": erro_percentual,
    }


def validar_empresa(service, id_indice: int, cnpj_empresa: str) -> list[dict]:
    """Roda a validação de holdout em todas as séries de uma empresa."""
    resultados = []
    try:
        overview = service.getIndiceOverview(id_indice, cnpj_empresa)
    except Exception as e:
        print(f"[ERRO] {cnpj_empresa}: falha ao buscar overview ({e})")
        return resultados

    series = extrair_series_de_overview(overview)

    for id_serie, valores in series.items():
        r = validar_serie(valores)
        if r is None:
            continue
        r["cnpj"] = cnpj_empresa
        r["id_serie"] = id_serie
        resultados.append(r)

    return resultados


def rodar_validacao_geral(service, id_indice: int, cnpjs: list[str]) -> list[dict]:
    """Roda a validação para todas as empresas e retorna a lista completa
    de resultados individuais (uma linha por série validada, por empresa)."""
    todos_resultados: list[dict] = []

    for i, cnpj in enumerate(cnpjs, start=1):
        print(f"[{i}/{len(cnpjs)}] Validando empresa {cnpj}...")
        resultados_empresa = validar_empresa(service, id_indice, cnpj)

        if not resultados_empresa:
            print(f"  -> nenhuma série validável para {cnpj}")
            continue

        for r in resultados_empresa:
            print(
                f"  [OK] {r['id_serie']}: real={r['valor_real']:.4f} "
                f"previsto={r['valor_previsto']:.4f} "
                f"erro_abs={r['erro_absoluto']:.4f}"
            )

        todos_resultados.extend(resultados_empresa)

    return todos_resultados


# =========================================================
# Agregação em uma pontuação única
# =========================================================

def resumo_metrico(resultados: list[dict]) -> dict:
    """Agrega TODOS os resultados (todas as empresas, todas as séries)
    em uma única pontuação geral do modelo."""
    if not resultados:
        return {}

    erros_abs = np.array([r["erro_absoluto"] for r in resultados])
    reais = np.array([r["valor_real"] for r in resultados])
    previstos = np.array([r["valor_previsto"] for r in resultados])

    mae = float(np.mean(erros_abs))
    rmse = float(np.sqrt(np.mean((reais - previstos) ** 2)))

    percentuais = [
        r["erro_percentual"] for r in resultados if r["erro_percentual"] is not None
    ]
    mape = float(np.mean(percentuais)) if percentuais else None

    n_empresas = len({r["cnpj"] for r in resultados})

    return {
        "n_empresas_validadas": n_empresas,
        "n_series_validadas": len(resultados),
        "mae": mae,
        "rmse": rmse,
        "mape": mape,
    }


# =========================================================
# Gravação no banco
# =========================================================

def criar_tabelas(sql_engine) -> None:
    ddl_detalhe = text("""
        CREATE TABLE IF NOT EXISTS validacao_barma_detalhe (
            id SERIAL PRIMARY KEY,
            cnpj TEXT,
            id_serie TEXT,
            valor_real DOUBLE PRECISION,
            valor_previsto DOUBLE PRECISION,
            erro_absoluto DOUBLE PRECISION,
            erro_percentual DOUBLE PRECISION,
            data_execucao TIMESTAMP NOT NULL
        );
    """)

    ddl_resumo = text("""
        CREATE TABLE IF NOT EXISTS validacao_barma_resumo (
            id SERIAL PRIMARY KEY,
            n_empresas_validadas INTEGER,
            n_series_validadas INTEGER,
            mae DOUBLE PRECISION,
            rmse DOUBLE PRECISION,
            mape DOUBLE PRECISION,
            data_execucao TIMESTAMP NOT NULL
        );
    """)

    with Session(sql_engine) as session:
        session.execute(ddl_detalhe)
        session.execute(ddl_resumo)
        session.commit()


def salvar_detalhe_bd(sql_engine, resultados: list[dict], data_execucao: datetime) -> None:
    if not resultados:
        return

    insert_sql = text("""
        INSERT INTO validacao_barma_detalhe
            (cnpj, id_serie, valor_real, valor_previsto, erro_absoluto, erro_percentual, data_execucao)
        VALUES
            (:cnpj, :id_serie, :valor_real, :valor_previsto, :erro_absoluto, :erro_percentual, :data_execucao)
    """)

    linhas = [
        {
            "cnpj": r["cnpj"],
            "id_serie": r["id_serie"],
            "valor_real": r["valor_real"],
            "valor_previsto": r["valor_previsto"],
            "erro_absoluto": r["erro_absoluto"],
            "erro_percentual": r["erro_percentual"],
            "data_execucao": data_execucao,
        }
        for r in resultados
    ]

    with Session(sql_engine) as session:
        session.execute(insert_sql, linhas)
        session.commit()

    print(f"Gravadas {len(linhas)} linhas em validacao_barma_detalhe")


def salvar_resumo_bd(sql_engine, resumo: dict, data_execucao: datetime) -> None:
    if not resumo:
        return

    insert_sql = text("""
        INSERT INTO validacao_barma_resumo
            (n_empresas_validadas, n_series_validadas, mae, rmse, mape, data_execucao)
        VALUES
            (:n_empresas_validadas, :n_series_validadas, :mae, :rmse, :mape, :data_execucao)
    """)

    with Session(sql_engine) as session:
        session.execute(insert_sql, {**resumo, "data_execucao": data_execucao})
        session.commit()

    print("Gravado resumo em validacao_barma_resumo")


# =========================================================
# Execução
# =========================================================

def main():
    service = Indice_repository(engine)

    criar_tabelas(engine)

    cnpjs = listar_cnpjs(engine)
    print(f"Encontradas {len(cnpjs)} empresas no banco. Iniciando validação...\n")

    resultados = rodar_validacao_geral(service, ID_INDICE_PADRAO, cnpjs)

    print("\n===== PONTUAÇÃO GERAL DO MODELO (todas as empresas) =====")
    resumo = resumo_metrico(resultados)
    for k, v in resumo.items():
        if isinstance(v, float):
            print(f"{k}: {v:.4f}")
        else:
            print(f"{k}: {v}")

    data_execucao = datetime.now()
    salvar_detalhe_bd(engine, resultados, data_execucao)
    salvar_resumo_bd(engine, resumo, data_execucao)


if __name__ == "__main__":
    main()