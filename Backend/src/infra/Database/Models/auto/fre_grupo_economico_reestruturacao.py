from src.infra.Database.extensions import db

class fre_grupo_economico_reestruturacao(db.Model):
    __tablename__ = "fre_grupo_economico_reestruturacao"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    arquivo_origem = db.Column(db.Text, nullable=True)
    tipo_csv = db.Column(db.Text, nullable=True)

    CNPJ_Companhia = db.Column(db.Text, nullable=True)
    Data_Referencia = db.Column(db.Date, nullable=True)
    ID_Documento = db.Column(db.Integer, nullable=True)
    Nome_Companhia = db.Column(db.Text, nullable=True)
    Versao = db.Column(db.Integer, nullable=True)
    Data_Operacao = db.Column(db.Date, nullable=True)
    Descricao_Operacao = db.Column(db.Text, nullable=True)
    Evento_Societario = db.Column(db.Text, nullable=True)