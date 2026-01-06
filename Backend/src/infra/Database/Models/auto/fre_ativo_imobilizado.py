from src.infra.Database.extensions import db

class fre_ativo_imobilizado(db.Model):
    __tablename__ = "fre_ativo_imobilizado"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    arquivo_origem = db.Column(db.Text, nullable=True)
    tipo_csv = db.Column(db.Text, nullable=True)

    CNPJ_Companhia = db.Column(db.Text, nullable=True)
    Data_Referencia = db.Column(db.Date, nullable=True)
    ID_Documento = db.Column(db.Integer, nullable=True)
    Nome_Companhia = db.Column(db.Text, nullable=True)
    Pais = db.Column(db.Text, nullable=True)
    UF = db.Column(db.Text, nullable=True)
    Versao = db.Column(db.Integer, nullable=True)
    Descricao_Bem_Ativo = db.Column(db.Text, nullable=True)
    Tipo_Propriedade = db.Column(db.Text, nullable=True)
    Municipio = db.Column(db.Text, nullable=True)