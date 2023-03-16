import psycopg2
from fastapi import FastAPI
from pathlib import Path

from fastapi import FastAPI
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


from dotenv import load_dotenv
import os

env_path = Path('.', '.env')
load_dotenv(dotenv_path=env_path)

load_dotenv()

DATABASE_NAME = os.getenv("DATABASE_NAME")
DATABASE_USER = os.getenv("DATABASE_USER")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")


# SQLAlchemy engine to connect to your PostgreSQL database
SQLALCHEMY_DATABASE_URL = f"postgresql://postgres:{DATABASE_PASSWORD}@localhost/{DATABASE_NAME}"
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# SQLAlchemy session to interact with the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()