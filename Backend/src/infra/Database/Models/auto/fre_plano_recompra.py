from src.infra.Database.extensions import db

class fre_plano_recompra(db.Model):
    __tablename__ = "fre_plano_recompra"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    arquivo_origem = db.Column(db.Text, nullable=True)
    tipo_csv = db.Column(db.Text, nullable=True)

    CNPJ_Companhia = db.Column(db.Text, nullable=True)
    Data_Referencia = db.Column(db.Date, nullable=True)
    ID_Documento = db.Column(db.Integer, nullable=True)
    Nome_Companhia = db.Column(db.Text, nullable=True)
    Versao = db.Column(db.Integer, nullable=True)
    Data_Fim_Recompra = db.Column(db.Date, nullable=True)
    Valor_Reserva_Disponivel_Recompra = db.Column(db.Numeric(18, 2), nullable=True)
    Data_Deliberacao = db.Column(db.Date, nullable=True)
    ID_Plano_Recompra = db.Column(db.Integer, nullable=True)
    Data_Inicio_Recompra = db.Column(db.Date, nullable=True)
    Outras_Caracteristicas_Importantes = db.Column(db.Text, nullable=True)