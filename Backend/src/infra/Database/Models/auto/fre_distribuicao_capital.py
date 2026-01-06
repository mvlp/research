from src.infra.Database.extensions import db

class fre_distribuicao_capital(db.Model):
    __tablename__ = "fre_distribuicao_capital"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    arquivo_origem = db.Column(db.Text, nullable=True)
    tipo_csv = db.Column(db.Text, nullable=True)

    CNPJ_Companhia = db.Column(db.Text, nullable=True)
    Data_Referencia = db.Column(db.Date, nullable=True)
    Data_Ultima_Assembleia = db.Column(db.Date, nullable=True)
    ID_Documento = db.Column(db.Integer, nullable=True)
    Nome_Companhia = db.Column(db.Text, nullable=True)
    Percentual_Acoes_Ordinarias_Circulacao = db.Column(db.Numeric(18, 6), nullable=True)
    Percentual_Acoes_Preferenciais_Circulacao = db.Column(db.Numeric(18, 6), nullable=True)
    Percentual_Total_Acoes_Circulacao = db.Column(db.Numeric(18, 6), nullable=True)
    Quantidade_Acionistas_Investidores_Institucionais = db.Column(db.Numeric(18, 0), nullable=True)
    Quantidade_Acionistas_PF = db.Column(db.Numeric(18, 0), nullable=True)
    Quantidade_Acionistas_PJ = db.Column(db.Numeric(18, 0), nullable=True)
    Quantidade_Acoes_Ordinarias_Circulacao = db.Column(db.Numeric(18, 0), nullable=True)
    Quantidade_Acoes_Preferenciais_Circulacao = db.Column(db.Numeric(18, 0), nullable=True)
    Quantidade_Total_Acoes_Circulacao = db.Column(db.Numeric(18, 0), nullable=True)
    Versao = db.Column(db.Integer, nullable=True)