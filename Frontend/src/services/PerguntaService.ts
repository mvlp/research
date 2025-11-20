import { PerguntaEntity } from "../entities/Pergunta.entity";
import { BaseRestService } from "../shared/interfaces/rest-service.interface";

export class PerguntaService extends BaseRestService<PerguntaEntity>{
    route = "pergunta"
}