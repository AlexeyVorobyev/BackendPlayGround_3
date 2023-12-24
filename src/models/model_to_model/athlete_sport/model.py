from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.SQLAlchemy.base import Base


class AthleteSportModel(Base):
    __tablename__ = 'athlete_sport'

    athlete_id: Mapped[str] = mapped_column(
        ForeignKey('athlete.id'),
        primary_key=True
    )

    sport_id: Mapped[str] = mapped_column(
        ForeignKey('sport.id'),
        primary_key=True
    )