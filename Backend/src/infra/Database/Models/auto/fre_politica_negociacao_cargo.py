from src.infra.Database.extensions import db

class fre_politica_negociacao_cargo(db.Model):
    __tablename__ = "fre_politica_negociacao_cargo"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    arquivo_origem = db.Column(db.Text, nullable=True)
    tipo_csv = db.Column(db.Text, nullable=True)

    CNPJ_Companhia = db.Column(db.Text, nullable=True)
    Data_Referencia = db.Column(db.Date, nullable=True)
    ID_Documento = db.Column(db.Integer, nullable=True)
    Nome_Companhia = db.Column(db.Text, nullable=True)
    Versao = db.Column(db.Integer, nullable=True)
    ID_Politica = db.Column(db.Integer, nullable=True)
    Cargo_Pessoa_Vinculada = db.Column(db.Text, nullable=True)