from src.infra.Database.extensions import db

class fre_remuneracao_acao(db.Model):
    __tablename__ = "fre_remuneracao_acao"

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
    Preco_Medio_Ponderado_Opcoes_Perdidas = db.Column(db.Numeric(18, 2), nullable=True)
    Diluicao_Potencial = db.Column(db.Numeric(18, 6), nullable=True)
    Quantidade_Membros_Remunerados = db.Column(db.Numeric(18, 2), nullable=True)
    Preco_Medio_Ponderado_Opcoes_Exercidas = db.Column(db.Numeric(18, 2), nullable=True)
    Preco_Medio_Ponderado_Opcoes_Em_Aberto = db.Column(db.Numeric(18, 2), nullable=True)
    Quantidade_Total_Membros = db.Column(db.Numeric(18, 2), nullable=True)