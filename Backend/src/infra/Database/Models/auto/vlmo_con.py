from src.infra.Database.extensions import db

class vlmo_con(db.Model):
    __tablename__ = "vlmo_con"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    arquivo_origem = db.Column(db.Text, nullable=True)
    tipo_csv = db.Column(db.Text, nullable=True)

    CNPJ_Companhia = db.Column(db.Text, nullable=True)
    Data_Referencia = db.Column(db.Date, nullable=True)
    Nome_Companhia = db.Column(db.Text, nullable=True)
    Preco_Unitario = db.Column(db.Float, nullable=True)
    Tipo_Ativo = db.Column(db.Text, nullable=True)
    Versao = db.Column(db.Integer, nullable=True)
    Descricao_Movimentacao = db.Column(db.Text, nullable=True)
    Intermediario = db.Column(db.Text, nullable=True)
    Tipo_Cargo = db.Column(db.Text, nullable=True)
    Empresa = db.Column(db.Text, nullable=True)
    Data_Movimentacao = db.Column(db.Date, nullable=True)
    Tipo_Movimentacao = db.Column(db.Text, nullable=True)
    Quantidade = db.Column(db.BigInteger, nullable=True)
    Caracteristica_Valor_Mobiliario = db.Column(db.Text, nullable=True)
    Volume = db.Column(db.Float, nullable=True)
    Tipo_Empresa = db.Column(db.Text, nullable=True)
    Tipo_Operacao = db.Column(db.Text, nullable=True)