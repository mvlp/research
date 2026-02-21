from src.infra.Database.extensions import db

class fre_historico_emissor(db.Model):
    __tablename__ = "fre_historico_emissor"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    arquivo_origem = db.Column(db.Text, nullable=True)
    tipo_csv = db.Column(db.Text, nullable=True)

    CNPJ_Companhia = db.Column(db.Text, nullable=True)
    Data_Referencia = db.Column(db.Date, nullable=True)
    ID_Documento = db.Column(db.Integer, nullable=True)
    Nome_Companhia = db.Column(db.Text, nullable=True)
    Versao = db.Column(db.Integer, nullable=True)
    Data_Registro_Emissor = db.Column(db.Date, nullable=True)
    Prazo_Duracao_Emissor = db.Column(db.Date, nullable=True)
    Requisicao_Registro_Emissor = db.Column(db.Text, nullable=True)
    Data_Constituicao_Emissor = db.Column(db.Date, nullable=True)
    Pais_Constituicao_Emissor = db.Column(db.Text, nullable=True)
    Sigla_Pais_Constituicao_Emissor = db.Column(db.Text, nullable=True)
    Forma_Constituicao_Emissor = db.Column(db.Text, nullable=True)