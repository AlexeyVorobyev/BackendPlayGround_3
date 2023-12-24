from pydantic import BaseModel


class GetAllDTO(BaseModel):
    total_pages: int
    total_elements: int
    current_page: int
    has_next_page: bool
    data: list
