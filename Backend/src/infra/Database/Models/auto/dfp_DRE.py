from src.infra.Database.extensions import db

class dfp_DRE(db.Model):
    __tablename__ = "dfp_DRE"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    arquivo_origem = db.Column(db.Text, nullable=True)
    tipo_csv = db.Column(db.Text, nullable=True)

    CD_CONTA = db.Column(db.Text, nullable=True)
    CD_CVM = db.Column(db.Text, nullable=True)
    CNPJ_CIA = db.Column(db.Text, nullable=True)
    DENOM_CIA = db.Column(db.Text, nullable=True)
    DS_CONTA = db.Column(db.Text, nullable=True)
    DT_FIM_EXERC = db.Column(db.Date, nullable=True)
    DT_INI_EXERC = db.Column(db.Date, nullable=True)
    DT_REFER = db.Column(db.Date, nullable=True)
    ESCALA_MOEDA = db.Column(db.Text, nullable=True)
    GRUPO_DFP = db.Column(db.Text, nullable=True)
    MOEDA = db.Column(db.Text, nullable=True)
    ORDEM_EXERC = db.Column(db.Text, nullable=True)
    ST_CONTA_FIXA = db.Column(db.Text, nullable=True)
    VERSAO = db.Column(db.Integer, nullable=True)
    VL_CONTA = db.Column(db.Float, nullable=True)