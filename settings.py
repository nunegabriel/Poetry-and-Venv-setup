# from fastapi import FastAPI
from pydantic import BaseSettings


class Settings(BaseSettings):
    # app_name: str = "Awesome API"
    # admin_email: str
    # items_per_user: int = 50
    # id: int
    name: str
    event: str
