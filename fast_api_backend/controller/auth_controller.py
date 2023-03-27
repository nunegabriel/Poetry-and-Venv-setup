from sqlalchemy import update as sql_update
from sqlalchemy.future import select

from database import db
from models.model import User


class UsersRepository:
    @staticmethod
    def find_by_email(email: str):
        query = select(User).where(User.email == email)
        return db.execute(query).scalar_one_or_none()

    @staticmethod
    def change_password(email: str, password: str):
        query = (
            sql_update(User)
            .where(User.email == email)
            .values(hashed_password=password)
            .execution_options(synchronize_session="fetch")
        )
        return db.execute(query)
