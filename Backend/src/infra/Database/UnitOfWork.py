from typing import Type
from src.infra.Database.repositories.governanca_repository import Governanca_repository
from src.infra.Database.repositories.Dimensao_repository import Dimensao_repository
from src.infra.Database.Models.Indice import Indice
from  src.Entities.Dimensao_entity import Dimensao_entity
from  src.Entities.Indice_entity import Indice_entity
from  src.infra.Database.Models.auto.cgvn_praticas import cgvn_praticas
from  src.infra.Database.Models.Dimensao import Dimensao
from  src.infra.Database.Models.pergunta_dimensao import Pergunta_Dimensao
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
    Governanca_entity: Governanca_repository(db.engine),
    Dimensao_entity: Dimensao_repository(db.engine),
    Pergunta_entity: BaseRepository(Pergunta_entity, Pergunta, db.engine),
    Indice_entity: BaseRepository(Indice_entity, Indice, db.engine)
}
