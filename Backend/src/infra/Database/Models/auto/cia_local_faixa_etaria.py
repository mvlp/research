from src.infra.Database.extensions import db

class cia_local_faixa_etaria(db.Model):
    __tablename__ = "cia_local_faixa_etaria"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    arquivo_origem = db.Column(db.Text, nullable=True)
    tipo_csv = db.Column(db.Text, nullable=True)

    CNPJ_Companhia = db.Column(db.Text, nullable=True)
    Data_Referencia = db.Column(db.Date, nullable=True)
    ID_Documento = db.Column(db.Integer, nullable=True)
    Nome_Companhia = db.Column(db.Text, nullable=True)
    Versao = db.Column(db.Integer, nullable=True)
    Local = db.Column(db.Text, nullable=True)
    Quantidade_Ate30Anos = db.Column(db.Integer, nullable=True)
    Quantidade_Acima50Anos = db.Column(db.Integer, nullable=True)
    Quantidade_30a50Anos = db.Column(db.Integer, nullable=True)