from fastapi import Depends, FastAPI, status, Response, HTTPException
from . import schemas, models
from .database import engine, get_db
from sqlalchemy.orm import Session
from typing import List
from .routers import blog, user


app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(blog.router)
app.include_router(user.router)
