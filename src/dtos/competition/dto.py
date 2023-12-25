import datetime
from typing import Optional
from pydantic import BaseModel, Field

from src.dtos.get_all.dto import GetAllDTO
from src.utils.decorators.builder import builder


class CompetitionDTO(BaseModel):
    id: str
    result: str
    date: datetime.datetime
    stadium_id: str
    sport_id: str
    judges_ids: list[str]


class CompetitionAddDTO(BaseModel):
    result: str
    date: datetime.datetime
    stadium_id: str
    sport_id: str
    judges_ids: list[str]


class CompetitionEditDTO(BaseModel):
    result: str
    date: datetime.datetime
    stadium_id: str
    sport_id: str
    judges_ids: list[str]


class CompetitionPartialEditDTO(BaseModel):
    result: Optional[str]
    date: Optional[datetime.datetime]
    stadium_id: Optional[str]
    sport_id: Optional[str]
    judges_ids: Optional[list[str]]


class CompetitionGetAllDTO(GetAllDTO):
    data: list[CompetitionDTO]


@builder
class CompetitionGetAllDTOBuilder:
    _model = CompetitionGetAllDTO
    _attr_total_pages: int
    _attr_total_elements: int
    _attr_current_page: int
    _attr_has_next_page: bool
    _attr_data: list[CompetitionDTO]
