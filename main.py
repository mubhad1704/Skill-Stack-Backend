from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel, ConfigDict
from typing import List

# cors
from fastapi.middleware.cors import CORSMiddleware

from database import SessionLocal, engine
from models import Skill, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

# cors
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# pydantic
class SkillSchema(BaseModel):
    id: int | None = None 
    skill_name: str
    resource_type: str
    platform: str
    status: str
    hours: int
    notes: str
    difficulty: int

    class Config:
        orm_mode = True

@app.get("/")
def home():
    return {"message": "SkillStack API running"}

# CREATE
@app.post("/skills", response_model=SkillSchema)
def create_skill(data:SkillSchema, db: Session = Depends(get_db)):
    skill = Skill(**data.dict(exclude={"id"}))
    db.add(skill)
    db.commit()
    db.refresh(skill)
    return skill

# GET ALL
@app.get("/skills", response_model=List[SkillSchema])
def get_skill(db: Session = Depends(get_db)):
    return db.query(Skill).all()

# GET ONE
@app.get("/skills/{skill_id}", response_model=SkillSchema)
def get_one(skill_id: int, db: Session = Depends(get_db)):
    skill = db.query(Skill).filter(Skill.id == skill_id).first()
    if not skill:
        raise HTTPException(status_code=404, detail="Skill not found")
    return skill

# UPDATE
@app.put("/skills/{skill_id}", response_model=SkillSchema)
def update_skill(skill_id:int, data:SkillSchema, db: Session = Depends(get_db)):
    skill = db.query(Skill).filter(Skill.id == skill_id).first()

    if not skill:
        raise HTTPException(status_code=404, detail="Skill not found")
    
    updates = data.dict(exclude={"id"})
    for key, value in updates.items():
        setattr(skill, key, value)
    db.commit()
    db.refresh(skill)
    return skill

# DELETE
@app.delete("/skills/{skill_id}")
def delete_skill(skill_id: int, db: Session = Depends(get_db)):
    skill = db.query(Skill).filter(Skill.id == skill_id).first()

    if not skill:
        raise HTTPException(status_code=404, detail="Skill not found")

    db.delete(skill)
    db.commit()
    return {"message": "Skill Deleted"}