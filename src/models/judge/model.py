from typing import Optional, List
from sqlalchemy import text, UUID, String
from sqlalchemy.orm import mapped_column, Mapped, relationship

from src.models.competition.model import CompetitionModel
from src.models.model_to_model.judge_competition.model import JudgeCompetitionModel
from src.SQLAlchemy.base import Base


class JudgeModel(Base):
    __tablename__ = 'judge'

    id: Mapped[Optional[str]] = mapped_column(UUID, primary_key=True, server_default=text("gen_random_uuid()"))
    name: Mapped[str] = mapped_column(String(100))
    surname: Mapped[str] = mapped_column(String(100))
    patronymic: Mapped[str] = mapped_column(String(100))

    competitions_models: Mapped[List[CompetitionModel]] = relationship(
        secondary='judge_competition'
    )
