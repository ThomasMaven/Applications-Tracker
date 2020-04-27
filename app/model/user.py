from sqlalchemy import Column, Integer, String
from db.database import Base


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    last_name = Column(String(100), nullable=False)
    first_name = Column(String(100), nullable=False)
    cv_url = Column(String(255))

    def __init__(self, last_name=None, first_name=None, cv_url=None):
        self.last_name = last_name
        self.first_name = first_name
        self.cv_url = cv_url

    def __repr__(self):
        return f"{self.first_name} {self.last_name}. CV: {self.cv_url}"
