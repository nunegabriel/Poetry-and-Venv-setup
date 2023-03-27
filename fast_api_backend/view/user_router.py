from typing import List

from fastapi import APIRouter, Depends, HTTPException, Security
from fastapi.security import HTTPAuthorizationCredentials
from sqlalchemy.orm import Session

from auth.auth_repo import JWTBearer, JWTRepo
from controller import user_controller
from database import get_db
from schemas import user_schema
from schemas.user_schema import ResponseSchema

router = APIRouter(
    prefix="/api/v1/users/account",
    tags=["User Account Management"],
)


@router.post("/", response_model=user_schema.User)
def create_user(user: user_schema.UserCreate, db: Session = Depends(get_db)):
    db_user = user_controller.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return user_controller.create_user(db=get_db, user=user)


@router.get("/", response_model=List[user_schema.User])
def view_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = user_controller.get_users(db, skip=skip, limit=limit)
    return users


@router.get("/{user_id}", response_model=user_schema.User)
def view_user(user_id: int, db: Session = Depends(get_db)):
    db_user = user_controller.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.delete(
    "/delete/{user_id}",
    response_model=ResponseSchema,
    dependencies=[Depends(JWTBearer())],
)
def delete_user(
    user_id: int,
    db: Session = Depends(get_db),
    credentials: HTTPAuthorizationCredentials = Security(JWTBearer()),
):
    JWTRepo.extract_token(credentials)
    db_user_to_delete = user_controller.delete_user(db, user_id)
    if db_user_to_delete is None:
        raise HTTPException(status_code=404, detail="User not found")
    return ResponseSchema(detail="User details deleted!")


@router.patch(
    "/{user_id}", response_model=ResponseSchema, dependencies=[Depends(JWTBearer())]
)
def update_user(
    user: user_schema.UserUpdate, user_id: int, db: Session = Depends(get_db)
):
    db_user_to_update = user_controller.update_user(db, user_id, user=user)
    if not db_user_to_update:
        raise HTTPException(status_code=404, detail="User not found")
    return ResponseSchema(detail="User details updated!")
