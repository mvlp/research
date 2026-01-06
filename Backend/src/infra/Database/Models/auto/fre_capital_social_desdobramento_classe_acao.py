from src.infra.Database.extensions import db

class fre_capital_social_desdobramento_classe_acao(db.Model):
    __tablename__ = "fre_capital_social_desdobramento_classe_acao"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    arquivo_origem = db.Column(db.Text, nullable=True)
    tipo_csv = db.Column(db.Text, nullable=True)

    CNPJ_Companhia = db.Column(db.Text, nullable=True)
    Data_Referencia = db.Column(db.Date, nullable=True)
    ID_Documento = db.Column(db.Integer, nullable=True)
    Nome_Companhia = db.Column(db.Text, nullable=True)
    Versao = db.Column(db.Integer, nullable=True)
    ID_Capital_Social_Desdobramento = db.Column(db.Integer, nullable=True)
    Quantidade_Acoes_Depois_Aprovacao = db.Column(db.Numeric(18, 0), nullable=True)
    Quantidade_Acoes_Antes_Aprovacao = db.Column(db.Numeric(18, 0), nullable=True)
    Tipo_Classe_Acao_Preferencial = db.Column(db.Text, nullable=True)