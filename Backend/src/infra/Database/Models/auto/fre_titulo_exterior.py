from src.infra.Database.extensions import db

class fre_titulo_exterior(db.Model):
    __tablename__ = "fre_titulo_exterior"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    arquivo_origem = db.Column(db.Text, nullable=True)
    tipo_csv = db.Column(db.Text, nullable=True)

    CNPJ_Companhia = db.Column(db.Text, nullable=True)
    Data_Emissao = db.Column(db.Date, nullable=True)
    Data_Referencia = db.Column(db.Date, nullable=True)
    Data_Vencimento = db.Column(db.Date, nullable=True)
    ID_Documento = db.Column(db.Integer, nullable=True)
    Nome_Companhia = db.Column(db.Text, nullable=True)
    Valor_Mobiliario = db.Column(db.Text, nullable=True)
    Versao = db.Column(db.Integer, nullable=True)
    Condicao_Alteracao_Direitos = db.Column(db.Text, nullable=True)
    Descricao_Restricao_Circulacao = db.Column(db.Text, nullable=True)
    Valor_Nominal = db.Column(db.Numeric(18, 2), nullable=True)
    Possibilidade_Resgate = db.Column(db.Text, nullable=True)
    Conversibilidade = db.Column(db.Text, nullable=True)
    Restricao_Circulacao = db.Column(db.Text, nullable=True)
    Condicao_Conversibilidade = db.Column(db.Text, nullable=True)
    Saldo_Devedor = db.Column(db.Numeric(18, 2), nullable=True)
    Quantidade = db.Column(db.BigInteger, nullable=True)
    Outras_Caracteristicas = db.Column(db.Text, nullable=True)
    Identificacao_Valor_Mobiliario = db.Column(db.Text, nullable=True)
    Hipotese_Calculo_Resgate = db.Column(db.Text, nullable=True)
    Caracteristicas_Divida = db.Column(db.Text, nullable=True)