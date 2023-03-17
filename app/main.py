from fastapi import FastAPI
from view import ticket_router

def init_app():
    app = FastAPI()
    app.include_router(ticket_router.router)

    return app
app = init_app()
