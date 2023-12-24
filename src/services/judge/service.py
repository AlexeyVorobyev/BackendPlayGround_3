import math
from typing import Any
from src.dtos.judge.dto import (
    JudgeGetAllDTO,
    JudgeGetAllDTOBuilder,
    JudgeDTO,
    JudgeAddDTO,
    JudgeEditDTO,
    JudgePartialEditDTO
)
from src.dtos.pagination.dto import PaginationDTO
from src.filters.judge.filter import JudgeFilter
from src.repositories.judge.repository import JudgeRepository
from src.utils.decorators.singleton import singleton
from src.utils.functions.clear_dict_from_none import clear_dict_from_none


@singleton
class JudgeService:
    _repository = JudgeRepository()

    def get_judges(self, page, per_page, simple_filter) -> JudgeGetAllDTO:
        pagination = PaginationDTO(**clear_dict_from_none(dict(page=page, per_page=per_page)))
        judge_filter_instance = JudgeFilter({
            'simple_filter': {
                'name': simple_filter,
                'surname': simple_filter,
                'patronymic': simple_filter
            }
        })

        judge_instances = self._repository.get_all(
            page=pagination.page,
            per_page=pagination.per_page,
            filter_instance=judge_filter_instance
        )

        judge_get_all_builder: Any = JudgeGetAllDTOBuilder()

        return (
            judge_get_all_builder
            .total_elements(self._repository.total_elements(filter_instance=judge_filter_instance))
            .total_pages(math.ceil(judge_get_all_builder.attr_total_elements() / pagination.per_page))
            .current_page(pagination.page)
            .data([
                dict(JudgeDTO(
                    id=str(instance.id),
                    name=instance.name,
                    surname=instance.surname,
                    patronymic=instance.patronymic,
                )) for instance in judge_instances
            ])
            .has_next_page(pagination.page + 1 < judge_get_all_builder.attr_total_pages())
            .build()
        )

    def create_judge(self, judge: JudgeAddDTO) -> str:
        return self._repository.create(dict(judge))

    def get_judge(self, id_arg: str) -> JudgeDTO:
        judge_instance = self._repository.get_by_id(id_arg=id_arg)

        if judge_instance is None:
            raise Exception('No entities with provided id')

        return JudgeDTO(
            id=str(judge_instance.id),
            name=judge_instance.name,
            description=judge_instance.description
        )

    def delete_judge(self, id_arg: str | None) -> str:
        return self._repository.delete_by_id(id_arg)

    def update_judge(self, id_arg: str | None, judge: JudgeEditDTO | JudgePartialEditDTO) -> str:
        return self._repository.update(id_arg=id_arg, data=dict(judge))
