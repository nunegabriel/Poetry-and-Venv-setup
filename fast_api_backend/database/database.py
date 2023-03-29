from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from core import configuration
from models import model

DATABASE_NAME = configuration.Settings().database_name
DATABASE_USER = configuration.Settings().database_user
DATABASE_PASSWORD = configuration.Settings().database_password

engine = create_engine(
    f"postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@localhost/{DATABASE_NAME}",
    echo=True,
)
SessionLocal = sessionmaker(bind=engine)
model.Base.metadata.create_all(bind=engine)

# Dependency
db = SessionLocal()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
