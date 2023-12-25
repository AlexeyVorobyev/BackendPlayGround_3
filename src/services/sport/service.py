import math
from typing import Any
from src.dtos.sport.dto import (
    SportGetAllDTO,
    SportGetAllDTOBuilder,
    SportDTO,
    SportAddDTO,
    SportEditDTO,
    SportPartialEditDTO
)
from src.dtos.pagination.dto import PaginationDTO
from src.filters.sport.filter import SportFilter
from src.repositories.sport.repository import SportRepository
from src.utils.decorators.singleton import singleton
from src.utils.functions.clear_dict_from_none import clear_dict_from_none


@singleton
class SportService:
    _repository = SportRepository()

    def get_sports(self, page, per_page, simple_filter) -> SportGetAllDTO:
        pagination = PaginationDTO(**clear_dict_from_none(dict(page=page, per_page=per_page)))
        sport_filter_instance = SportFilter({
            'simple_filter': {
                'name': simple_filter,
            }
        })

        sport_instances = self._repository.get_all(
            page=pagination.page,
            per_page=pagination.per_page,
            filter_instance=sport_filter_instance
        )

        sport_get_all_builder: Any = SportGetAllDTOBuilder()

        return (
            sport_get_all_builder
            .total_elements(self._repository.total_elements(filter_instance=sport_filter_instance))
            .total_pages(math.ceil(sport_get_all_builder.attr_total_elements() / pagination.per_page))
            .current_page(pagination.page)
            .data([
                dict(SportDTO(
                    id=str(instance.id),
                    name=instance.name,
                )) for instance in sport_instances
            ])
            .has_next_page(pagination.page + 1 < sport_get_all_builder.attr_total_pages())
            .build()
        )

    def create_sport(self, sport: SportAddDTO) -> str:
        return self._repository.create(dict(sport))

    def get_sport(self, id_arg: str) -> SportDTO:
        sport_instance = self._repository.get_by_id(id_arg=id_arg)

        if sport_instance is None:
            raise Exception('No entities with provided id')

        return SportDTO(
            id=str(sport_instance.id),
            name=sport_instance.name,
        )

    def delete_sport(self, id_arg: str | None) -> str:
        return self._repository.delete_by_id(id_arg)

    def update_sport(self, id_arg: str | None, sport: SportEditDTO | SportPartialEditDTO) -> str:
        return self._repository.update(id_arg=id_arg, data=dict(sport))
