from pydantic import BaseModel


class PaginationDTO(BaseModel):
    page: int = 0
    per_page: int = 8

