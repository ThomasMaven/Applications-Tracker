from sqlalchemy import Column, Integer, String
from db.database import Base


class Skill(Base):
    __tablename__ = 'skill'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)

    def __init__(self, name=None):
        self.name = name
