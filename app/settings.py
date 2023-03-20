# from fastapi import FastAPI
from pydantic import BaseSettings


class Settings(BaseSettings):
    database_name: str
    database_user: str
    database_password: str
    database_type: str
    database_port: str

    class Config:
        env_file = ".env"