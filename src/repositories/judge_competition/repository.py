from sqlalchemy import insert
from sqlalchemy.orm import Session

from src.SQLAlchemy.repository import SQLAlchemyRepository
from src.filters.judge_competition.filter import JudgeCompetitionFilter
from src.models.model_to_model.judge_competition.model import JudgeCompetitionModel
from src.utils.decorators.singleton import singleton


@singleton
class JudgeCompetitionRepository(SQLAlchemyRepository[JudgeCompetitionModel, JudgeCompetitionFilter]):
    _model = JudgeCompetitionModel

    def create(self, data):
        session: Session = self._session_maker()
        statement = insert(self._model).values(**data).returning(self._model.judge_id)
        query_result = session.execute(statement)
        session.commit()
        result = query_result.scalar_one()
        return result
