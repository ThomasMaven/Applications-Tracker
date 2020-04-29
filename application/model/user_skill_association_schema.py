from marshmallow import fields

from application.app import ma
from application.model.skill_schema import SkillSchema


class UserSkillAssociationSchema(ma.Schema):
    skill = fields.Nested(SkillSchema)

    class Meta:
        fields = ('user_id', 'skill', 'level')
