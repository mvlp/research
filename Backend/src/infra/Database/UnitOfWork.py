from typing import Type
from  src.Entities.Indice_entity import Indice_entity
from  src.infra.Database.Models.Governanca import Governanca
from  src.infra.Database.Models.Indice import Indice
from  src.infra.Database.Models.pergunta_indice import Pergunta_indice
from  src.Entities.Pergunta_indice_entity import Pergunta_indice_entity
from src.Entities.Governanca_entity import Governanca_entity
from  src.Entities.Pergunta_entity import Pergunta_entity
from src.infra.Database.Models.pergunta import Pergunta
from src.infra.Database.repositories.Base_repository import E, M, BaseRepository
from src.infra.Database.extensions import db

##Define as entidades compativeis no sistema e quem irá provelas no sistema inteiro 
DicionarioEntidadeRepository = dict[
    Type[E], 
    BaseRepository[E, M]
    ]
UnitOfWorkRepositories: DicionarioEntidadeRepository = {
    Governanca_entity: BaseRepository(Governanca_entity, Governanca, db.engine),
    Indice_entity: BaseRepository(Indice_entity, Indice, db.engine),
    Pergunta_indice_entity: BaseRepository(Pergunta_indice_entity, Pergunta_indice, db.engine),
    Pergunta_entity: BaseRepository(Pergunta_entity, Pergunta, db.engine)
}
