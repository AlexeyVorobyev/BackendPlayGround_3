from typing import TypedDict, NotRequired
from src.SQLAlchemy.filter import SQLAlchemyFilter
from src.models.judge.model import JudgeModel
from src.utils.functions.clear_dict_from_none import clear_nested_dict_from_none


class SimpleFilterConfigTyped(TypedDict):
    name: NotRequired[str]
    surname: NotRequired[str]
    patronymic: NotRequired[str]


class ConfigTyped(TypedDict):
    simple_filter: NotRequired[SimpleFilterConfigTyped]
    id: NotRequired[list[str]]
    name: NotRequired[list[str]]
    patronymic: NotRequired[list[str]]


class JudgeFilter(SQLAlchemyFilter[JudgeModel]):
    _model = JudgeModel

    def __init__(self, config_arg: ConfigTyped):
        self._config = clear_nested_dict_from_none(config_arg)
