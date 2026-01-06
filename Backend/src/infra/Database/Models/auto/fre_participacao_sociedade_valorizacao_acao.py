from src.infra.Database.extensions import db

class fre_participacao_sociedade_valorizacao_acao(db.Model):
    __tablename__ = "fre_participacao_sociedade_valorizacao_acao"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    arquivo_origem = db.Column(db.Text, nullable=True)
    tipo_csv = db.Column(db.Text, nullable=True)

    CNPJ_Companhia = db.Column(db.Text, nullable=True)
    Data_Referencia = db.Column(db.Date, nullable=True)
    ID_Documento = db.Column(db.Integer, nullable=True)
    Nome_Companhia = db.Column(db.Text, nullable=True)
    Versao = db.Column(db.Integer, nullable=True)
    Data_Encerramento = db.Column(db.Date, nullable=True)
    Variacao_Percentual_Valor_Mercado = db.Column(db.Numeric(24, 8), nullable=True)
    Variacao_Percentual_Valor_Contabil = db.Column(db.Numeric(24, 8), nullable=True)
    Valor_Montante_Dividendos_Recebidos = db.Column(db.Numeric(18, 2), nullable=True)
    ID_Sociedade = db.Column(db.Integer, nullable=True)