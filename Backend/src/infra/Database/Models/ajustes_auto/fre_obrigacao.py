from src.infra.Database.extensions import db

class fre_obrigacao(db.Model):
    __tablename__ = "fre_obrigacao"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    arquivo_origem = db.Column(db.Text, nullable=True)

    CNPJ_Companhia = db.Column(db.Text, nullable=True)
    Data_Referencia = db.Column(db.Date, nullable=True)
    ID_Documento = db.Column(db.Integer, nullable=True)
    Nome_Companhia = db.Column(db.Text, nullable=True)
    Versao = db.Column(db.Integer, nullable=True)
    Data_Inicio_Exercicio_Social = db.Column(db.Date, nullable=True)
    Data_Fim_Exercicio_Social = db.Column(db.Date, nullable=True)
    Tipo_Obrigacao = db.Column(db.Text, nullable=True)
    Tipo_Garantia = db.Column(db.Text, nullable=True)
    Descricao_Outras_Garantias = db.Column(db.Text, nullable=True)
    Divida_Inferior_1_Ano = db.Column(db.Float, nullable=True)
    Divida_1a3Anos = db.Column(db.Float, nullable=True)
    Divida_3a5Anos = db.Column(db.Float, nullable=True)
    Divida_Superior_5Anos = db.Column(db.Float, nullable=True)
    Divida_Total = db.Column(db.Text, nullable=True)
    Observacao = db.Column(db.Text, nullable=True)