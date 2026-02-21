from src.infra.Database.extensions import db

class fre_auditor(db.Model):
    __tablename__ = "fre_auditor"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    arquivo_origem = db.Column(db.Text, nullable=True)
    tipo_csv = db.Column(db.Text, nullable=True)

    Auditor = db.Column(db.Text, nullable=True)
    CNPJ_Auditor = db.Column(db.Text, nullable=True)
    CNPJ_Companhia = db.Column(db.Text, nullable=True)
    Codigo_CVM_Auditor = db.Column(db.Text, nullable=True)
    Data_Referencia = db.Column(db.Date, nullable=True)
    ID_Documento = db.Column(db.Integer, nullable=True)
    Nome_Companhia = db.Column(db.Text, nullable=True)
    Versao = db.Column(db.Integer, nullable=True)
    Justificativa_Substituicao = db.Column(db.Text, nullable=True)
    Servico_Contratado = db.Column(db.Text, nullable=True)
    Remuneracao_Auditor = db.Column(db.Text, nullable=True)
    Tipo_Origem_Auditor = db.Column(db.Text, nullable=True)
    CPF_Auditor = db.Column(db.Text, nullable=True)
    Data_Inicio_Prestacao_Servico = db.Column(db.Date, nullable=True)
    Data_Fim_Contratacao = db.Column(db.Date, nullable=True)
    Razao_Apresentada = db.Column(db.Text, nullable=True)
    ID_Auditor = db.Column(db.Integer, nullable=True)
    Data_Inicio_Contratacao = db.Column(db.Date, nullable=True)