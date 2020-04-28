from application.app import db


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    last_name = db.Column(db.String(100), nullable=False)
    first_name = db.Column(db.String(100), nullable=False)
    cv_url = db.Column(db.String(255))

    def __init__(self, last_name=None, first_name=None, cv_url=None):
        self.last_name = last_name
        self.first_name = first_name
        self.cv_url = cv_url

    def __repr__(self):
        return f"{self.first_name} {self.last_name}. CV: {self.cv_url}"
