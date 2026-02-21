from  src.infra.Database.extensions import db

class cgvn_praticas(db.Model):
    __tablename__ = "cgvn_praticas"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    arquivo_origem = db.Column(db.Text, nullable=True)

    CNPJ_Companhia = db.Column(db.Text, nullable=True)
    Data_Referencia = db.Column(db.Date, nullable=True)
    ID_Documento = db.Column(db.Integer, nullable=True)
    Nome_Empresarial = db.Column(db.Text, nullable=True)
    Versao = db.Column(db.Integer, nullable=True)
    ID_Item = db.Column(db.Text, nullable=True)
    Pratica_Recomendada = db.Column(db.Text, nullable=True)
    Pratica_Adotada = db.Column(db.Text, nullable=True)
    Capitulo = db.Column(db.Text, nullable=True)
    Principio = db.Column(db.Text, nullable=True)
    Explicacao = db.Column(db.Text, nullable=True)

    
    Data_Entrega = db.Column(db.Date, nullable=False)
    gc_factor = db.Column(db.String(100), nullable=False)
    gc_value = db.Column(db.Integer, nullable=False)

