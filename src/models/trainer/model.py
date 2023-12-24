from typing import Optional, List
from sqlalchemy import text, UUID, String
from sqlalchemy.orm import mapped_column, Mapped, relationship
from src.SQLAlchemy.base import Base


class TrainerModel(Base):
    __tablename__ = 'trainer'

    id: Mapped[Optional[str]] = mapped_column(UUID, primary_key=True, server_default=text("gen_random_uuid()"))
    name: Mapped[str] = mapped_column(String(100))
    surname: Mapped[str] = mapped_column(String(100))
    patronymic: Mapped[str] = mapped_column(String(100))
    athlete_models: Mapped[List['AthleteModel']] = relationship()
