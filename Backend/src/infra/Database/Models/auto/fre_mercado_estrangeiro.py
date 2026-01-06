from src.infra.Database.extensions import db

class fre_mercado_estrangeiro(db.Model):
    __tablename__ = "fre_mercado_estrangeiro"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    arquivo_origem = db.Column(db.Text, nullable=True)
    tipo_csv = db.Column(db.Text, nullable=True)

    CNPJ_Companhia = db.Column(db.Text, nullable=True)
    Data_Emissao = db.Column(db.Date, nullable=True)
    Data_Inicio_Listagem = db.Column(db.Date, nullable=True)
    Data_Referencia = db.Column(db.Date, nullable=True)
    ID_Documento = db.Column(db.Integer, nullable=True)
    Mercado = db.Column(db.Text, nullable=True)
    Nome_Companhia = db.Column(db.Text, nullable=True)
    Valor_Mobiliario = db.Column(db.Text, nullable=True)
    Versao = db.Column(db.Integer, nullable=True)
    Descricao_Instituicao_Custodiante = db.Column(db.Text, nullable=True)
    Descricao_Banco_Depositario = db.Column(db.Text, nullable=True)
    Percentual = db.Column(db.Numeric(18, 6), nullable=True)
    Administradora = db.Column(db.Text, nullable=True)
    Pais_Negociacao = db.Column(db.Text, nullable=True)
    Descricao_Proporcao_Certificado = db.Column(db.Text, nullable=True)
    Identificacao_Valor_Mobiliario = db.Column(db.Text, nullable=True)
    Descricao_Segmento = db.Column(db.Text, nullable=True)