from src.infra.Database.extensions import db

class fre_relacao_subordinacao(db.Model):
    __tablename__ = "fre_relacao_subordinacao"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    arquivo_origem = db.Column(db.Text, nullable=True)
    tipo_csv = db.Column(db.Text, nullable=True)

    Cargo_Administrador = db.Column(db.Text, nullable=True)
    Cargo_Pessoa_Relacionada = db.Column(db.Text, nullable=True)
    Categoria_Pessoa_Relacionada = db.Column(db.Text, nullable=True)
    CNPJ_Companhia = db.Column(db.Text, nullable=True)
    CPF_Administrador = db.Column(db.Text, nullable=True)
    Data_Fim_Exercicio_Social = db.Column(db.Date, nullable=True)
    Data_Inicio_Exercicio_Social = db.Column(db.Date, nullable=True)
    Data_Referencia = db.Column(db.Date, nullable=True)
    Documento_Pessoa_Relacionada = db.Column(db.Text, nullable=True)
    ID_Documento = db.Column(db.Integer, nullable=True)
    Nome_Administrador = db.Column(db.Text, nullable=True)
    Nome_Companhia = db.Column(db.Text, nullable=True)
    Nome_Pessoa_Relacionada = db.Column(db.Text, nullable=True)
    Observacao = db.Column(db.Text, nullable=True)
    Tipo_Pessoa_Relacionada = db.Column(db.Text, nullable=True)
    Tipo_Relacao = db.Column(db.Text, nullable=True)
    Versao = db.Column(db.Integer, nullable=True)