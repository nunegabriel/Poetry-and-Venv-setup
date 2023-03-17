from fastapi import  FastAPI
from controller import users


def init_app():
    app = FastAPI()

    app.include_router(users.router)
    
    return app
app = init_app()