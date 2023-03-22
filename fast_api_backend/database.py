from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import model
from configuration import Settings


DATABASE_NAME = Settings().database_name
DATABASE_USER = Settings().database_user
DATABASE_PASSWORD = Settings().database_password

engine = create_engine(f'postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@localhost/{DATABASE_NAME}',
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






