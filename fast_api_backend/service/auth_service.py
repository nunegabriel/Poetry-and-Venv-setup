from fastapi import HTTPException
from typing import List

from passlib.context import CryptContext
from schemas.user_schema import LoginSchema,ChangePasswordSchema
from auth.auth_repo import JWTRepo
from controller.auth_controller import UsersRepository


# Encrypt password
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class AuthService:
    @staticmethod
    def logins_service(user: LoginSchema):
        _user= UsersRepository.find_by_email(user.email)

        if _user is not None:
                if not pwd_context.verify(user.password, _user.hashed_password):
                    raise HTTPException(
                        status_code=400, detail="Invalid Password !")
                return JWTRepo(data={"email": _user.email}).generate_token()
        raise HTTPException(status_code=404, detail="Email not found !")
    

    @staticmethod
    def change_password_service(change_password: ChangePasswordSchema):
        _email = UsersRepository.find_by_email(change_password.email)
        if _email is None:
            raise HTTPException(status_code=404, detail="Email not found !")
        UsersRepository.change_password(change_password.email, pwd_context.hash(change_password.new_password))


    
