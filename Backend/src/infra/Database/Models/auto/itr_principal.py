from src.infra.Database.extensions import db

class itr_principal(db.Model):
    __tablename__ = "itr_principal"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    arquivo_origem = db.Column(db.Text, nullable=True)
    tipo_csv = db.Column(db.Text, nullable=True)

    CATEG_DOC = db.Column(db.Text, nullable=True)
    CD_CVM = db.Column(db.Text, nullable=True)
    CNPJ_CIA = db.Column(db.Text, nullable=True)
    DENOM_CIA = db.Column(db.Text, nullable=True)
    DT_RECEB = db.Column(db.Date, nullable=True)
    DT_REFER = db.Column(db.Date, nullable=True)
    ID_DOC = db.Column(db.Integer, nullable=True)
    LINK_DOC = db.Column(db.Text, nullable=True)
    VERSAO = db.Column(db.Integer, nullable=True)