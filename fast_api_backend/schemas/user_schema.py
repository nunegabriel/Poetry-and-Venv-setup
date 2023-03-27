from typing import Optional, TypeVar

from pydantic import BaseModel

T = TypeVar("T")


class UserBase(BaseModel):
    first_name: str
    last_name: str
    email: str


class LoginSchema(BaseModel):
    email: str
    password: str


class ChangePasswordSchema(BaseModel):
    email: str
    new_password: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True


class UserUpdate(UserBase):
    email: str = None


class ResponseSchema(BaseModel):
    detail: str
    result: Optional[T] = None
