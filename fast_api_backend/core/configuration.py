from pydantic import BaseSettings


class Settings(BaseSettings):
    database_name: str
    database_user: str
    database_password: str
    secret_key: str
    algorithm: str

    class Config:
        env_file = ".env"
