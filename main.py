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

@app.get("/")
def home():
    return {"message": "SkillStack API running"}

# CREATE
@app.post("/skills", response_model=SkillSchema)
def create_skill(data:SkillSchema, db: Session = Depends(get_db)):
    skill = Skill(**data.model_dump())
    db.add(skill)
    db.commit()
    db.refresh(skill)
    return skill

# GET ALL
@app.get("/skills", response_model=List[SkillSchema])
def get_skill(db: Session = Depends(get_db)):
    return db.query(Skill).all()

# UPDATE
@app.put("/skills/{skill_id}", response_model=SkillSchema)
def update_skill(skill_id:int, data:SkillSchema, db: Session = Depends(get_db)):
    skill = db.query(Skill).filter(Skill.id == skill_id).first()
    for key, value in data.model_dump().items():
        setattr(skill, key, value)
    db.commit()
    db.refresh(skill)
    return skill

# DELETE
@app.delete("/skills/{skill_id}")
def delete_skill(skill_id: int, db: Session = Depends(get_db)):
    skill = db.query(Skill).filter(Skill.id == skill_id).first()
    db.delete(skill)
    db.commit()
    return {"message": "Skill Deleted"}