from fastapi import APIRouter
from src.services.judge.service import JudgeService
from src.dtos.judge.dto import (
    JudgeDTO,
    JudgeAddDTO,
    JudgeEditDTO,
    JudgePartialEditDTO,
    JudgeGetAllDTO
)

router = APIRouter(
    prefix="/judge",
    tags=["judge"],
)


class RegionController:
    @staticmethod
    @router.get("")
    def get_judges(
            page: int | None = None,
            per_page: int | None = None,
            simple_filter: str | None = None
    ) -> JudgeGetAllDTO:
        return JudgeService().get_judges(page, per_page, simple_filter)

    @staticmethod
    @router.post("")
    def add_judge(region: JudgeAddDTO):
        return JudgeService().create_judge(region)

    @staticmethod
    @router.delete("/{id_arg}")
    def delete_region(id_arg: str):
        return JudgeService().delete_judge(id_arg)

    @staticmethod
    @router.get("/{id_arg}")
    def get_region(id_arg: str) -> JudgeDTO:
        return JudgeService().get_judge(id_arg)

    @staticmethod
    @router.put("/{id_arg}")
    def replace_region(id_arg: str, judge: JudgeEditDTO):
        return JudgeService().update_judge(id_arg=id_arg, judge=judge)

    @staticmethod
    @router.patch("/{id_arg}")
    def replace_region(id_arg: str, judge: JudgePartialEditDTO):
        return JudgeService().update_judge(id_arg=id_arg, judge=judge)
