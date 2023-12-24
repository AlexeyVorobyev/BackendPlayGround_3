from typing import Optional, List
from sqlalchemy import text, UUID, String, DateTime, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship
from src.SQLAlchemy.base import Base
from src.models.athlete.model import AthleteModel
from src.models.sport.model import SportModel
from src.models.stadium.model import StadiumModel


class CompetitionModel(Base):
    __tablename__ = 'competition'

    id: Mapped[Optional[str]] = mapped_column(UUID, primary_key=True, server_default=text("gen_random_uuid()"))
    result: Mapped[str] = mapped_column(String(1000))
    date: Mapped[str] = mapped_column(DateTime)

    stadium_id: Mapped[str] = mapped_column(ForeignKey('stadium.id'))
    stadium_model: Mapped[StadiumModel] = relationship()

    sport_id: Mapped[str] = mapped_column(ForeignKey('sport.id'))
    sport_model: Mapped[SportModel] = relationship()

    judge_models: Mapped[List["JudgeModel"]] = relationship(
        secondary='judge_competition'
    )

    athlete_models: Mapped[List[AthleteModel]] = relationship(
        secondary='athlete_competition'
    )