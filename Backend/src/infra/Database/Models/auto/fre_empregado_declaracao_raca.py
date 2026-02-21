from src.infra.Database.extensions import db

class fre_empregado_declaracao_raca(db.Model):
    __tablename__ = "fre_empregado_declaracao_raca"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    arquivo_origem = db.Column(db.Text, nullable=True)
    tipo_csv = db.Column(db.Text, nullable=True)

    Classe = db.Column(db.Text, nullable=True)
    CNPJ_Companhia = db.Column(db.Text, nullable=True)
    Data_Referencia = db.Column(db.Date, nullable=True)
    ID_Documento = db.Column(db.Integer, nullable=True)
    Versao = db.Column(db.Integer, nullable=True)
    Quantidade_Preto = db.Column(db.Integer, nullable=True)
    Quantidade_Indigena = db.Column(db.Integer, nullable=True)
    Quantidade_Amarelo = db.Column(db.Integer, nullable=True)
    Quantidade_Pardo = db.Column(db.Integer, nullable=True)
    Quantidade_Sem_Resposta = db.Column(db.Integer, nullable=True)
    Quantidade_Branco = db.Column(db.Integer, nullable=True)
    Quantidade_Outros = db.Column(db.Integer, nullable=True)