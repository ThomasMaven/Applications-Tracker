from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from application.app import db


class DbUserSkillAssociation(db.Model):
    __tablename__ = 'user_skill_association'
    user_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    skill_id = Column(Integer, ForeignKey('skill.id'), primary_key=True)
    level = Column(Integer)
    skill = relationship('DbSkill', back_populates='user')
    user = relationship('DbUser', back_populates='skill')
