from sqlalchemy import Column, Integer, String, Text
from database import Base

class Skill(Base):

    __tablename__ = "skills"

    id = Column(Integer, primary_key=True, index=True)
    skill_name = Column(String(100))
    resource_type = Column(String(50))
    platform = Column(String(50))
    status = Column(String(50))
    hours = Column(Integer)
    notes = Column(Text)
    difficulty = Column(Integer)