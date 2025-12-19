from  src.infra.Database.extensions import db

class Governanca(db.Model):
    __tablename__ = "Governanca"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    
    CNPJ_Companhia = db.Column(db.String(100), nullable=False)
    Data_Referencia = db.Column(db.Date, nullable=False)
    Versao = db.Column(db.String(100), nullable=False)
    Nome_Empresarial = db.Column(db.String(100), nullable=False)
    ID_Documento = db.Column(db.String(100), nullable=False)
    ID_Item = db.Column(db.String(100), nullable=False)
    Capitulo = db.Column(db.String(100), nullable=False)
    Principio = db.Column(db.String(100), nullable=False)
    Pratica_Recomendada = db.Column(db.String(100), nullable=False)
    Pratica_Adotada = db.Column(db.String(100), nullable=False)
    Explicacao = db.Column(db.String(255), nullable=False)
    Data_Entrega = db.Column(db.Date, nullable=False)
    gc_factor = db.Column(db.String(100), nullable=False)
    gc_value = db.Column(db.Integer, nullable=False)

