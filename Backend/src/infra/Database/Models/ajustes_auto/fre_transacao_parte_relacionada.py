from src.infra.Database.extensions import db

class fre_transacao_parte_relacionada(db.Model):
    __tablename__ = "fre_transacao_parte_relacionada"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tipo_csv = db.Column(db.Text, nullable=True)
    arquivo_origem = db.Column(db.Text, nullable=True)

    CNPJ_Companhia = db.Column(db.Text, nullable=True)
    Data_Referencia = db.Column(db.Text, nullable=True)
    Data_Transacao = db.Column(db.Text, nullable=True)
    Documento_Parte_Relacionada = db.Column(db.Text, nullable=True)
    Duracao_Transacao = db.Column(db.Text, nullable=True)
    Emprestimo_Divida = db.Column(db.Text, nullable=True)
    Especificacao_Posicao_Contratual_Emissor = db.Column(db.Text, nullable=True)
    Garantia_Seguro = db.Column(db.Text, nullable=True)
    ID_Documento = db.Column(db.Integer, nullable=True)
    Montante_Envolvido = db.Column(db.Numeric(18, 2), nullable=True)
    Montante_Interesse_Parte_Relacionada = db.Column(db.Text, nullable=True)
    Natureza_Razao_Operacao = db.Column(db.Text, nullable=True)
    Nome_Companhia = db.Column(db.Text, nullable=True)
    Objeto_Contrato = db.Column(db.Text, nullable=True)
    Parte_Relacionada = db.Column(db.Text, nullable=True)
    Posicao_Contratual_Emissor = db.Column(db.Text, nullable=True)
    Relacao_Emissor = db.Column(db.Text, nullable=True)
    Rescisao = db.Column(db.Text, nullable=True)
    Saldo_Existente = db.Column(db.Text, nullable=True)
    Taxa_Juros = db.Column(db.Text, nullable=True) ##Precisa ser alterada pois há lugares em que se tem o valor: TMS (Taxa média selic), e é incompativel com o bd
    Tipo_Pessoa = db.Column(db.Text, nullable=True)
    Versao = db.Column(db.Integer, nullable=True)