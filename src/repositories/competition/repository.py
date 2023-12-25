from src.SQLAlchemy.repository import SQLAlchemyRepository
from src.filters.competition.filter import CompetitionFilter
from src.models.competition.model import CompetitionModel
from src.utils.decorators.singleton import singleton


@singleton
class CompetitionRepository(SQLAlchemyRepository[CompetitionModel, CompetitionFilter]):
    _model = CompetitionModel

