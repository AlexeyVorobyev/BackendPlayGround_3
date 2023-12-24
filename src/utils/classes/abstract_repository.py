from abc import ABC, abstractmethod
from typing import TypeVar, Generic

Model = TypeVar('Model')
Filter = TypeVar('Filter')


class AbstractRepository(Generic[Model, Filter], ABC):
    _model: Model

    @abstractmethod
    def total_elements(self, filter_instance: Filter) -> int:
        pass

    @abstractmethod
    def get_all(self, page: int, per_page: int, filter_instance: Filter) -> list[Model]:
        pass

    @abstractmethod
    def get_by_id(self, id_arg: str) -> Model | None:
        pass

    @abstractmethod
    def create(self, data: dict) -> str:
        pass

    @abstractmethod
    def update(self, id_arg: str, data: dict) -> str:
        pass

    @abstractmethod
    def delete_by_id(self, id_arg: str) -> str:
        pass
