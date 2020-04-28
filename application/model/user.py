from sqlalchemy.orm import relationship

from application.app import db


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    last_name = db.Column(db.String(100), nullable=False)
    first_name = db.Column(db.String(100), nullable=False)
    cv_url = db.Column(db.String(255))
    skill = relationship("UserSkillAssociation", back_populates="user")

    def __repr__(self):
        return f"{self.first_name} {self.last_name}. CV: {self.cv_url}"
