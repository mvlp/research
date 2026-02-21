from src.infra.Database.extensions import db

class fre_capital_social_reducao(db.Model):
    __tablename__ = "fre_capital_social_reducao"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    arquivo_origem = db.Column(db.Text, nullable=True)
    tipo_csv = db.Column(db.Text, nullable=True)

    CNPJ_Companhia = db.Column(db.Text, nullable=True)
    Data_Referencia = db.Column(db.Date, nullable=True)
    ID_Documento = db.Column(db.Integer, nullable=True)
    Nome_Companhia = db.Column(db.Text, nullable=True)
    Versao = db.Column(db.Integer, nullable=True)
    Quantidade_Acoes_Ordinarias = db.Column(db.Numeric(18, 0), nullable=True)
    Reducao_Capital_Anterior = db.Column(db.Numeric(18, 6), nullable=True)
    Quantidade_Acoes_Preferenciais = db.Column(db.Numeric(18, 0), nullable=True)
    ID_Capital_Social_Reducao = db.Column(db.Integer, nullable=True)
    Razao_Reducao = db.Column(db.Text, nullable=True)
    Forma_Restituicao = db.Column(db.Text, nullable=True)
    Data_Deliberacao = db.Column(db.Date, nullable=True)
    Data_Reducao = db.Column(db.Date, nullable=True)
    Valor_Total_Reducao = db.Column(db.Numeric(18, 2), nullable=True)
    Valor_Restituido_Por_Acao = db.Column(db.Numeric(18, 8), nullable=True)
    Quantidade_Total_Acoes = db.Column(db.Numeric(18, 0), nullable=True)