from src.infra.Database.extensions import db

class fre_administrador_declaracao_genero(db.Model):
    __tablename__ = "fre_administrador_declaracao_genero"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    arquivo_origem = db.Column(db.Text, nullable=True)
    tipo_csv = db.Column(db.Text, nullable=True)

    CNPJ_Companhia = db.Column(db.Text, nullable=True)
    Data_Referencia = db.Column(db.Date, nullable=True)
    ID_Documento = db.Column(db.Integer, nullable=True)
    Nome_Companhia = db.Column(db.Text, nullable=True)
    Orgao_Administracao = db.Column(db.Text, nullable=True)
    Versao = db.Column(db.Integer, nullable=True)
    Quantidade_Nao_Binario = db.Column(db.Integer, nullable=True)
    Quantidade_Sem_Resposta = db.Column(db.Integer, nullable=True)
    Quantidade_Feminino = db.Column(db.Integer, nullable=True)
    Quantidade_Masculino = db.Column(db.Integer, nullable=True)
    Quantidade_Outros = db.Column(db.Integer, nullable=True)
    Nao_Aplicavel = db.Column(db.Text, nullable=True)