from src.infra.Database.extensions import db

class fre_valor_mobiliario_tesouraria_ultimo_exercicio(db.Model):
    __tablename__ = "fre_valor_mobiliario_tesouraria_ultimo_exercicio"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    arquivo_origem = db.Column(db.Text, nullable=True)
    tipo_csv = db.Column(db.Text, nullable=True)

    CNPJ_Companhia = db.Column(db.Text, nullable=True)
    Data_Referencia = db.Column(db.Date, nullable=True)
    ID_Documento = db.Column(db.Integer, nullable=True)
    Nome_Companhia = db.Column(db.Text, nullable=True)
    Valor_Mobiliario = db.Column(db.Text, nullable=True)
    Versao = db.Column(db.Integer, nullable=True)
    Especie_Acao = db.Column(db.Text, nullable=True)
    Valor_Preco_Medio = db.Column(db.Numeric(18, 2), nullable=True)
    Escala_Cotacao = db.Column(db.Text, nullable=True)
    Data_Aquisicao = db.Column(db.Date, nullable=True)
    Descricao_Valor_Mobiliario = db.Column(db.Text, nullable=True)
    Tipo_Classe_Acao_Preferencial = db.Column(db.Text, nullable=True)
    Percentual_Circulacao = db.Column(db.Numeric(18, 6), nullable=True)
    Quantidade_Valor_Mobiliario = db.Column(db.Numeric(18, 0), nullable=True)