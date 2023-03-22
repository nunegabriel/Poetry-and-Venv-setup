from fastapi import APIRouter,Depends
from schemas.user_schema import ResponseSchema, LoginSchema, ChangePasswordSchema
from service.auth_service import AuthService
from auth.auth_repo import JWTBearer


router = APIRouter(
    prefix="/api/v1/users/auth",
    tags=['User Authentication'],

)



@router.post("/login", response_model=ResponseSchema)
def login(user: LoginSchema):
    token = AuthService.logins_service(user)
    return ResponseSchema(detail="Login Successful", result={"token_type": "Bearer", "access_token": token})


@router.patch("/change_password", response_model=ResponseSchema,dependencies=[Depends(JWTBearer())])
def change_password(user: ChangePasswordSchema):
    AuthService.change_password_service(user)
    return ResponseSchema(detail="Successfully changed password!")
