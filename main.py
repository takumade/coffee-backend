from fastapi import FastAPI
from pydantic import BaseModel

from app.routers import users
from app.routers import items

app = FastAPI()

app.include_router(users.router)
app.include_router(items.router)
