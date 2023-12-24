from src.SQLAlchemy.repository import SQLAlchemyRepository
from src.filters.judge.filter import JudgeFilter
from src.models.judge.model import JudgeModel
from src.utils.decorators.singleton import singleton


@singleton
class JudgeRepository(SQLAlchemyRepository[JudgeModel, JudgeFilter]):
    _model = JudgeModel

