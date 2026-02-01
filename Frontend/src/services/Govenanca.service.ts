import { HttpClient } from "@angular/common/http";
import { DimensaoEntity } from "../entities/Dimensao.entity";
import { environment } from "../shared/interfaces/rest-service.interface";
import { inject } from "@angular/core";
import { tabelaData } from "../entities/TabelaData.entity";
import GraficoEntity from "../entities/Grafico.entity";


export class GovernancaService {
    http: HttpClient = inject(HttpClient);
    route = "governanca"
    getDadosFaltantes(){
        return this.http.get<Array<any>>(`${environment.base_url}${this.route}/faltantes`)
    }

    getEmpresas(empresa:string){
        return this.http.get<Array<SelectDataEntity>>(`${environment.base_url}${this.route}/empresa`, {params:{empresa}})
    }
    getTable(){
        return this.http.get<Array<tabelaData>>(`${environment.base_url}${this.route}/tabela`)
    }
    getGraficoPercentuais(capitulo:string, resposta:string){
        return this.http.get<GraficoEntity>(`${environment.base_url}${this.route}/grafico/percentual`, {params: {capitulo,resposta}})
    }
    getGraficoQtd(capitulo:string, resposta:string){
        return this.http.get<GraficoEntity>(`${environment.base_url}${this.route}/grafico/quantidade`, {params: {capitulo,resposta}})
    }

}