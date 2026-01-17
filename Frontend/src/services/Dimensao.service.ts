import { DimensaoEntity } from "../entities/Dimensao.entity";
import { BaseRestService } from "../shared/interfaces/rest-service.interface";

export class DimensaoService extends BaseRestService<DimensaoEntity>{
    route = "Dimensao"
}