from src.infra.Database.extensions import db

class fre_acao_entregue(db.Model):
    __tablename__ = "fre_acao_entregue"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    arquivo_origem = db.Column(db.Text, nullable=True)
    tipo_csv = db.Column(db.Text, nullable=True)

    CNPJ_Companhia = db.Column(db.Text, nullable=True)
    Data_Fim_Exercicio_Social = db.Column(db.Date, nullable=True)
    Data_Inicio_Exercicio_Social = db.Column(db.Date, nullable=True)
    Data_Referencia = db.Column(db.Date, nullable=True)
    ID_Documento = db.Column(db.Integer, nullable=True)
    Nome_Companhia = db.Column(db.Text, nullable=True)
    Orgao_Administracao = db.Column(db.Text, nullable=True)
    Versao = db.Column(db.Integer, nullable=True)
    Valor_Diferenca_Aquisicao_Mercado = db.Column(db.Numeric(18, 2), nullable=True)
    Preco_Medio_Ponderado_Aquisicao = db.Column(db.Numeric(18, 2), nullable=True)
    Preco_Medio_Ponderado_Mercado = db.Column(db.Numeric(18, 2), nullable=True)
    Quantidade_Acoes = db.Column(db.Integer, nullable=True)
    Quantidade_Membros_Remunerados = db.Column(db.Numeric(18, 2), nullable=True)
    Quantidade_Total_Membros = db.Column(db.Numeric(18, 2), nullable=True)