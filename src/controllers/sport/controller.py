from fastapi import APIRouter
from src.services.sport.service import SportService
from src.dtos.sport.dto import (
    SportDTO,
    SportAddDTO,
    SportEditDTO,
    SportPartialEditDTO,
    SportGetAllDTO
)

router = APIRouter(
    prefix="/sport",
    tags=["sport"],
)


class SportController:
    @staticmethod
    @router.get("")
    def get_sports(
            page: int | None = None,
            per_page: int | None = None,
            simple_filter: str | None = None
    ) -> SportGetAllDTO:
        return SportService().get_sports(page, per_page, simple_filter)

    @staticmethod
    @router.post("")
    def add_sport(region: SportAddDTO):
        return SportService().create_sport(region)

    @staticmethod
    @router.delete("/{id_arg}")
    def delete_sport(id_arg: str):
        return SportService().delete_sport(id_arg)

    @staticmethod
    @router.get("/{id_arg}")
    def get_sport(id_arg: str) -> SportDTO:
        return SportService().get_sport(id_arg)

    @staticmethod
    @router.put("/{id_arg}")
    def replace_sport(id_arg: str, sport: SportEditDTO):
        return SportService().update_sport(id_arg=id_arg, sport=sport)

    @staticmethod
    @router.patch("/{id_arg}")
    def replace_sport(id_arg: str, sport: SportPartialEditDTO):
        return SportService().update_sport(id_arg=id_arg, sport=sport)
