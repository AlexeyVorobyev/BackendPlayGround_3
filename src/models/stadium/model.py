from typing import Optional, List
from sqlalchemy import text, UUID, String, Integer
from sqlalchemy.orm import mapped_column, Mapped, relationship
from src.SQLAlchemy.base import Base


class StadiumModel(Base):
    __tablename__ = 'stadium'

    id: Mapped[Optional[str]] = mapped_column(UUID, primary_key=True, server_default=text("gen_random_uuid()"))
    name: Mapped[str] = mapped_column(String(100))
    address: Mapped[str] = mapped_column(String(100))
    seats: Mapped[str] = mapped_column(Integer)

    competition_models: Mapped[List['CompetitionModel']] = relationship()
