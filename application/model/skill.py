from sqlalchemy.orm import relationship

from application.app import db
import application.model.user_skill_association


class DbSkill(db.Model):
    __tablename__ = 'skill'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    user = relationship("DbUserSkillAssociation", back_populates="skill")
