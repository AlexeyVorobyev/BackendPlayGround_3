from abc import abstractmethod, ABC
import sqlalchemy
from sqlalchemy import Engine
from sqlalchemy.orm import sessionmaker, Session
from src.utils.decorators.singleton import singleton


class AlchemyConnection(ABC):
    @abstractmethod
    def __init__(self, config_arg):
        pass

@singleton
class PostgreAlchemyConnection(AlchemyConnection):
    def __init__(self, config_arg):
        self._url = f'postgresql://{config_arg.db_pg_user}:{config_arg.db_pg_password}@{config_arg.db_pg_host}:{config_arg.db_pg_port}/{config_arg.db_pg_name}'
        self._engine = sqlalchemy.create_engine(
            url=self._url,
            echo=False
        )
        self._session_maker = sessionmaker(self._engine)

    @property
    def engine(self):
        return self._engine

    @property
    def session_maker(self):
        return self._session_maker
