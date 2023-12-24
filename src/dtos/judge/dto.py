from typing import Optional

from pydantic import BaseModel
from src.dtos.get_all.dto import GetAllDTO
from src.utils.decorators.builder import builder


class JudgeDTO(BaseModel):
    id: str
    name: str
    surname: str
    patronymic: str


class JudgeAddDTO(BaseModel):
    name: str
    surname: str
    patronymic: str


class JudgeEditDTO(BaseModel):
    name: str
    surname: str
    patronymic: str


class JudgePartialEditDTO(BaseModel):
    name: Optional[str]
    surname: Optional[str]
    patronymic: Optional[str]


class JudgeGetAllDTO(GetAllDTO):
    data: list[JudgeDTO]


@builder
class JudgeGetAllDTOBuilder:
    _model = JudgeGetAllDTO
    _attr_total_pages: int
    _attr_total_elements: int
    _attr_current_page: int
    _attr_has_next_page: bool
    _attr_data: list[JudgeDTO]
