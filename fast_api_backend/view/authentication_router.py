from fastapi import APIRouter, Depends

from auth.auth_repo import JWTBearer
from schemas.user_schema import (ChangePasswordSchema, LoginSchema,
                                 ResponseSchema)
from service.auth_service import AuthService

router = APIRouter(
    prefix="/api/v1/users/auth",
    tags=["User Authentication"],
)


@router.post("/login", response_model=ResponseSchema)
def login(user: LoginSchema):
    token = AuthService.logins_service(user)
    return ResponseSchema(
        detail="Login Successful",
        result={"token_type": "Bearer", "access_token": token},
    )


@router.patch(
    "/change_password",
    response_model=ResponseSchema,
    dependencies=[Depends(JWTBearer())],
)
def change_password(user: ChangePasswordSchema):
    AuthService.change_password_service(user)
    return ResponseSchema(detail="Successfully changed password!")
