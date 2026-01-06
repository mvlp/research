from src.infra.Database.extensions import db

class fre_capital_social_aumento(db.Model):
    __tablename__ = "fre_capital_social_aumento"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    arquivo_origem = db.Column(db.Text, nullable=True)
    tipo_csv = db.Column(db.Text, nullable=True)

    CNPJ_Companhia = db.Column(db.Text, nullable=True)
    Data_Emissao = db.Column(db.Date, nullable=True)
    Data_Referencia = db.Column(db.Date, nullable=True)
    ID_Documento = db.Column(db.Integer, nullable=True)
    Nome_Companhia = db.Column(db.Text, nullable=True)
    Versao = db.Column(db.Integer, nullable=True)
    Fator_Cotacao = db.Column(db.Text, nullable=True)
    Criterio_Determinacao_Preco_Emissao = db.Column(db.Text, nullable=True)
    Preco_Emissao = db.Column(db.Numeric(24, 8), nullable=True)
    Subscricao_Capital_Anterior = db.Column(db.Numeric(24, 8), nullable=True)
    Valor_Total_Emissao = db.Column(db.Numeric(18, 2), nullable=True)
    Quantidade_Acoes_Ordinarias = db.Column(db.Numeric(18, 0), nullable=True)
    Quantidade_Acoes_Preferenciais = db.Column(db.Numeric(18, 0), nullable=True)
    Orgao_Deliberacao_Aumento = db.Column(db.Text, nullable=True)
    Tipo_Subscricao = db.Column(db.Text, nullable=True)
    Data_Deliberacao = db.Column(db.Date, nullable=True)
    Forma_Integralizacao = db.Column(db.Text, nullable=True)
    ID_Capital_Social_Aumento = db.Column(db.Integer, nullable=True)
    Quantidade_Total_Acoes = db.Column(db.Numeric(18, 0), nullable=True)