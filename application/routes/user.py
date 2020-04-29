from flask import jsonify, request

from application.app import db
from application.model.skill_schema import SkillSchema
from application.model.user import DbUser
from application.model.user_schema import UserSchema
from flask import current_app as app

user_schema = UserSchema(many=False)
users_schema = UserSchema(many=True)

skill_schema = SkillSchema(many=False)
skills_schema = SkillSchema(many=True)


@app.route('/', methods=['GET'])
def get():
    return jsonify({'msg': 'It works'})


@app.route("/users", methods=['GET'])
def get_users():
    all_users = DbUser.query.all()
    return users_schema.jsonify(all_users)


@app.route("/users/<id>", methods=['GET'])
def get_user(id):
    user = DbUser.query.get(id)
    if user is None:
        return user_schema.jsonify(user), "404"
    return user_schema.jsonify(user)


@app.route("/users", methods=['POST'])
def create_user():
    last_name = request.json['last_name']
    first_name = request.json['first_name']
    cv_url = request.json['cv_url']
    skills = request.json['skills']
    new_user = DbUser(last_name=last_name, first_name=first_name, cv_url=cv_url)
    db.session.add(new_user)
    db.session.commit()
    return user_schema.jsonify(new_user), "201"


@app.route("/users/<id>", methods=['PUT'])
def update_user(id):
    user = DbUser.query.get(id)
    if user is None:
        return user_schema.jsonify(user), "404"
    last_name = request.json['last_name']
    first_name = request.json['first_name']
    cv_url = request.json['cv_url']

    user.first_name = first_name
    user.last_name = last_name
    user.cv_url = cv_url

    db.session.commit()

    return user_schema.jsonify(user)


@app.route("/users/<id>", methods=['DELETE'])
def delete_user(id):
    user = DbUser.query.get(id)
    if user is None:
        return user_schema.jsonify(user), "404"
    db.session.delete(user)
    db.session.commit()

    return "", "204"
