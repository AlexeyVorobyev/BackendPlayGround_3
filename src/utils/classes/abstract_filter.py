from abc import ABC, abstractmethod
from typing import TypeVar, Generic

Model = TypeVar('Model')


class AbstractFilter(Generic[Model], ABC):
    _model: Model
    _config: dict

    @abstractmethod
    def filter(self, query):
        pass
