from typing import Optional
from pydantic import BaseModel, Field
from src.dtos.get_all.dto import GetAllDTO
from src.utils.decorators.builder import builder


class StadiumDTO(BaseModel):
    id: str
    name: str
    address: str
    seats: int = Field(..., gt=-1)


class StadiumAddDTO(BaseModel):
    name: str
    address: str
    seats: int = Field(..., gt=-1)


class StadiumEditDTO(BaseModel):
    name: str
    address: str
    seats: int = Field(..., gt=-1)


class StadiumPartialEditDTO(BaseModel):
    name: Optional[str]
    address: Optional[str]
    seats: Optional[int] = Field(..., gt=-1)


class StadiumGetAllDTO(GetAllDTO):
    data: list[StadiumDTO]


@builder
class StadiumGetAllDTOBuilder:
    _model = StadiumGetAllDTO
    _attr_total_pages: int
    _attr_total_elements: int
    _attr_current_page: int
    _attr_has_next_page: bool
    _attr_data: list[StadiumDTO]
