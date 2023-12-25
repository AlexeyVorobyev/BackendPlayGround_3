import math
import uuid
from typing import Any
from src.dtos.competition.dto import (
    CompetitionGetAllDTO,
    CompetitionGetAllDTOBuilder,
    CompetitionDTO,
    CompetitionAddDTO,
    CompetitionEditDTO,
    CompetitionPartialEditDTO
)
from src.dtos.judge_competition.dto import JudgeCompetitionAddDTO
from src.dtos.pagination.dto import PaginationDTO
from src.filters.competition.filter import CompetitionFilter
from src.repositories.competition.repository import CompetitionRepository
from src.repositories.judge.repository import JudgeRepository
from src.repositories.judge_competition.repository import JudgeCompetitionRepository
from src.utils.decorators.singleton import singleton
from src.utils.functions.clear_dict_from_none import clear_dict_from_none


@singleton
class CompetitionService:
    _repository = CompetitionRepository()
    _judge_competition_repository = JudgeCompetitionRepository()
    _judge_repository = JudgeRepository()

    def get_competitions(self, page, per_page, simple_filter) -> CompetitionGetAllDTO:
        pagination = PaginationDTO(**clear_dict_from_none(dict(page=page, per_page=per_page)))
        competition_filter_instance = CompetitionFilter({
            'simple_filter': {
                'result': simple_filter,
            }
        })

        competition_instances = self._repository.get_all(
            page=pagination.page,
            per_page=pagination.per_page,
            filter_instance=competition_filter_instance
        )

        competition_get_all_builder: Any = CompetitionGetAllDTOBuilder()

        return (
            competition_get_all_builder
            .total_elements(self._repository.total_elements(filter_instance=competition_filter_instance))
            .total_pages(math.ceil(competition_get_all_builder.attr_total_elements() / pagination.per_page))
            .current_page(pagination.page)
            .data([
                dict(CompetitionDTO(
                    id=str(instance.id),
                    result=instance.result,
                    date=instance.date,
                    stadium_id=str(instance.stadium_id),
                    sport_id=str(instance.sport_id),
                    judges_ids=[str(judge_instance.id) for judge_instance in instance.judge_models]
                )) for instance in competition_instances
            ])
            .has_next_page(pagination.page + 1 < competition_get_all_builder.attr_total_pages())
            .build()
        )

    def create_competition(self, competition: CompetitionAddDTO) -> str:
        dict_competition = dict(competition)
        del dict_competition['judges_ids']
        competition_id = self._repository.create(dict_competition)

        for judge_id in competition.judges_ids:
            if self._judge_repository.get_by_id(id_arg=judge_id) is None:
                raise Exception(f'Entity with {judge_id} does not exist')

            self._judge_competition_repository.create(dict(JudgeCompetitionAddDTO(
                competition_id=str(competition_id),
                judge_id=judge_id
            )))

        return competition_id

    def get_competition(self, id_arg: str) -> CompetitionDTO:
        competition_instance = self._repository.get_by_id(id_arg=id_arg)

        if competition_instance is None:
            raise Exception('No entities with provided id')

        return CompetitionDTO(
            id=str(competition_instance.id),
            result=competition_instance.result,
            date=competition_instance.date,
            stadium_id=str(competition_instance.stadium_id),
            sport_id=str(competition_instance.sport_id),
            judges_ids=[str(judge_instance.id) for judge_instance in competition_instance.judge_models]
        )

    def delete_competition(self, id_arg: str | None) -> str:
        return self._repository.delete_by_id(id_arg)

    def update_competition(self, id_arg: str | None,
                           competition: CompetitionEditDTO | CompetitionPartialEditDTO) -> str:
        return self._repository.update(id_arg=id_arg, data=dict(competition))
