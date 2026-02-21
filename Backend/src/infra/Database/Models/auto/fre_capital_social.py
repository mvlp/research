from src.infra.Database.extensions import db

class fre_capital_social(db.Model):
    __tablename__ = "fre_capital_social"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    arquivo_origem = db.Column(db.Text, nullable=True)
    tipo_csv = db.Column(db.Text, nullable=True)

    CNPJ_Companhia = db.Column(db.Text, nullable=True)
    Data_Referencia = db.Column(db.Date, nullable=True)
    ID_Documento = db.Column(db.Integer, nullable=True)
    Nome_Companhia = db.Column(db.Text, nullable=True)
    Versao = db.Column(db.Integer, nullable=True)
    Data_Autorizacao_Aprovacao = db.Column(db.Date, nullable=True)
    Prazo_Integralizacao = db.Column(db.Text, nullable=True)
    Valor_Capital = db.Column(db.Numeric(18, 2), nullable=True)
    Quantidade_Acoes_Ordinarias = db.Column(db.Numeric(18, 0), nullable=True)
    Quantidade_Acoes_Preferenciais = db.Column(db.Numeric(18, 0), nullable=True)
    ID_Capital_Social = db.Column(db.Integer, nullable=True)
    Tipo_Capital = db.Column(db.Text, nullable=True)
    Quantidade_Total_Acoes = db.Column(db.Numeric(18, 0), nullable=True)