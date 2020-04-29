from marshmallow import fields

from application.app import ma
from application.model.skill_schema import SkillSchema


class UserSchema(ma.Schema):
    skills = fields.Nested(SkillSchema, many=True)

    class Meta:
        fields = ('id', 'first_name', 'last_name', 'cv_url', "skills")
