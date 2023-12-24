from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.SQLAlchemy.base import Base


class AthleteCompetitionModel(Base):
    __tablename__ = 'athlete_competition'

    athlete_id: Mapped[str] = mapped_column(
        ForeignKey('athlete.id'),
        primary_key=True
    )

    competition_id: Mapped[str] = mapped_column(
        ForeignKey('competition.id'),
        primary_key=True
    )
