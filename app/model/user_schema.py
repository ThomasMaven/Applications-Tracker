from flask_marshmallow import Marshmallow


class UserSchema(Marshmallow().Schema):
    class Meta:
        fields = ('id', 'first_name', 'last_name', 'cv_url')