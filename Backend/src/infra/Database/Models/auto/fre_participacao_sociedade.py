from src.infra.Database.extensions import db

class fre_participacao_sociedade(db.Model):
    __tablename__ = "fre_participacao_sociedade"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    arquivo_origem = db.Column(db.Text, nullable=True)
    tipo_csv = db.Column(db.Text, nullable=True)

    CNPJ = db.Column(db.Text, nullable=True)
    CNPJ_Companhia = db.Column(db.Text, nullable=True)
    Codigo_CVM = db.Column(db.Text, nullable=True)
    Data_Referencia = db.Column(db.Date, nullable=True)
    ID_Documento = db.Column(db.Integer, nullable=True)
    Nome_Companhia = db.Column(db.Text, nullable=True)
    Versao = db.Column(db.Integer, nullable=True)
    Data_Valor_Contabil = db.Column(db.Date, nullable=True)
    Data_Valor_Mercado = db.Column(db.Date, nullable=True)
    Valor_Mercado = db.Column(db.Numeric(18, 2), nullable=True)
    Tipo_Sociedade = db.Column(db.Text, nullable=True)
    UF_Sede = db.Column(db.Text, nullable=True)
    Razao_Aquisicao_Manutencao = db.Column(db.Text, nullable=True)
    Valor_Contabil = db.Column(db.Numeric(18, 2), nullable=True)
    Descricao_Atividades = db.Column(db.Text, nullable=True)
    Razao_Social = db.Column(db.Text, nullable=True)
    Participacao_Emissor = db.Column(db.Numeric(24, 8), nullable=True)
    Possui_Registro_CVM = db.Column(db.Text, nullable=True)
    Municipio_Sede = db.Column(db.Text, nullable=True)
    Pais_Sede = db.Column(db.Text, nullable=True)
    ID_Sociedade = db.Column(db.Integer, nullable=True)