from fastapi import FastAPI
from view import ticket_router
# from app.services.cache_service import cache
# from app.database import db



app = FastAPI()

app.include_router(ticket_router.router)


