from abc import ABC
from typing import Generic, TypeVar
from sqlalchemy import select, insert, delete, update, func
from sqlalchemy.orm import Session
from src.SQLAlchemy.connection import PostgreAlchemyConnection
from src.utils.classes.abstract_repository import AbstractRepository
from src.utils.classes.config import Config

Model = TypeVar('Model')
Filter = TypeVar('Filter')


class SQLAlchemyRepository(Generic[Model, Filter], AbstractRepository[Model, Filter], ABC):
    _model: Model = None
    _session_maker = PostgreAlchemyConnection(Config()).session_maker

    def total_elements(self, filter_instance: Filter):
        session: Session = self._session_maker()
        statement = filter_instance.filter(
            select(func.count())
            .select_from(self._model)
        )
        query_result = session.execute(statement)
        result = query_result.scalar()
        return result

    def get_all(self, filter_instance: Filter, page: int, per_page: int):
        session: Session = self._session_maker()
        statement = filter_instance.filter(
            select(self._model)
            .offset(page * per_page)
            .limit(per_page)
        )
        query_result = session.execute(statement)
        result = [item[0] for item in query_result.all()]
        return result

    def get_by_id(self, id_arg: str):
        session: Session = self._session_maker()
        statement = select(self._model).where(self._model.id == id_arg)
        query_result = session.execute(statement)
        result = query_result.first()
        if result is None:
            return None
        else:
            result: Model = result[0]
            return result

    def create(self, data):
        session: Session = self._session_maker()
        statement = insert(self._model).values(**data).returning(self._model.id)
        query_result = session.execute(statement)
        session.commit()
        result = query_result.scalar_one()
        return result

    def update(self, id_arg, data):
        session: Session = self._session_maker()
        statement = (
            update(self._model)
            .where(self._model.id == id_arg)
            .values(**data)
            .returning(self._model.id)
        )
        query_result = session.execute(statement)
        session.commit()
        result = query_result.scalar_one()
        return result

    def delete_by_id(self, id_arg):
        session: Session = self._session_maker()
        statement = delete(self._model).where(self._model.id == id_arg).returning(self._model.id)
        query_result = session.execute(statement)
        session.commit()
        result = query_result.scalar_one()
        return result
