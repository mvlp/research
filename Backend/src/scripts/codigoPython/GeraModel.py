from os import listdir, mkdir, remove, rename
from pathlib import Path
from shutil import move
from zipfile import ZipFile
from requests import get
from .DataMiner import DataMiner

dir_base = Path(__file__).resolve().parent  # Isso dá "CodigoPython/"
dir_meta = str(dir_base) + "/data/zip/META/"
dir_model = str(dir_base) + "/mineracao/model/"


def pega_arquivos(url:str):
    html = get(url).text # Pega o HTML da página
    index_inicial = html.find("<pre>")
    index_final = html.find("</pre>") #seleciona onde tem os links
    hyperlinks = html[index_inicial:index_final].split("\n")
    hyperlinks.pop(0)
    hyperlinks.pop(-1)
    for i in range(len(hyperlinks)): #extrai os links
        start_link = hyperlinks[i].find('href="') + len('href="')
        end_link = hyperlinks[i].find('">', start_link)
        hyperlinks[i] = hyperlinks[i][start_link:end_link]
    return hyperlinks

def baixar_meta():
    url_base = "https://dados.cvm.gov.br/dados/CIA_ABERTA/DOC/" 
    nomes = pega_arquivos(url_base)
    nomes = list(map(lambda s: s[:-1], nomes)) # Remove o / no fim da lista
    diretorios = listdir(dir_meta)
    for nome in nomes:
        url = url_base + nome + "/META/"
        nomes_arquivos = DataMiner.pegar_nomes_arquivos(url)
        DataMiner.baixar_zips(url,"META",nomes_arquivos)
        arquivos = listdir(dir_meta)
        arquivos = list(filter(lambda s: s.endswith(".txt") or s.endswith(".zip"),arquivos)) # pega apenas os .zip
        dir = f"{dir_meta}{nome}/"
        if not nome in diretorios:
            mkdir(dir)
        for arquivo in arquivos:
            if arquivo.endswith(".zip"):
                with ZipFile(dir_meta + arquivo , 'r') as zip_ref:
                    zip_ref.extractall(dir)
                remove(dir_meta + arquivo)
            else: 
                move(dir_meta+arquivo,dir+arquivo)

TYPE_MAP = {
    "varchar": lambda _: f"db.Text",
    "nvarchar": lambda _: f"db.Text",
    "char": lambda _: f"db.Text",
    "date": lambda _: "db.Date",
    "datetime": lambda _: "db.DateTime",
    "int": lambda _: "db.Integer",
    "decimal": lambda _: "db.Float",
    "smallint": lambda _: "db.Integer",
    "bigint": lambda _: "db.BigInteger",
    "numeric": lambda p, s: f"db.Numeric({p}, {s})"
}


def gerar_model(schema: str, name:str) -> str:
    campos = schema.split("Campo:")
    colunas = []

    for campo in campos[1:]:
        linhas = campo.strip().splitlines()
        nome = linhas[0].strip()

        tipo = None
        tamanho = None
        precisao = None
        scale = None

        for linha in linhas:
            if "Tipo Dados:" in linha:
                tipo = linha.split(":")[1].strip().lower()
            elif "Tamanho" in linha:
                tamanho = linha.split(":")[1].strip()
            elif "Precisão" in linha:
                precisao = linha.split(":")[1].strip()
            elif "Scale" in linha:
                scale = linha.split(":")[1].strip()
        if tipo is None:
            raise ValueError(f"Tipo de dado não encontrado para o campo {nome}")
        print(tipo)
        if tipo == "numeric":
            coluna_tipo = TYPE_MAP[tipo](precisao, scale)
        else:
            coluna_tipo = TYPE_MAP[tipo](tamanho)

        colunas.append(
            f"    {nome} = db.Column({coluna_tipo}, nullable=True)"
        )

    model = [
        "from src.infra.Database.extensions import db",
        "",
        f"class {name}(db.Model):",
        f'    __tablename__ = "{name}"',
        "",
        "    id = db.Column(db.Integer, primary_key=True, autoincrement=True)",
        "    arquivo_origem = db.Column(db.Text, nullable=True)",
        "    tipo_csv = db.Column(db.Text, nullable=True)",
        "",
    ]

    model.extend(colunas)

    return "\n".join(model)


def tratar_nome(txt:str):
    nome = txt.split("_")
    nome[-1] = nome[-1].split(".")[0] # remove o .txt
    nome.pop(0)
    nome.pop(1)
    nome.pop(1)
    if len(nome) == 1:
        nome.append("principal")
    return "_".join(nome)   
def create_dir_if_dont_exist(categoria: str ):
    diretorios_model = listdir(dir_model)
    if not categoria in diretorios_model:
        dir = dir_model + f"{categoria}/"
        mkdir(dir) 


if __name__ == "__main__":
    baixar_meta()
    metas = listdir(dir_meta)
    for categoria in metas:
        txts = listdir(dir_meta + categoria)
        create_dir_if_dont_exist(categoria)
        for txt in txts:
            nome = tratar_nome(txt)
            with open(f"{dir_meta}/{categoria}/{txt}",encoding="latin-1") as origem, open(f"{dir_model}/{nome}.py", "w") as model:
                string_arquivo = origem.read().rstrip()
                model.write(gerar_model(string_arquivo,nome))
                
                    
    
        
        
