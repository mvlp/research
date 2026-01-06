from src.infra.Database.extensions import db

class fca_endereco(db.Model):
    __tablename__ = "fca_endereco"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    arquivo_origem = db.Column(db.Text, nullable=True)
    tipo_csv = db.Column(db.Text, nullable=True)

    Bairro = db.Column(db.Text, nullable=True)
    Caixa_Postal = db.Column(db.Text, nullable=True)
    CEP = db.Column(db.Text, nullable=True)
    Cidade = db.Column(db.Text, nullable=True)
    CNPJ_Companhia = db.Column(db.Text, nullable=True)
    Complemento = db.Column(db.Text, nullable=True)
    Data_Referencia = db.Column(db.Date, nullable=True)
    DDD_Fax = db.Column(db.Text, nullable=True)
    DDD_Telefone = db.Column(db.Text, nullable=True)
    DDI_Fax = db.Column(db.Text, nullable=True)
    DDI_Telefone = db.Column(db.Text, nullable=True)
    Email = db.Column(db.Text, nullable=True)
    Fax = db.Column(db.Text, nullable=True)
    ID_Documento = db.Column(db.Integer, nullable=True)
    Logradouro = db.Column(db.Text, nullable=True)
    Nome_Empresarial = db.Column(db.Text, nullable=True)
    Pais = db.Column(db.Text, nullable=True)
    Sigla_UF = db.Column(db.Text, nullable=True)
    Telefone = db.Column(db.Text, nullable=True)
    Tipo_Endereco = db.Column(db.Text, nullable=True)
    Versao = db.Column(db.Integer, nullable=True)