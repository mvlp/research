from src.infra.Database.extensions import db

class fre_capital_social_titulo_conversivel(db.Model):
    __tablename__ = "fre_capital_social_titulo_conversivel"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    arquivo_origem = db.Column(db.Text, nullable=True)
    tipo_csv = db.Column(db.Text, nullable=True)

    CNPJ_Companhia = db.Column(db.Text, nullable=True)
    Data_Referencia = db.Column(db.Date, nullable=True)
    ID_Documento = db.Column(db.Integer, nullable=True)
    Nome_Companhia = db.Column(db.Text, nullable=True)
    Versao = db.Column(db.Integer, nullable=True)
    Condicoes_Conversao = db.Column(db.Text, nullable=True)
    ID_Capital_Social = db.Column(db.Integer, nullable=True)
    Titulo_Conversivel_Acao = db.Column(db.Text, nullable=True)