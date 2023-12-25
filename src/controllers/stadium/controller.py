from fastapi import APIRouter
from src.services.stadium.service import StadiumService
from src.dtos.stadium.dto import (
    StadiumDTO,
    StadiumAddDTO,
    StadiumEditDTO,
    StadiumPartialEditDTO,
    StadiumGetAllDTO
)

router = APIRouter(
    prefix="/stadium",
    tags=["stadium"],
)


class StadiumController:
    @staticmethod
    @router.get("")
    def get_stadiums(
            page: int | None = None,
            per_page: int | None = None,
            simple_filter: str | None = None
    ) -> StadiumGetAllDTO:
        return StadiumService().get_stadiums(page, per_page, simple_filter)

    @staticmethod
    @router.post("")
    def add_stadium(region: StadiumAddDTO):
        return StadiumService().create_stadium(region)

    @staticmethod
    @router.delete("/{id_arg}")
    def delete_stadium(id_arg: str):
        return StadiumService().delete_stadium(id_arg)

    @staticmethod
    @router.get("/{id_arg}")
    def get_stadium(id_arg: str) -> StadiumDTO:
        return StadiumService().get_stadium(id_arg)

    @staticmethod
    @router.put("/{id_arg}")
    def replace_stadium(id_arg: str, stadium: StadiumEditDTO):
        return StadiumService().update_stadium(id_arg=id_arg, stadium=stadium)

    @staticmethod
    @router.patch("/{id_arg}")
    def replace_stadium(id_arg: str, stadium: StadiumPartialEditDTO):
        return StadiumService().update_stadium(id_arg=id_arg, stadium=stadium)
