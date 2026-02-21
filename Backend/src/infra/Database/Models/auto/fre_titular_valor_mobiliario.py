from src.infra.Database.extensions import db

class fre_titular_valor_mobiliario(db.Model):
    __tablename__ = "fre_titular_valor_mobiliario"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    arquivo_origem = db.Column(db.Text, nullable=True)
    tipo_csv = db.Column(db.Text, nullable=True)

    CNPJ_Companhia = db.Column(db.Text, nullable=True)
    Data_Referencia = db.Column(db.Date, nullable=True)
    ID_Documento = db.Column(db.Integer, nullable=True)
    Nome_Companhia = db.Column(db.Text, nullable=True)
    Valor_Mobiliario = db.Column(db.Text, nullable=True)
    Versao = db.Column(db.Integer, nullable=True)
    Quantidade_Investidor = db.Column(db.Numeric(18, 0), nullable=True)
    Quantidade_Pessoa_Fisica = db.Column(db.Numeric(18, 0), nullable=True)
    Quantidade_Pessoa_Juridica = db.Column(db.Numeric(18, 0), nullable=True)