import os
from dotenv import load_dotenv
from src.utils.decorators.singleton import singleton


@singleton
class Config:
    def __init__(self):
        load_dotenv()
        self.db_pg_user = os.environ.get('DB_PG_USER') or 'postgres'
        self.db_pg_password = os.environ.get('DB_PG_PASSWORD') or 'admin'
        self.db_pg_host = os.environ.get('DB_PG_HOST') or 'localhost'
        self.db_pg_port = os.environ.get('DB_PG_PORT') or '5432'
        self.db_pg_name = os.environ.get('DB_PG_NAME') or 'pythonPlayground'
