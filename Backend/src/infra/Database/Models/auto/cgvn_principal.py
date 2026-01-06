from src.infra.Database.extensions import db

class cgvn_principal(db.Model):
    __tablename__ = "cgvn_principal"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    arquivo_origem = db.Column(db.Text, nullable=True)
    tipo_csv = db.Column(db.Text, nullable=True)

    Categoria = db.Column(db.Text, nullable=True)
    CNPJ_Companhia = db.Column(db.Text, nullable=True)
    Codigo_CVM = db.Column(db.Text, nullable=True)
    Data_Entrega = db.Column(db.Date, nullable=True)
    Data_Fim_Exercicio_Social = db.Column(db.Date, nullable=True)
    Data_Inicio_Exercicio_Social = db.Column(db.Date, nullable=True)
    Data_Referencia = db.Column(db.Date, nullable=True)
    ID_Documento = db.Column(db.Integer, nullable=True)
    Link_Download = db.Column(db.Text, nullable=True)
    Nome_Empresarial = db.Column(db.Text, nullable=True)
    Versao = db.Column(db.Integer, nullable=True)
    Motivo_Reapresentacao = db.Column(db.Text, nullable=True)