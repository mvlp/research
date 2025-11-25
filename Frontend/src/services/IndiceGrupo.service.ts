import { IndiceGrupoEntity } from "../entities/IndiceGrupo.entity";
import { BaseRestService } from "../shared/interfaces/rest-service.interface";

export class IndiceGrupoService extends BaseRestService<IndiceGrupoEntity>{
    route = "Grupo_do_indice"
}