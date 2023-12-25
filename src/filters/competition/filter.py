from typing import TypedDict, NotRequired
from src.SQLAlchemy.filter import SQLAlchemyFilter
from src.models.competition.model import CompetitionModel
from src.utils.functions.clear_dict_from_none import clear_nested_dict_from_none


class SimpleFilterConfigTyped(TypedDict):
    result: NotRequired[str]


class ConfigTyped(TypedDict):
    simple_filter: NotRequired[SimpleFilterConfigTyped]
    id: NotRequired[list[str]]


class CompetitionFilter(SQLAlchemyFilter[CompetitionModel]):
    _model = CompetitionModel

    def __init__(self, config_arg: ConfigTyped):
        self._config = clear_nested_dict_from_none(config_arg)
