import psycopg2
from fastapi import FastAPI
from pathlib import Path

from fastapi import FastAPI
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from settings import Settings


from dotenv import load_dotenv
import os

env_path = Path('.', '.env')
load_dotenv(dotenv_path=env_path)

load_dotenv()

settings = Settings()

DATABASE_NAME = settings.database_name
DATABASE_USER = settings.database_user
DATABASE_PASSWORD = settings.database_password

# SQLAlchemy engine to connect to your PostgreSQL database
SQLALCHEMY_DATABASE_URL = f"postgresql://postgres:{DATABASE_PASSWORD}@localhost/{DATABASE_NAME}"
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# SQLAlchemy session to interact with the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()