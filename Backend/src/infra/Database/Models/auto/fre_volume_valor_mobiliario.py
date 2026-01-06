from src.infra.Database.extensions import db

class fre_volume_valor_mobiliario(db.Model):
    __tablename__ = "fre_volume_valor_mobiliario"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    arquivo_origem = db.Column(db.Text, nullable=True)
    tipo_csv = db.Column(db.Text, nullable=True)

    Classe_Acao_Preferencial = db.Column(db.Text, nullable=True)
    CNPJ_Companhia = db.Column(db.Text, nullable=True)
    Data_Fim_Exercicio_Social = db.Column(db.Date, nullable=True)
    Data_Inicio_Exercicio_Social = db.Column(db.Date, nullable=True)
    Data_Referencia = db.Column(db.Date, nullable=True)
    ID_Documento = db.Column(db.Integer, nullable=True)
    Nome_Companhia = db.Column(db.Text, nullable=True)
    Valor_Mobiliario = db.Column(db.Text, nullable=True)
    Versao = db.Column(db.Integer, nullable=True)
    Valor_Maior_Cotacao = db.Column(db.Numeric(18, 2), nullable=True)
    Especie_Acao = db.Column(db.Text, nullable=True)
    Valor_Volume_Negociado = db.Column(db.Numeric(18, 2), nullable=True)
    Valor_Menor_Cotacao = db.Column(db.Numeric(18, 2), nullable=True)
    Escala_Cotacao = db.Column(db.Text, nullable=True)
    Entidade_Administradora_Mercado = db.Column(db.Text, nullable=True)
    Mercado_Valor_Mobiliario = db.Column(db.Text, nullable=True)
    Valor_Cotacao_Media = db.Column(db.Numeric(18, 2), nullable=True)
    Descricao_Outro_Valor_Mobiliario = db.Column(db.Text, nullable=True)
    Data_Fim_Trimestre = db.Column(db.Date, nullable=True)