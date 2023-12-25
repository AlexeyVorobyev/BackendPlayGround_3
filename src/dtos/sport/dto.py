from typing import Optional
from pydantic import BaseModel, Field
from src.dtos.get_all.dto import GetAllDTO
from src.utils.decorators.builder import builder


class SportDTO(BaseModel):
    id: str
    name: str

class SportAddDTO(BaseModel):
    name: str


class SportEditDTO(BaseModel):
    name: str


class SportPartialEditDTO(BaseModel):
    name: Optional[str]


class SportGetAllDTO(GetAllDTO):
    data: list[SportDTO]


@builder
class SportGetAllDTOBuilder:
    _model = SportGetAllDTO
    _attr_total_pages: int
    _attr_total_elements: int
    _attr_current_page: int
    _attr_has_next_page: bool
    _attr_data: list[SportDTO]
