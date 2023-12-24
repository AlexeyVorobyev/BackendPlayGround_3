from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.SQLAlchemy.base import Base


class JudgeCompetitionModel(Base):
    __tablename__ = 'judge_competition'

    judge_id: Mapped[str] = mapped_column(
        ForeignKey('judge.id'),
        primary_key=True
    )

    competition_id: Mapped[str] = mapped_column(
        ForeignKey('competition.id'),
        primary_key=True
    )