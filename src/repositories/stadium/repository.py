from src.SQLAlchemy.repository import SQLAlchemyRepository
from src.filters.stadium.filter import StadiumFilter
from src.models.stadium.model import StadiumModel
from src.utils.decorators.singleton import singleton


@singleton
class StadiumRepository(SQLAlchemyRepository[StadiumModel, StadiumFilter]):
    _model = StadiumModel

