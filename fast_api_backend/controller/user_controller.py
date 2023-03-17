from sqlalchemy.orm import Session
from passlib.context import CryptContext
from models import model
from schemas import user_schema

# Hashing password using passlib
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_user(db: Session, user_id: int):
    return db.query(model.User).filter(model.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(model.User).filter(model.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(model.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: user_schema.UserCreate):
    hashed_password = pwd_context.hash(user.password)
    db_user = model.User(
        first_name=user.first_name,last_name=user.last_name,
        email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def delete_user(db: Session, user_id: int):
    db_user_to_delete = db.query(model.User).filter(
        model.User.id == user_id).first()
    db.delete(db_user_to_delete)
    db.commit()
    db.refresh(db_user_to_delete)
    return db_user_to_delete


def update_user(db: Session, user_id: int, user: user_schema.UserCreate):
    db_user_to_update = db.query(model.User).filter(
        model.User.id == user_id).first()
    db_user_to_update = {db_user_to_update.email: user.email,
                         db_user_to_update.hashed_password: pwd_context.hash(user.password)}
    updated_data = db.add(db_user_to_update)
    db.commit()
    return updated_data

