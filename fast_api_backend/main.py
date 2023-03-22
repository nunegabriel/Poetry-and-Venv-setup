from fastapi import FastAPI
from view import user_router
from view import authentication_router


def init_app():
    app = FastAPI()

    app.include_router(user_router.router)
    app.include_router(authentication_router.router)
    return app

app = init_app()
