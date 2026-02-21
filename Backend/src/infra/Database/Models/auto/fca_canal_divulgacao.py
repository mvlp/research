from src.infra.Database.extensions import db

class fca_canal_divulgacao(db.Model):
    __tablename__ = "fca_canal_divulgacao"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    arquivo_origem = db.Column(db.Text, nullable=True)
    tipo_csv = db.Column(db.Text, nullable=True)

    Canal_Divulgacao = db.Column(db.Text, nullable=True)
    CNPJ_Companhia = db.Column(db.Text, nullable=True)
    Data_Referencia = db.Column(db.Date, nullable=True)
    ID_Documento = db.Column(db.Integer, nullable=True)
    Nome_Empresarial = db.Column(db.Text, nullable=True)
    Sigla_UF = db.Column(db.Text, nullable=True)
    Versao = db.Column(db.Integer, nullable=True)