from src.infra.Database.extensions import db

class fre_direito_acao(db.Model):
    __tablename__ = "fre_direito_acao"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    arquivo_origem = db.Column(db.Text, nullable=True)
    tipo_csv = db.Column(db.Text, nullable=True)

    Classe_Acao_Preferencial = db.Column(db.Text, nullable=True)
    CNPJ_Companhia = db.Column(db.Text, nullable=True)
    Data_Referencia = db.Column(db.Date, nullable=True)
    ID_Documento = db.Column(db.Integer, nullable=True)
    Nome_Companhia = db.Column(db.Text, nullable=True)
    Versao = db.Column(db.Integer, nullable=True)
    Condicao_Alteracao_Direitos = db.Column(db.Text, nullable=True)
    Direito_Voto = db.Column(db.Text, nullable=True)
    Especie_Acao = db.Column(db.Text, nullable=True)
    Descricao_Voto_Restrito = db.Column(db.Text, nullable=True)
    Descricao_Restricao_Circulacao = db.Column(db.Text, nullable=True)
    Condicao_Conversibilidade_Efeito_Capital_Social = db.Column(db.Text, nullable=True)
    Resgatavel = db.Column(db.Text, nullable=True)
    Caracteristicas_Reembolso_Capital = db.Column(db.Text, nullable=True)
    Percentual_Tag_Along = db.Column(db.Numeric(18, 6), nullable=True)
    Conversibilidade = db.Column(db.Text, nullable=True)
    Restricao_Circulacao = db.Column(db.Text, nullable=True)
    Direito_Dividendo = db.Column(db.Text, nullable=True)
    Direito_Reembolso_Capital = db.Column(db.Text, nullable=True)
    Hipotese_Resgate_Formula_Calculo = db.Column(db.Text, nullable=True)
    Outras_Caracteristicas_Relevantes = db.Column(db.Text, nullable=True)