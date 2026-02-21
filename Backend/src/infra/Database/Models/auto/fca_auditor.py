from src.infra.Database.extensions import db

class fca_auditor(db.Model):
    __tablename__ = "fca_auditor"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    arquivo_origem = db.Column(db.Text, nullable=True)
    tipo_csv = db.Column(db.Text, nullable=True)

    Auditor = db.Column(db.Text, nullable=True)
    CNPJ_Companhia = db.Column(db.Text, nullable=True)
    Codigo_CVM_Auditor = db.Column(db.Text, nullable=True)
    CPF_CNPJ_Auditor = db.Column(db.Text, nullable=True)
    CPF_Responsavel_Tecnico = db.Column(db.Text, nullable=True)
    Data_Fim_Atuacao_Auditor = db.Column(db.Date, nullable=True)
    Data_Fim_Atuacao_Responsavel_Tecnico = db.Column(db.Date, nullable=True)
    Data_Inicio_Atuacao_Auditor = db.Column(db.Date, nullable=True)
    Data_Inicio_Atuacao_Responsavel_Tecnico = db.Column(db.Date, nullable=True)
    Data_Referencia = db.Column(db.Date, nullable=True)
    ID_Documento = db.Column(db.Integer, nullable=True)
    Nome_Empresarial = db.Column(db.Text, nullable=True)
    Origem_Auditor = db.Column(db.Text, nullable=True)
    Responsavel_Tecnico = db.Column(db.Text, nullable=True)
    Versao = db.Column(db.Integer, nullable=True)