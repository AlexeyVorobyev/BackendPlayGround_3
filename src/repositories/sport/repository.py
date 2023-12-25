from src.SQLAlchemy.repository import SQLAlchemyRepository
from src.filters.sport.filter import SportFilter
from src.models.sport.model import SportModel
from src.utils.decorators.singleton import singleton


@singleton
class SportRepository(SQLAlchemyRepository[SportModel, SportFilter]):
    _model = SportModel

