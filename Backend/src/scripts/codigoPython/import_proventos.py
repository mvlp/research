import argparse
import csv
import sys
from datetime import datetime
from decimal import Decimal, InvalidOperation

from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

from src.scripts.codigoPython.url_db import url_db

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

DATE_FORMATS = ["%m/%d/%Y", "%d/%m/%Y", "%Y-%m-%d"]


def parse_date(value: str):
    value = value.strip()
    if not value:
        return None
    for fmt in DATE_FORMATS:
        try:
            return datetime.strptime(value, fmt).date()
        except ValueError:
            continue
    print(f"  [WARN] Data não reconhecida: '{value}'")
    return None


def parse_decimal(value: str):
    value = value.strip().replace(",", ".")
    if not value:
        return None
    try:
        return Decimal(value)
    except InvalidOperation:
        return None


# ---------------------------------------------------------------------------
# ISIN cache – evita consultas repetidas para o mesmo papel
# ---------------------------------------------------------------------------

_isin_cache: dict[str, str | None] = {}


def get_isin(conn, codigo: str) -> str | None:
    if codigo in _isin_cache:
        return _isin_cache[codigo]

    result = conn.execute(
        text(
            """
            SELECT isin
            FROM   cotacao_b3
            WHERE  codigo_negociacao = :codigo
            ORDER  BY data_pregao ASC
            LIMIT  1
            """
        ),
        {"codigo": codigo},
    ).fetchone()

    isin = result[0] if result else None
    _isin_cache[codigo] = isin

    if isin is None:
        print(f"  [WARN] ISIN não encontrado para '{codigo}'")

    return isin


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():

    # parser = argparse.ArgumentParser(description="Importa proventos B3 para o banco.")
    # parser.add_argument("--csv",  required=True, help="Caminho para o arquivo CSV")
    # parser.add_argument("--db",   required=True, help="SQLAlchemy DB URL")
    # parser.add_argument(
    #     "--batch", type=int, default=500,
    #     help="Tamanho do lote para commit (padrão: 500)"
    # )
    # parser.add_argument(
    #     "--skip-existing", action="store_true",
    #     help="Pula registros já existentes (mesmo assetIssued + lastDatePrior + rate)"
    # )
    # args = parser.parse_args()
    batch = 500
    engine  = create_engine(url_db, echo=False)
    Session = sessionmaker(bind=engine)

    # Importação lazy para não exigir o app Flask no contexto do script
    # Ajuste o import abaixo conforme a estrutura do seu projeto
    try:
        from main import db  # noqa: F401 – garante metadados mapeados
        from src.infra.Database.Models.cash_dividends_b3 import Cash_dividends_b3
    except ImportError:
        print(
            "[ERRO] Não foi possível importar 'Cash_dividends_b3'.\n"
            "       Ajuste o import no topo deste script conforme seu projeto."
        )
        sys.exit(1)

    inserted = 0
    skipped  = 0
    errors   = 0
    
    with open("/home/guilhermedesouzafornaciari/Documentos/github/research/Backend/src/scripts/codigoPython/planilhas/Todas empresas proventos.csv", newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)

        session = Session()
        try:
            conn = engine.connect()  # conexão dedicada para as consultas de ISIN

            for i, row in enumerate(reader, start=1):
                try:
                    asset    = row["Papel"].strip()
                    last_dt  = parse_date(row["Último Dia Com"])
                    pay_dt   = parse_date(row["Data de Pagamento"])
                    rate_val = parse_decimal(row["Valor Provento"])

                    if last_dt is None or rate_val is None:
                        print(f"  [SKIP] Linha {i}: lastDatePrior ou rate inválido – {row}")
                        skipped += 1
                        continue

                    isin = get_isin(conn, asset)
                    record = Cash_dividends_b3()
                    record.assetIssued = asset
                    record.paymentDate = pay_dt
                    record.rate = rate_val
                    record.relatedTo = row["Tipo"].strip() or None
                    record.isinCode = isin
                    record.approvedOn = None
                    record.label = row["Tipo do Provento"].strip() or None
                    record.lastDatePrior = last_dt
                    record.remarks = row["Descrição/Emissor"].strip() or None
                    record.value_at_date = parse_decimal(row["Último Preço Com"])
                    session.add(record)
                    inserted += 1

                    if inserted % batch == 0:
                        session.commit()
                        print(f"  [INFO] {inserted} registros inseridos…")

                except Exception as exc:
                    print(f"  [ERRO] Linha {i}: {exc} – {row}")
                    errors += 1

            session.commit()
            conn.close()

        except Exception:
            session.rollback()
            raise
        finally:
            session.close()

    print(
        f"\nConcluído: {inserted} inseridos | {skipped} pulados | {errors} erros"
    )


if __name__ == "__main__":
    main()
