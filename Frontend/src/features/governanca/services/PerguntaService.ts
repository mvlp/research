import { BaseRestService } from "../../shared/interfaces/rest-service.interface";
import { PerguntaEntity } from "../entities/Pergunta.entity";

export class PerguntaService extends BaseRestService<PerguntaEntity>{
    route = "pergunta"
}