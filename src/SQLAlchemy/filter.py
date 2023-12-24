from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Any

from sqlalchemy import Select, or_

from src.utils.classes.abstract_filter import AbstractFilter

Model = TypeVar('Model')


class SQLAlchemyFilter(Generic[Model], AbstractFilter[Model], ABC):
    _model: Model = None
    _config: dict

    @abstractmethod
    def __init__(self, config_arg: dict):
        pass

    def _internal_filter(self, query, config_value, config_key) -> Select:
        print(config_key)
        if config_key == 'simple_filter':
            return query.filter(or_(
                getattr(self._model, key).contains(config_value[key]) for key in config_value
            ))
        return query

    def filter(self, query: Select):
        for key in self._config:
            query = self._internal_filter(query, self._config[key], key)
        return query
