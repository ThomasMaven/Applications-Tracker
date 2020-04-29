from marshmallow import fields

from application.app import ma
from application.model.skill_schema import SkillSchema


class UserSchema(ma.Schema):
    # id = fields.String()
    # first_name = fields.String()
    # last_name = fields.String()
    skills = fields.Nested(SkillSchema, many=True)
    class Meta:
        fields = ('id', 'first_name', 'last_name', 'cv_url', "skills")
