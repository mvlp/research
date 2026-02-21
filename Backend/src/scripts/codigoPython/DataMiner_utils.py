from requests import get

import json
import base64


class Codigo_negociacao:
    isin: str
    code: str
    def __init__(self, isin: str, code: str) -> None:
        self.isin = isin
        self.code = code

    def is_equal(self, type_stock: str):
        return self.inferir_type_stock() == type_stock

    def inferir_type_stock(self) -> str | None:
        if self.code.endswith("11"):
            return "UNIT"

        sufixo = self.code[-1]

        return {
            "3": "ON",
            "4": "PN",
            "5": "PNA",
            "6": "PNB",
        }.get(sufixo)


        

class Empresa:
    codeCVM: str
    cnpj: str
    issuingCompany: str
    def __init__(self, codeCVM: str, cnpj: str, issuingCompany: str) -> None:
        self.codeCVM = codeCVM 
        self.cnpj = cnpj 
        self.issuingCompany = issuingCompany  



class DataMinerUtil:
    @staticmethod
    def  get_codes_http(empresa:Empresa)-> list[Codigo_negociacao]:

        payload = {"codeCVM":empresa.codeCVM,"language":"pt-br"}
        json_str = json.dumps(payload, separators=(",", ":"))
        b64 = base64.b64encode(json_str.encode("utf-8")).decode("utf-8")
        req = {}
        try:
            for _ in range(3):
                req = get(f"https://sistemaswebb3-listados.b3.com.br/listedCompaniesProxy/CompanyCall/GetDetail/{b64}").json()
                break
        except:
            req = {}
        if not req or not req["otherCodes"]: return []
        codes: list[Codigo_negociacao] = []
        for code in req["otherCodes"]:
            codes.append(Codigo_negociacao(code["isin"],code["code"]))
        return codes

    @staticmethod
    def get_proventos_dinheiro_http(empresaNome:str, pageNumber: int):
        payload = {"language":"pt-br","pageNumber":pageNumber,"pageSize":120,"tradingName": empresaNome}
        json_str = json.dumps(payload, separators=(",", ":"))
        b64 = base64.b64encode(json_str.encode("utf-8")).decode("utf-8")
        req = {}
        for _ in range(3):
            try:
                req = get(f"https://sistemaswebb3-listados.b3.com.br/listedCompaniesProxy/CompanyCall/GetListedCashDividends/{b64}").json()
                break
            except Exception as e:
                req = {}
        return req

    @staticmethod
    def get_proventos_aprovados_http(empresa: Empresa):
        payload = {"issuingCompany": empresa.issuingCompany,"language":"pt-br"}
        json_str = json.dumps(payload, separators=(",", ":"))
        b64 = base64.b64encode(json_str.encode("utf-8")).decode("utf-8")
        req = {}
        for _ in range(10):
            try:
                req = get(f"https://sistemaswebb3-listados.b3.com.br/listedCompaniesProxy/CompanyCall/GetListedSupplementCompany/{b64}").json()
                break
            except Exception as Exc:
                req = {}
                print("erro req eventos ")
        return req

    @staticmethod
    def get_empresas_http() -> list[Empresa]:
        
        payload = {
            "language": "pt-br",
            "pageNumber": 1,
            "pageSize": 120
        }

        json_str = json.dumps(payload, separators=(",", ":"))
        b64 = base64.b64encode(json_str.encode("utf-8")).decode("utf-8")

        req = get(f"https://sistemaswebb3-listados.b3.com.br/listedCompaniesProxy/CompanyCall/GetInitialCompanies/{b64}" ).json()
        paginas_totais = req["page"]["totalPages"]
        codigos = []
        for i in range(1,paginas_totais + 1):
            payload["pageNumber"] = i
            json_str = json.dumps(payload, separators=(",", ":"))
            b64 = base64.b64encode(json_str.encode("utf-8")).decode("utf-8")
            for _ in range(3):
                try:
                    req = get(f"https://sistemaswebb3-listados.b3.com.br/listedCompaniesProxy/CompanyCall/GetInitialCompanies/{b64}").json()
                    break;
                except Exception as exc:
                    req = None
                    print("erro req pagina ",i)
            if req == None: raise Exception("Erro de requisições")

            for result in req["results"]:
                codigos.append(Empresa(result["codeCVM"],result["cnpj"],result["issuingCompany"]))
        return codigos
            