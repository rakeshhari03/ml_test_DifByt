from fastapi import FastAPI,Depends

from contextlib import asynccontextmanager
from app.database import base,engine, get_db
from pydantic import BaseModel
from typing import Annotated
from sqlalchemy.orm import Session
from app.models import Forms

class Creating(BaseModel):
    name:str
    email:str
    message:str

@asynccontextmanager
def lifespan(app:FastAPI):
    base.metadata.create_all(engine)
    yield

app=FastAPI(title="form app",lifespan=lifespan)

@app.post("/create")
def create_user(
    userdata: Creating,
    db: Annotated[Session, Depends(get_db)],
):
    new_user = Forms(
        name=userdata.name,
        email=str(userdata.email),
        message=userdata.message,
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "message": "New user created successfully",
        "id": new_user.id,
    }


