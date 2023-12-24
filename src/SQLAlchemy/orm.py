from src.SQLAlchemy.base import Base
from src.SQLAlchemy.connection import PostgreAlchemyConnection
from src.utils.classes.config import Config
from src.utils.decorators.singleton import singleton


@singleton
class PostgreAlchemyORM:
    def __init__(self):
        self._session_maker = PostgreAlchemyConnection(Config()).session_maker
        self._engine = PostgreAlchemyConnection(Config()).engine

    def create_database(self):
        import src.models
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)

