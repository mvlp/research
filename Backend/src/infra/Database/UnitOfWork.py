from typing import Type
from Backend.src.Entities.pergunta_entity import Pergunta_entity
from Backend.src.infra.Database.Models.pergunta import Pergunta
from src.infra.Database.repositories.Base_repository import E, M, BaseRepository


##Define as entidades compativeis no sistema e quem irá provelas no sistema inteiro 
DicionarioEntidadeRepository = dict[
    Type[E], 
    BaseRepository[E, M]
    ]
UnitOfWorkRepositories: DicionarioEntidadeRepository = {
    Pergunta_entity: BaseRepository(Pergunta_entity, Pergunta)
}
