import { IndiceEntity } from "../entities/Indice.entity";
import { BaseRestService } from "../shared/interfaces/rest-service.interface";

export class IndiceService extends BaseRestService<IndiceEntity>{
    route = "indice"
}