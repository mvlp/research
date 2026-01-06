from src.infra.Database.extensions import db

class fre_administrador_membro_conselho_fiscal(db.Model):
    __tablename__ = "fre_administrador_membro_conselho_fiscal"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    arquivo_origem = db.Column(db.Text, nullable=True)
    tipo_csv = db.Column(db.Text, nullable=True)

    Cargo_Eletivo_Ocupado = db.Column(db.Text, nullable=True)
    CNPJ_Companhia = db.Column(db.Text, nullable=True)
    Complemento_Cargo_Eletivo_Ocupado = db.Column(db.Text, nullable=True)
    CPF = db.Column(db.Text, nullable=True)
    Data_Eleicao = db.Column(db.Date, nullable=True)
    Data_Nascimento = db.Column(db.Date, nullable=True)
    Data_Posse = db.Column(db.Date, nullable=True)
    Data_Referencia = db.Column(db.Date, nullable=True)
    Eleito_Controlador = db.Column(db.Text, nullable=True)
    Experiencia_Profissional = db.Column(db.Text, nullable=True)
    ID_Documento = db.Column(db.Integer, nullable=True)
    Nome = db.Column(db.Text, nullable=True)
    Nome_Companhia = db.Column(db.Text, nullable=True)
    Numero_Mandatos_Consecutivos = db.Column(db.Integer, nullable=True)
    Orgao_Administracao = db.Column(db.Text, nullable=True)
    Outro_Cargo_Funcao = db.Column(db.Text, nullable=True)
    Percentual_Participacao_Reunioes = db.Column(db.Numeric(7, 2), nullable=True)
    Prazo_Mandato = db.Column(db.Text, nullable=True)
    Profissao = db.Column(db.Text, nullable=True)
    Versao = db.Column(db.Integer, nullable=True)
    Data_Inicio_Primeiro_Mandato = db.Column(db.Date, nullable=True)