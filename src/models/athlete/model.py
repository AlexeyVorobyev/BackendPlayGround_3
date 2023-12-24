from typing import Optional, List
from sqlalchemy import text, UUID, String, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import ENUM
from sqlalchemy.orm import mapped_column, Mapped, relationship
from src.SQLAlchemy.base import Base
from src.models.sport.model import SportModel
from src.models.trainer.model import TrainerModel

genders = ('Male', 'Female')

gender_enum = ENUM(*genders, name='gender')


class AthleteModel(Base):
    __tablename__ = 'athlete'

    id: Mapped[Optional[str]] = mapped_column(UUID, primary_key=True, server_default=text("gen_random_uuid()"))
    name: Mapped[str] = mapped_column(String(100))
    surname: Mapped[str] = mapped_column(String(100))
    patronymic: Mapped[str] = mapped_column(String(100))
    date_of_birth: Mapped[str] = mapped_column(DateTime)
    gender: Mapped[gender_enum] = mapped_column(gender_enum)

    trainer_id: Mapped[str] = mapped_column(ForeignKey('trainer.id'))
    trainer_model: Mapped[TrainerModel] = relationship()

    sport_models: Mapped[List[SportModel]] = relationship(
        secondary='athlete_sport'
    )

    athlete_models: Mapped[List["AthleteModel"]] = relationship(
        secondary='athlete_competition'
    )
