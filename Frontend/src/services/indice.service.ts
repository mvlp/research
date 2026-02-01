import GraficoEntity from "../entities/Grafico.entity";
import { IndiceEntity } from "../entities/Indice.entity";
import { BaseRestService, environment } from "../shared/interfaces/rest-service.interface";

export class IndiceService extends BaseRestService<IndiceEntity>{
    route = "Indice"
    getEmpresaOverview(cnpj_empresa:string, idIndice:number){
        return this.http.get<Record<string,GraficoEntity>>(`${environment.base_url}${this.route}/overview`, {params: {cnpj_empresa,idIndice}})
    }
}