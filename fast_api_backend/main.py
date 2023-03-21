from fastapi import FastAPI
from view import user_router
from view import authentication_router
import uvicorn


def init_app():
    app = FastAPI()

    app.include_router(user_router.router)
    app.include_router(authentication_router.router)
    return app

app = init_app()

# def start():
#     """Launch with 'poetry run start' at root level """
#     uvicorn.run("main:app", host="localhost", port=8000, reload=True)