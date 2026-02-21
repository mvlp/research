from typing import Any, Generic, Type

from  src.infra.Database.UnitOfWork import UnitOfWorkRepositories, DicionarioEntidadeRepository
from  src.infra.Database.repositories.Base_repository import E, M, BaseRepository


class Base_service(Generic[E, M]):
    uw_repos: DicionarioEntidadeRepository
    repo: Any
    def __init__(self, entity_cls: Type[E]) -> None:
        self.uw_repos = UnitOfWorkRepositories
        self.repo: Any = UnitOfWorkRepositories[entity_cls]

    def get_all(self,params: dict[str,Any]) -> list[E]:
        return self.repo.get_all(params)

    def get_one(self, id: int) -> E | None:
        return self.repo.get_one(id)
    def update_one(self, entity: E) -> E | None:
        return self.repo.update_one(entity)
    def create_one(self,entity: E) -> E:
        return self.repo.create_one(entity)
    def delete_one(self, id: int) -> None:
        return self.repo.delete_one(id)