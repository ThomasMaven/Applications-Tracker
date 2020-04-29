from sqlalchemy.orm import relationship

from application.app import db
import application.model.user_skill_association


class DbUser(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    last_name = db.Column(db.String(100), nullable=False)
    first_name = db.Column(db.String(100), nullable=False)
    cv_url = db.Column(db.String(255))
    skill = relationship("DbUserSkillAssociation", back_populates="user", lazy='joined')

    def __repr__(self):
        return f"{self.first_name} {self.last_name}. CV: {self.cv_url}"
