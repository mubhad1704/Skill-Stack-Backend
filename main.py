from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import List

from database import SessionLocal, engine
from models import Skill, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# pydantic
class SkillSchema(BaseModel):
    skill_name = str
    resource_type = str
    platform = str
    status = str
    hours = int
    notes = str
    difficulty = int

    class Config:
        orm_mode=True


