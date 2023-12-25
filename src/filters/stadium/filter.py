from typing import TypedDict, NotRequired
from src.SQLAlchemy.filter import SQLAlchemyFilter
from src.models.stadium.model import StadiumModel
from src.utils.functions.clear_dict_from_none import clear_nested_dict_from_none


class SimpleFilterConfigTyped(TypedDict):
    name: NotRequired[str]
    address: NotRequired[str]
    seats: NotRequired[int]


class ConfigTyped(TypedDict):
    simple_filter: NotRequired[SimpleFilterConfigTyped]
    id: NotRequired[list[str]]
    name: NotRequired[list[str]]
    address: NotRequired[list[str]]


class StadiumFilter(SQLAlchemyFilter[StadiumModel]):
    _model = StadiumModel

    def __init__(self, config_arg: ConfigTyped):
        self._config = clear_nested_dict_from_none(config_arg)
