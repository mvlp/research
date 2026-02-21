from src.infra.Database.extensions import db

class fre_outro_valor_mobiliario(db.Model):
    __tablename__ = "fre_outro_valor_mobiliario"

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
    Caracteristicas_Valores_Mobiliarios_Divida = db.Column(db.Text, nullable=True)
    Descricao_Restricao_Circulacao = db.Column(db.Text, nullable=True)
    Condicao_Conversibilidade_Efeito_Capital_Social = db.Column(db.Text, nullable=True)
    Resgatavel = db.Column(db.Text, nullable=True)
    Quantidade_Investidor_Institucional = db.Column(db.Numeric(18, 0), nullable=True)
    Conversibilidade = db.Column(db.Text, nullable=True)
    Restricao_Circulacao = db.Column(db.Text, nullable=True)
    Valor = db.Column(db.Numeric(18, 2), nullable=True)
    Saldo_Devedor = db.Column(db.Numeric(18, 2), nullable=True)
    Quantidade_Pessoa_Fisica = db.Column(db.Numeric(18, 0), nullable=True)
    Quantidade_Pessoa_Juridica = db.Column(db.Numeric(18, 0), nullable=True)
    Quantidade = db.Column(db.Numeric(18, 0), nullable=True)
    Hipotese_Resgate_Formula_Calculo = db.Column(db.Text, nullable=True)
    Identificacao_Valor_Mobiliario = db.Column(db.Text, nullable=True)
    Outras_Caracteristicas_Relevantes = db.Column(db.Text, nullable=True)