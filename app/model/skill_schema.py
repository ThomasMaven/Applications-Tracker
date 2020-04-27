from flask_marshmallow import Marshmallow


class SkillSchema(Marshmallow().Schema):
    class Meta:
        fields = ('id', 'name')
