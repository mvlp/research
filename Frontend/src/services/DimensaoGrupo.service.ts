import { DimensaoGrupoEntity } from "../entities/DimensaoGrupo.entity";
import { BaseRestService } from "../shared/interfaces/rest-service.interface";

export class DimensaoGrupoService extends BaseRestService<DimensaoGrupoEntity>{
    route = "Grupo_do_Dimensao"
}