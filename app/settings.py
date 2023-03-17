# from fastapi import FastAPI
from pydantic import BaseSettings


class Settings(BaseSettings):
    # app_name: str = "Awesome API"
    # admin_email: str
    # items_per_user: int = 50
    # id: int
    db_name: str = "testing"
    db_user: str = "postgres"
    db_host: str = "localhost"
    db_port: int = "5432"