from src.infra.Database.extensions import db

class dfp_composicao_capital(db.Model):
    __tablename__ = "dfp_composicao_capital"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    arquivo_origem = db.Column(db.Text, nullable=True)
    tipo_csv = db.Column(db.Text, nullable=True)

    CNPJ_CIA = db.Column(db.Text, nullable=True)
    DENOM_CIA = db.Column(db.Text, nullable=True)
    DT_REFER = db.Column(db.Date, nullable=True)
    VERSAO = db.Column(db.Integer, nullable=True)
    QT_ACAO_ORDIN_TESOURO = db.Column(db.BigInteger, nullable=True)
    QT_ACAO_TOTAL_TESOURO = db.Column(db.BigInteger, nullable=True)
    QT_ACAO_TOTAL_CAP_INTEGR = db.Column(db.BigInteger, nullable=True)
    QT_ACAO_PREF_TESOURO = db.Column(db.BigInteger, nullable=True)
    QT_ACAO_PREF_CAP_INTEGR = db.Column(db.BigInteger, nullable=True)
    QT_ACAO_ORDIN_CAP_INTEGR = db.Column(db.BigInteger, nullable=True)