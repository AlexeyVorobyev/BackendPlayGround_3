from typing import Optional, List
from sqlalchemy import text, UUID, String
from sqlalchemy.orm import mapped_column, Mapped, relationship
from src.SQLAlchemy.base import Base


class SportModel(Base):
    __tablename__ = 'sport'

    id: Mapped[Optional[str]] = mapped_column(UUID, primary_key=True, server_default=text("gen_random_uuid()"))
    name: Mapped[str] = mapped_column(String(100))
    competition_models: Mapped[List["CompetitionModel"]] = relationship()

    athlete_models: Mapped[List["AthleteModel"]] = relationship(
        secondary='athlete_sport'
    )

