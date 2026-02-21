from flask import Flask
from sqlalchemy import text
from src.infra.Database.extensions import db
from flask_cors import CORS


from src.infra.Database.Models.ajustes_auto.fre_obrigacao import fre_obrigacao

from src.infra.Database.Models.Indice import Indice
from src.infra.Database.Models.Dimensao import Dimensao
from src.infra.Database.Models.pergunta import Pergunta
from src.infra.Database.Models.pergunta_dimensao import Pergunta_Dimensao
from src.infra.Database.Models.Importacao import Importacao
from src.infra.Database.Models.cotacao_b3 import CotacaoB3
from src.infra.Database.Models.stock_dividends_b3 import Stock_dividends_b3
from src.infra.Database.Models.approved_cash_dividends_b3 import Approved_cash_dividends_b3

from src.infra.Database.Models.auto.cgvn_praticas import cgvn_praticas
from src.infra.Database.Models.auto.cgvn_principal import cgvn_principal
from src.infra.Database.Models.auto.cia_local_faixa_etaria import cia_local_faixa_etaria
from src.infra.Database.Models.auto.dfp_BPA import dfp_BPA
from src.infra.Database.Models.auto.dfp_BPP import dfp_BPP
from src.infra.Database.Models.auto.dfp_composicao_capital import dfp_composicao_capital
from src.infra.Database.Models.auto.dfp_DFC_MD import dfp_DFC_MD
from src.infra.Database.Models.auto.dfp_DFC_MI import dfp_DFC_MI
from src.infra.Database.Models.auto.dfp_DMPL import dfp_DMPL
from src.infra.Database.Models.auto.dfp_DRA import dfp_DRA
from src.infra.Database.Models.auto.dfp_DRE import dfp_DRE
from src.infra.Database.Models.auto.dfp_DVA import dfp_DVA
from src.infra.Database.Models.auto.dfp_parecer import dfp_parecer
from src.infra.Database.Models.auto.dfp_principal import dfp_principal
from src.infra.Database.Models.auto.fca_auditor import fca_auditor
from src.infra.Database.Models.auto.fca_canal_divulgacao import fca_canal_divulgacao
from src.infra.Database.Models.auto.fca_departamento_acionistas import fca_departamento_acionistas
from src.infra.Database.Models.auto.fca_dri import fca_dri
from src.infra.Database.Models.auto.fca_endereco import fca_endereco
from src.infra.Database.Models.auto.fca_escriturador import fca_escriturador
from src.infra.Database.Models.auto.fca_geral import fca_geral
from src.infra.Database.Models.auto.fca_pais_estrangeiro_negociacao import fca_pais_estrangeiro_negociacao
from src.infra.Database.Models.auto.fca_principal import fca_principal
from src.infra.Database.Models.auto.fca_valor_mobiliario import fca_valor_mobiliario
from src.infra.Database.Models.auto.fre_acao_entregue import fre_acao_entregue
from src.infra.Database.Models.auto.fre_administrador_declaracao_genero import fre_administrador_declaracao_genero
from src.infra.Database.Models.auto.fre_administrador_declaracao_raca import fre_administrador_declaracao_raca
from src.infra.Database.Models.auto.fre_administrador_membro_conselho_fiscal import fre_administrador_membro_conselho_fiscal
from src.infra.Database.Models.auto.fre_ativo_imobilizado import fre_ativo_imobilizado
from src.infra.Database.Models.auto.fre_ativo_intangivel import fre_ativo_intangivel
from src.infra.Database.Models.auto.fre_auditor_responsavel import fre_auditor_responsavel
from src.infra.Database.Models.auto.fre_auditor import fre_auditor
from src.infra.Database.Models.auto.fre_capital_social_aumento_classe_acao import fre_capital_social_aumento_classe_acao
from src.infra.Database.Models.auto.fre_capital_social_aumento import fre_capital_social_aumento
from src.infra.Database.Models.auto.fre_capital_social_classe_acao import fre_capital_social_classe_acao
from src.infra.Database.Models.auto.fre_capital_social_desdobramento_classe_acao import fre_capital_social_desdobramento_classe_acao
from src.infra.Database.Models.auto.fre_capital_social_desdobramento import fre_capital_social_desdobramento
from src.infra.Database.Models.auto.fre_capital_social_reducao_classe_acao import fre_capital_social_reducao_classe_acao
from src.infra.Database.Models.auto.fre_capital_social_reducao import fre_capital_social_reducao
from src.infra.Database.Models.auto.fre_capital_social_titulo_conversivel import fre_capital_social_titulo_conversivel
from src.infra.Database.Models.auto.fre_capital_social import fre_capital_social
from src.infra.Database.Models.auto.fre_direito_acao import fre_direito_acao
from src.infra.Database.Models.auto.fre_distribuicao_capital_classe_acao import fre_distribuicao_capital_classe_acao
from src.infra.Database.Models.auto.fre_distribuicao_capital import fre_distribuicao_capital
from src.infra.Database.Models.auto.fre_empregado_declaracao_genero import fre_empregado_declaracao_genero
from src.infra.Database.Models.auto.fre_empregado_declaracao_raca import fre_empregado_declaracao_raca
from src.infra.Database.Models.auto.fre_grupo_economico_reestruturacao import fre_grupo_economico_reestruturacao
from src.infra.Database.Models.auto.fre_historico_emissor import fre_historico_emissor
from src.infra.Database.Models.auto.fre_membro_comite import fre_membro_comite
from src.infra.Database.Models.auto.fre_mercado_estrangeiro import fre_mercado_estrangeiro
from src.infra.Database.Models.auto.fre_outro_valor_mobiliario import fre_outro_valor_mobiliario
from src.infra.Database.Models.auto.fre_participacao_sociedade_valorizacao_acao import fre_participacao_sociedade_valorizacao_acao
from src.infra.Database.Models.auto.fre_participacao_sociedade import fre_participacao_sociedade
from src.infra.Database.Models.auto.fre_plano_recompra_classe_acao import fre_plano_recompra_classe_acao
from src.infra.Database.Models.auto.fre_plano_recompra import fre_plano_recompra
from src.infra.Database.Models.auto.fre_politica_negociacao_cargo import fre_politica_negociacao_cargo
from src.infra.Database.Models.auto.fre_politica_negociacao import fre_politica_negociacao
from src.infra.Database.Models.auto.fre_posicao_acionaria_classe_acao import fre_posicao_acionaria_classe_acao
from src.infra.Database.Models.auto.fre_posicao_acionaria import fre_posicao_acionaria
from src.infra.Database.Models.auto.fre_principal import fre_principal
from src.infra.Database.Models.auto.fre_relacao_familiar import fre_relacao_familiar
from src.infra.Database.Models.auto.fre_relacao_subordinacao import fre_relacao_subordinacao
from src.infra.Database.Models.auto.fre_remuneracao_acao import fre_remuneracao_acao
from src.infra.Database.Models.auto.fre_remuneracao_maxima_minima_media import fre_remuneracao_maxima_minima_media
from src.infra.Database.Models.auto.fre_remuneracao_total_orgao import fre_remuneracao_total_orgao
from src.infra.Database.Models.auto.fre_remuneracao_variavel import fre_remuneracao_variavel
from src.infra.Database.Models.auto.fre_responsavel import fre_responsavel
from src.infra.Database.Models.auto.fre_titular_valor_mobiliario import fre_titular_valor_mobiliario
from src.infra.Database.Models.auto.fre_titulo_exterior import fre_titulo_exterior
from src.infra.Database.Models.auto.fre_transacao_parte_relacionada import fre_transacao_parte_relacionada
from src.infra.Database.Models.auto.fre_valor_mobiliario_tesouraria_movimentacao import fre_valor_mobiliario_tesouraria_movimentacao
from src.infra.Database.Models.auto.fre_valor_mobiliario_tesouraria_ultimo_exercicio import fre_valor_mobiliario_tesouraria_ultimo_exercicio
from src.infra.Database.Models.auto.fre_volume_valor_mobiliario import fre_volume_valor_mobiliario
from src.infra.Database.Models.auto.ipe_principal import ipe_principal
from src.infra.Database.Models.auto.itr_BPA import itr_BPA
from src.infra.Database.Models.auto.itr_BPP import itr_BPP
from src.infra.Database.Models.auto.itr_composicao_capital import itr_composicao_capital
from src.infra.Database.Models.auto.itr_DFC_MD import itr_DFC_MD
from src.infra.Database.Models.auto.itr_DFC_MI import itr_DFC_MI
from src.infra.Database.Models.auto.itr_DMPL import itr_DMPL
from src.infra.Database.Models.auto.itr_DRA import itr_DRA
from src.infra.Database.Models.auto.itr_DRE import itr_DRE
from src.infra.Database.Models.auto.itr_DVA import itr_DVA
from src.infra.Database.Models.auto.itr_parecer import itr_parecer
from src.infra.Database.Models.auto.itr_principal import itr_principal
from src.infra.Database.Models.auto.vlmo_con import vlmo_con
from src.infra.Database.Models.auto.vlmo_principal import vlmo_principal


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://guilhermedesouzafornaciari:Ga05112002@localhost:5432/research"
db.init_app(app)
CORS(app)
with app.app_context():
    from src.infra.controller.Governanca_controller import Governanca_controller
    from src.infra.controller.Dimensao_controller import Dimensao_controller
    from src.infra.controller.Pergunta_controller import Pergunta_controller
    from src.infra.controller.Indice_controller import Indice_controller
    from src.infra.controller.CotacaoB3Controller import Cotacao_b3_controller

controllers = []
controllers.append(Governanca_controller())
controllers.append(Dimensao_controller())
controllers.append(Pergunta_controller())
controllers.append(Indice_controller())
controllers.append(Cotacao_b3_controller())

for controller in controllers:
    app.register_blueprint(controller.blueprint, url_prefix= "/" + controller.name)

print(app.url_map)

if __name__ == '__main__':
    with app.app_context():
      db.create_all()
      print("Database is reachable and tables can be created.")
      try:
          db.session.execute(text('SELECT 1'))
          print("Database connection successful!")
      except Exception as e:
          print("Database connection failed:", e)
    app.run(debug=True)
