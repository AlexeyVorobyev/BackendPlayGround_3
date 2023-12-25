import math
from typing import Any
from src.dtos.stadium.dto import (
    StadiumGetAllDTO,
    StadiumGetAllDTOBuilder,
    StadiumDTO,
    StadiumAddDTO,
    StadiumEditDTO,
    StadiumPartialEditDTO
)
from src.dtos.pagination.dto import PaginationDTO
from src.filters.stadium.filter import StadiumFilter
from src.repositories.stadium.repository import StadiumRepository
from src.utils.decorators.singleton import singleton
from src.utils.functions.clear_dict_from_none import clear_dict_from_none


@singleton
class StadiumService:
    _repository = StadiumRepository()

    def get_stadiums(self, page, per_page, simple_filter) -> StadiumGetAllDTO:
        pagination = PaginationDTO(**clear_dict_from_none(dict(page=page, per_page=per_page)))
        stadium_filter_instance = StadiumFilter({
            'simple_filter': {
                'name': simple_filter,
                'address': simple_filter,
                'seats': simple_filter
            }
        })

        stadium_instances = self._repository.get_all(
            page=pagination.page,
            per_page=pagination.per_page,
            filter_instance=stadium_filter_instance
        )

        stadium_get_all_builder: Any = StadiumGetAllDTOBuilder()

        return (
            stadium_get_all_builder
            .total_elements(self._repository.total_elements(filter_instance=stadium_filter_instance))
            .total_pages(math.ceil(stadium_get_all_builder.attr_total_elements() / pagination.per_page))
            .current_page(pagination.page)
            .data([
                dict(StadiumDTO(
                    id=str(instance.id),
                    name=instance.name,
                    address=instance.address,
                    seats=instance.seats
                )) for instance in stadium_instances
            ])
            .has_next_page(pagination.page + 1 < stadium_get_all_builder.attr_total_pages())
            .build()
        )

    def create_stadium(self, stadium: StadiumAddDTO) -> str:
        return self._repository.create(dict(stadium))

    def get_stadium(self, id_arg: str) -> StadiumDTO:
        stadium_instance = self._repository.get_by_id(id_arg=id_arg)

        if stadium_instance is None:
            raise Exception('No entities with provided id')

        return StadiumDTO(
            id=str(stadium_instance.id),
            name=stadium_instance.name,
            address=stadium_instance.address,
            seats=stadium_instance.seats
        )

    def delete_stadium(self, id_arg: str | None) -> str:
        return self._repository.delete_by_id(id_arg)

    def update_stadium(self, id_arg: str | None, stadium: StadiumEditDTO | StadiumPartialEditDTO) -> str:
        return self._repository.update(id_arg=id_arg, data=dict(stadium))
