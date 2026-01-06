from src.infra.Database.extensions import db

class itr_parecer(db.Model):
    __tablename__ = "itr_parecer"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    arquivo_origem = db.Column(db.Text, nullable=True)
    tipo_csv = db.Column(db.Text, nullable=True)

    CNPJ_CIA = db.Column(db.Text, nullable=True)
    DENOM_CIA = db.Column(db.Text, nullable=True)
    DT_REFER = db.Column(db.Date, nullable=True)
    NUM_ITEM_PARECER_DECL = db.Column(db.Integer, nullable=True)
    TP_PARECER_DECL = db.Column(db.Text, nullable=True)
    TP_RELAT_ESP = db.Column(db.Text, nullable=True)
    TXT_PARECER_DECL = db.Column(db.Text, nullable=True)
    VERSAO = db.Column(db.Integer, nullable=True)