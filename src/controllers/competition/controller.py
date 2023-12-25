from fastapi import APIRouter
from src.services.competition.service import CompetitionService
from src.dtos.competition.dto import (
    CompetitionDTO,
    CompetitionAddDTO,
    CompetitionEditDTO,
    CompetitionPartialEditDTO,
    CompetitionGetAllDTO
)

router = APIRouter(
    prefix="/competition",
    tags=["competition"],
)


class CompetitionController:
    @staticmethod
    @router.get("")
    def get_competitions(
            page: int | None = None,
            per_page: int | None = None,
            simple_filter: str | None = None
    ) -> CompetitionGetAllDTO:
        return CompetitionService().get_competitions(page, per_page, simple_filter)

    @staticmethod
    @router.post("")
    def add_competition(region: CompetitionAddDTO):
        return CompetitionService().create_competition(region)

    @staticmethod
    @router.delete("/{id_arg}")
    def delete_competition(id_arg: str):
        return CompetitionService().delete_competition(id_arg)

    @staticmethod
    @router.get("/{id_arg}")
    def get_competition(id_arg: str) -> CompetitionDTO:
        return CompetitionService().get_competition(id_arg)

    @staticmethod
    @router.put("/{id_arg}")
    def replace_competition(id_arg: str, competition: CompetitionEditDTO):
        return CompetitionService().update_competition(id_arg=id_arg, competition=competition)

    @staticmethod
    @router.patch("/{id_arg}")
    def replace_competition(id_arg: str, competition: CompetitionPartialEditDTO):
        return CompetitionService().update_competition(id_arg=id_arg, competition=competition)
