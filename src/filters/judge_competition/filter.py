from src.SQLAlchemy.filter import SQLAlchemyFilter
from src.models.model_to_model.judge_competition.model import JudgeCompetitionModel


class JudgeCompetitionFilter(SQLAlchemyFilter[JudgeCompetitionModel]):
    _model = JudgeCompetitionModel

