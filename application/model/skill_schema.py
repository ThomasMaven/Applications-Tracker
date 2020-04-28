from application.app import ma


class SkillSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name')
