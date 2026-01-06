from src.infra.Database.extensions import db

class fre_remuneracao_maxima_minima_media(db.Model):
    __tablename__ = "fre_remuneracao_maxima_minima_media"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    arquivo_origem = db.Column(db.Text, nullable=True)
    tipo_csv = db.Column(db.Text, nullable=True)

    CNPJ_Companhia = db.Column(db.Text, nullable=True)
    Data_Fim_Exercicio_Social = db.Column(db.Date, nullable=True)
    Data_Inicio_Exercicio_Social = db.Column(db.Date, nullable=True)
    Data_Referencia = db.Column(db.Date, nullable=True)
    ID_Documento = db.Column(db.Integer, nullable=True)
    Nome_Companhia = db.Column(db.Text, nullable=True)
    Numero_Membros = db.Column(db.Numeric(18, 2), nullable=True)
    Numero_Membros_Remunerados = db.Column(db.Numeric(18, 2), nullable=True)
    Observacao = db.Column(db.Text, nullable=True)
    Orgao_Administracao = db.Column(db.Text, nullable=True)
    Valor_Maior_Remuneracao = db.Column(db.Numeric(18, 2), nullable=True)
    Valor_Medio_Remuneracao = db.Column(db.Numeric(18, 2), nullable=True)
    Valor_Menor_Remuneracao = db.Column(db.Numeric(18, 2), nullable=True)
    Versao = db.Column(db.Integer, nullable=True)