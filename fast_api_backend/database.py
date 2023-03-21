from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from pathlib import Path
from dotenv import load_dotenv
from models import model

env_path = Path('.', '.env')
load_dotenv(dotenv_path=env_path)

DATABASE_NAME = os.getenv("DATABASE_NAME")
DATABASE_USER = os.getenv("DATABASE_USER")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")

engine = create_engine(f"postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@localhost/{DATABASE_NAME}",
                       echo=True
                       )

SessionLocal = sessionmaker(bind=engine)
model.Base.metadata.create_all(bind=engine)

# Dependency
db= SessionLocal()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()






