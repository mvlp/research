from src.infra.Database.extensions import db

class fre_plano_recompra_classe_acao(db.Model):
    __tablename__ = "fre_plano_recompra_classe_acao"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    arquivo_origem = db.Column(db.Text, nullable=True)
    tipo_csv = db.Column(db.Text, nullable=True)

    CNPJ_Companhia = db.Column(db.Text, nullable=True)
    Data_Referencia = db.Column(db.Date, nullable=True)
    ID_Documento = db.Column(db.Integer, nullable=True)
    Nome_Companhia = db.Column(db.Text, nullable=True)
    Versao = db.Column(db.Integer, nullable=True)
    Quantidade_Prevista = db.Column(db.BigInteger, nullable=True)
    Especie_Acao = db.Column(db.Text, nullable=True)
    Quantidade_Adquirida = db.Column(db.BigInteger, nullable=True)
    Valor_Preco_Medio = db.Column(db.Numeric(18, 2), nullable=True)
    Escala_Cotacao = db.Column(db.Text, nullable=True)
    Percentual_Previsto = db.Column(db.Float, nullable=True)
    Tipo_Classe_Acao_Preferencial = db.Column(db.Text, nullable=True)
    Percentual_Adquirido = db.Column(db.Numeric(18, 6), nullable=True)
    ID_Plano_Recompra = db.Column(db.Integer, nullable=True)