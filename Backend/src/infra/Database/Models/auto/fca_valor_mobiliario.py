from src.infra.Database.extensions import db

class fca_valor_mobiliario(db.Model):
    __tablename__ = "fca_valor_mobiliario"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    arquivo_origem = db.Column(db.Text, nullable=True)
    tipo_csv = db.Column(db.Text, nullable=True)

    Classe_Acao_Preferencial = db.Column(db.Text, nullable=True)
    CNPJ_Companhia = db.Column(db.Text, nullable=True)
    Codigo_Negociacao = db.Column(db.Text, nullable=True)
    Composicao_BDR_Unit = db.Column(db.Text, nullable=True)
    Data_Fim_Listagem = db.Column(db.Date, nullable=True)
    Data_Fim_Negociacao = db.Column(db.Date, nullable=True)
    Data_Inicio_Listagem = db.Column(db.Date, nullable=True)
    Data_Inicio_Negociacao = db.Column(db.Date, nullable=True)
    Data_Referencia = db.Column(db.Date, nullable=True)
    Entidade_Administradora = db.Column(db.Text, nullable=True)
    ID_Documento = db.Column(db.Integer, nullable=True)
    Mercado = db.Column(db.Text, nullable=True)
    Nome_Empresarial = db.Column(db.Text, nullable=True)
    Segmento = db.Column(db.Text, nullable=True)
    Sigla_Classe_Acao_Preferencial = db.Column(db.Text, nullable=True)
    Sigla_Entidade_Administradora = db.Column(db.Text, nullable=True)
    Valor_Mobiliario = db.Column(db.Text, nullable=True)
    Versao = db.Column(db.Integer, nullable=True)