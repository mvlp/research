from decimal import Decimal
from pathlib import Path
from types import SimpleNamespace
import pandas as pd
from sqlalchemy import create_engine
from main import app
from sqlalchemy.orm import Session
from sqlalchemy import Engine, select, text
from src.scripts.codigoPython.url_db import url_db
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent  # Isso dá "CodigoPython/"

with app.app_context():
    from src.services.Cotacao_b3_service import Cotacao_b3_service
    from src.infra.Database.Models.cotacao_b3_relativa import CotacaoB3Corrigida


class Gera_indices:
    def __init__(self,engine: Engine) -> None:
        self.engine = engine
    def preco_para_porcentagem(self, isin:str = "", codigo_neg:str = ""):
        service = Cotacao_b3_service()
        with Session(self.engine) as session:
            empresas = []
            if (isin != "" and codigo_neg != ""):
                session.query(CotacaoB3Corrigida).where(CotacaoB3Corrigida.isin == isin).delete()
                empresas = [SimpleNamespace(codigo_negociacao=codigo_neg)]
            else:
                session.query(CotacaoB3Corrigida).delete()
                empresas = session.execute(text("select distinct(codigo_negociacao)  from cotacao_b3 where data_pregao > '2000-01-01' and codigo_bdi = '2';")).mappings().all()
            session.commit()
            total = len(empresas)
            count_empresa = 1
            for empresa in empresas:
                codigo = empresa.codigo_negociacao
                print(f"{codigo}: {count_empresa}/{total} ")
                count_empresa+= 1
                dado = session.execute(text("select isin from cotacao_b3 where data_pregao > '2000-01-01' and codigo_negociacao = :code order by data_pregao desc limit 1;"),{"code":codigo}).mappings().all()
                dados_b3 = service.getCorrigido(dado[0].isin,codigo,"2026-06-06")
                for i in range(1,len(dados_b3)):
                    dado = dados_b3[i]
                    anterior = dados_b3[i-1]
                    corrigido = CotacaoB3Corrigida()
                    corrigido.tipo_registro = dado.tipo_registro 
                    corrigido.data_pregao = dado.data_pregao
                    corrigido.codigo_bdi = dado.codigo_bdi 
                    corrigido.codigo_negociacao = dado.codigo_negociacao 
                    corrigido.mercado = dado.mercado 
                    corrigido.nome_empresa = dado.nome_empresa 
                    corrigido.especificacao_papel = dado.especificacao_papel 
                    corrigido.prazo_termo = dado.prazo_termo
                    corrigido.moeda = dado.moeda
                    
                    if (dado.preco_abertura): corrigido.preco_abertura = dado.preco_abertura
                    if (dado.preco_maximo): corrigido.preco_maximo = dado.preco_maximo
                    if (dado.preco_minimo): corrigido.preco_minimo = dado.preco_minimo
                    if (dado.preco_medio): corrigido.preco_medio = dado.preco_medio
                    if (dado.preco_fechamento): corrigido.preco_fechamento = dado.preco_fechamento

                    if (dado.preco_abertura and anterior.preco_abertura): corrigido.preco_abertura_relativo = (dado.preco_abertura - anterior.preco_abertura) / anterior.preco_abertura
                    if (dado.preco_maximo and anterior.preco_maximo): corrigido.preco_maximo_relativo = (dado.preco_maximo - anterior.preco_maximo) / anterior.preco_maximo
                    if (dado.preco_minimo and anterior.preco_minimo): corrigido.preco_minimo_relativo = (dado.preco_minimo - anterior.preco_minimo) / anterior.preco_minimo
                    if (dado.preco_medio and anterior.preco_medio): corrigido.preco_medio_relativo = (dado.preco_medio - anterior.preco_medio) / anterior.preco_medio
                    if (dado.preco_fechamento and anterior.preco_fechamento): corrigido.preco_fechamento_relativo = (dado.preco_fechamento - anterior.preco_fechamento) / anterior.preco_fechamento
                    
                    corrigido.numero_negocios = dado.numero_negocios 
                    corrigido.quantidade_negociada = dado.quantidade_negociada 
                    corrigido.volume_financeiro = dado.volume_financeiro 
                    corrigido.preco_exercicio = dado.preco_exercicio 
                    corrigido.indicador_correcao = dado.indicador_correcao
                    corrigido.data_vencimento = dado.data_vencimento 
                    corrigido.fator_cotacao = dado.fator_cotacao
                    corrigido.preco_exercicio_pontos = dado.preco_exercicio_pontos 
                    corrigido.isin = dado.isin 
                    corrigido.distribuicao = dado.distribuicao
                    session.add(corrigido)
                session.commit()
    def calcular_retorno(
        self,
        painel: pd.DataFrame,
        coluna_preco: str = 'preco_fechamento',
        coluna_ativo: str = 'isin',
        coluna_tempo: str = 'trimestre',
    ) -> pd.DataFrame:
        painel = painel.sort_values([coluna_ativo, coluna_tempo]).copy()

        preco_anterior: pd.Series = painel.groupby(coluna_ativo)[coluna_preco].shift(1)

        painel['retorno'] = (
            (painel[coluna_preco] - preco_anterior) / preco_anterior
        )

        return painel
    def calcular_peso(
        self,
        painel: pd.DataFrame,
        coluna_valor: str = 'valor_total',
        coluna_tempo: str = 'trimestre',
        coluna_retorno: str = 'retorno',
    ) -> pd.DataFrame:
        painel = painel.copy()

        valor_total_periodo: pd.Series = painel.groupby(coluna_tempo)[coluna_valor].transform('sum')

        painel['peso'] = painel[coluna_valor] / valor_total_periodo
        painel['retorno_ponderado'] = painel[coluna_retorno] * painel['peso']

        return painel
    
    def fator_smb_nefin(self) -> pd.Series:
        dados = pd.read_sql("SELECT * FROM tamanho_empresa_b3", self.engine)
        dados['trimestre'] = pd.to_datetime(dados['trimestre']).dt.tz_localize(None)
        dados['ano'] = dados['trimestre'].dt.year
        dados['mes'] = dados['trimestre'].dt.month
        dados['valor_total'] = dados['qtd_acoes'] * dados['preco_fechamento']

        # DEBUG: ver quais meses existem
        print("Meses únicos na tabela:", sorted(dados['mes'].unique()))
        print("Amostra de trimestres:", dados['trimestre'].sort_values().unique()[:8])

        # Q4 no postgres date_trunc começa em outubro (mes=10)
        # Esse é o market cap de "dezembro t-1" para classificar o ano t
        market_cap_q4 = (
            dados[dados['mes'] == 10]
            .groupby(['isin', 'ano'])['valor_total']
            .last()
            .reset_index()
            .rename(columns={'valor_total': 'market_cap_ref', 'ano': 'ano_ref'})
        )

        print("\nAnos disponíveis para classificação:", sorted(market_cap_q4['ano_ref'].unique()))

        def classificar(grupo):
            grupo = grupo.copy()
            try:
                grupo['tercil'] = pd.qcut(
                    grupo['market_cap_ref'], 3, labels=[0, 1, 2], duplicates='drop'
                )
            except Exception:
                grupo['tercil'] = pd.NA
            return grupo

        market_cap_q4 = market_cap_q4.groupby('ano_ref', group_keys=False).apply(classificar)
        
        # ano_ref=2020 Q4 → classifica o ano 2021
        market_cap_q4['ano_carteira'] = market_cap_q4['ano_ref'] + 1

        dados = dados.merge(
            market_cap_q4[['isin', 'ano_carteira', 'tercil']],
            left_on=['isin', 'ano'],
            right_on=['isin', 'ano_carteira'],
            how='inner'
        )
        dados = dados.dropna(subset=['tercil'])
        dados = dados[dados['ano'] < 2026]

        dados = dados.sort_values(['isin', 'trimestre'])
        dados['retorno'] = dados.groupby('isin')['preco_fechamento'].pct_change()
                # Winsorize: corta retornos abaixo do percentil 1 e acima do percentil 99
        p1 = dados['retorno'].quantile(0.01)
        p99 = dados['retorno'].quantile(0.99)
        dados['retorno'] = dados['retorno'].clip(lower=p1, upper=p99)
        print(f"Winsorize: cortando retornos fora de [{p1:.3f}, {p99:.3f}]")
        dados = dados.dropna(subset=['retorno'])

        smb = (
            dados.groupby(['trimestre', 'tercil'])['retorno']
            .mean()
            .unstack('tercil')
        )
        smb_fator = smb[0] - smb[2]
        smb_fator.name = 'SMB'
        return smb_fator
    

def teste():
    dados = pd.read_sql("SELECT * FROM tamanho_empresa_b3", engine)
    dados['trimestre'] = pd.to_datetime(dados['trimestre']).dt.tz_localize(None)
    dados['ano'] = dados['trimestre'].dt.year
    dados['mes'] = dados['trimestre'].dt.month
    dados['valor_total'] = dados['qtd_acoes'] * dados['preco_fechamento']
    print("Trimestres únicos disponíveis em julho/2024:")
    print(dados[dados['trimestre'].dt.month == 7]['trimestre'].unique())

    market_cap_q4 = (
        dados[dados['mes'] == 10]
        .groupby(['isin', 'ano'])['valor_total']
        .last()
        .reset_index()
        .rename(columns={'valor_total': 'market_cap_ref', 'ano': 'ano_ref'})
    )

    def classificar(grupo):
        grupo = grupo.copy()
        try:
            grupo['tercil'] = pd.qcut(grupo['market_cap_ref'], 3, labels=[0,1,2], duplicates='drop')
        except Exception:
            grupo['tercil'] = pd.NA
        return grupo

    market_cap_q4 = market_cap_q4.groupby('ano_ref', group_keys=False).apply(classificar)
    market_cap_q4['ano_carteira'] = market_cap_q4['ano_ref'] + 1

    dados = dados.merge(
        market_cap_q4[['isin', 'ano_carteira', 'tercil']],
        left_on=['isin', 'ano'],
        right_on=['isin', 'ano_carteira'],
        how='inner'
    )
    dados = dados.sort_values(['isin', 'trimestre'])
    dados['retorno'] = dados.groupby('isin')['preco_fechamento'].pct_change()

    # Foco no 2024Q3 = trimestre 2024-07-01
    q3_2024 = dados[
        (dados['trimestre'].dt.year == 2024) & 
        (dados['trimestre'].dt.month == 7)
    ].dropna(subset=['retorno'])

    print("Linhas encontradas:", len(q3_2024))
    print("\n=== Top 10 retornos no 2024Q3 ===")
    print(q3_2024.nlargest(10, 'retorno')[['isin', 'codigo_negociacao', 'tercil', 'retorno', 'preco_fechamento', 'valor_total']])

    print("\n=== Retorno médio por tercil no 2024Q3 ===")
    print(q3_2024.groupby('tercil', observed=True)['retorno'].describe())
    print("\n=== Bottom 10 retornos no 2024Q3 ===")
    print(q3_2024.nsmallest(10, 'retorno')[['isin', 'codigo_negociacao', 'tercil', 'retorno', 'preco_fechamento', 'valor_total']])

    print("\n=== Retorno médio por tercil no 2024Q3 ===")
    print(q3_2024.groupby('tercil')['retorno'].describe())



    # dados = pd.read_sql("SELECT * FROM tamanho_empresa_b3", engine)
    # dados['trimestre'] = pd.to_datetime(dados['trimestre']).dt.tz_localize(None)
    # dados['valor_total'] = dados['qtd_acoes'] * dados['preco_fechamento']
    

    # print("=== Ações por trimestre ===")
    # print(dados.groupby('trimestre')['isin'].nunique().tail(12))

    # print("\n=== Nulos por coluna ===")
    # print(dados[['preco_fechamento', 'qtd_acoes', 'valor_total']].isna().sum())

    # print("\n=== Trimestres disponíveis ===")
    # print(sorted(dados['trimestre'].unique())[-8:])

    # # Pega o trimestre mais recente disponível dinamicamente
    # ultimo_trimestre = dados['trimestre'].max()
    # recente = dados[dados['trimestre'] == ultimo_trimestre].copy()
    # print("Total de linhas:", len(recente))
    # print("qtd_acoes nulos:", recente['qtd_acoes'].isna().sum())
    # print("preco_fechamento nulos:", recente['preco_fechamento'].isna().sum())
    # print("valor_total nulos:", recente['valor_total'].isna().sum())
    # print("valor_total zeros:", (recente['valor_total'] == 0).sum())
    # print("\nAmostra:")
    # print(recente[['isin', 'preco_fechamento', 'qtd_acoes', 'valor_total']].head(10))
    # print(f"\n=== Market cap no trimestre {ultimo_trimestre} ===")
    # recente = dados[dados['trimestre'] == ultimo_trimestre].copy()
    # recente['tercil'] = pd.qcut(recente['valor_total'].dropna(), 3, labels=['Small','Mid','Big'], duplicates='drop')
    # print(recente.groupby('tercil')['valor_total'].describe() / 1e6)

        
if __name__ == "__main__":
    engine = create_engine(url_db)
    gerador = Gera_indices(engine)
    # teste()
    

    smb = gerador.fator_smb_nefin()


    df = pd.read_csv('/home/guilhermedesouzafornaciari/Documentos/github/research/Backend/src/scripts/codigoPython/planilhas/nefin_factors.csv')
    df['Date'] = pd.to_datetime(df['Date'])

    nefin_trimestral = (
        df[df['Date'].dt.year >= 2021]
        .groupby(df['Date'].dt.to_period('Q'))['SMB']
        .apply(lambda x: (1 + x).prod() - 1)
    )
    nefin_trimestral.index = nefin_trimestral.index.to_timestamp(how='end').normalize()

    smb_seu = smb.copy()
    smb_seu.index = smb_seu.index.tz_localize(None)

    # Converter ambos para Period('Q') para alinhar sem depender de data exata
    smb_seu.index = smb_seu.index.to_period('Q')
    nefin_trimestral.index = nefin_trimestral.index.to_period('Q')

    comparacao = pd.DataFrame({
        'NEFIN': nefin_trimestral,
        'Seu_SMB': smb_seu
    }).dropna()

    print("=== Índices após conversão ===")
    print("NEFIN:", nefin_trimestral.index[:3])
    print("SEU:", smb_seu.index[:3])

    print("\n=== Correlação ===")
    print(comparacao.corr())
    print("\n=== Diferença média absoluta ===")
    print((comparacao['NEFIN'] - comparacao['Seu_SMB']).abs().mean())
    print("\n=== Comparação ===")
    print(comparacao)
