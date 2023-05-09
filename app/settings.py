from pydantic import BaseSettings

class Settings(BaseSettings):
    database_name: str
    database_user: str
    database_password: str
    # reminder: redis server config
    redis_server: str
    redis_port: int
    redis_password: str
    
    class Config:
        env_file = ".env"
