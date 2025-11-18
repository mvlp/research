from typing import Generic, Type

from Backend.src.infra.Database.UnitOfWork import UnitOfWorkRepositories, DicionarioEntidadeRepository
from Backend.src.infra.Database.repositories.Base_repository import E, M, BaseRepository


class Base_service(Generic[E, M]):
    uw_repos: DicionarioEntidadeRepository
    repo: BaseRepository[E, M]
    def __init__(self, entity_cls: Type[E]) -> None:
        self.uw_repos = UnitOfWorkRepositories
        self.repo: BaseRepository[E, M] = UnitOfWorkRepositories[entity_cls]

    def get_one(self, id: int) -> E | None:
        return self.repo.get_one(id)
    def update_one(self, entity: E) -> E | None:
        return self.repo.update_one(entity)
    def create_one(self,entity) -> None:
        return self.repo.create_one(entity)
    def delete_one(self, id: int) -> None:
        return self.repo.delete_one(id)