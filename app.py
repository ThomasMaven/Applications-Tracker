from flask import Flask, request, jsonify
import db.database
from app_utils import AppUtils
from config import Config
from model.skill import Skill
from model.skill_schema import SkillSchema
from model.user import User
from model.user_schema import UserSchema

app = Flask(__name__)
app.route = AppUtils.prefix_route(app.route, Config.API_PREFIX)

db_session = db.database.init_db()

user_schema = UserSchema(many=False)
users_schema = UserSchema(many=True)

skill_schema = SkillSchema(many=False)
skills_schema = SkillSchema(many=True)


@app.route('/', methods=['GET'])
def get():
    return jsonify({'msg': 'It works'})


@app.route("/user", methods=['GET'])
def get_users():
    all_users = User.query.all()
    return users_schema.jsonify(all_users)


@app.route("/user", methods=['POST'])
def create_user():
    last_name = request.json['last_name']
    first_name = request.json['first_name']
    cv_url = request.json['cv_url']

    new_user = User(last_name, first_name, cv_url)
    db_session.add(new_user)
    db_session.commit()
    return user_schema.jsonify(new_user)


@app.route("/user/<id>", methods=['PUT'])
def update_user(id):
    user = User.query.get(id)

    last_name = request.json['last_name']
    first_name = request.json['first_name']
    cv_url = request.json['cv_url']

    user.first_name = first_name
    user.last_name = last_name
    user.cv_url = cv_url

    db_session.commit()

    return user_schema.jsonify(user)


@app.route("/user/<id>", methods=['DELETE'])
def delete_user(id):
    user = User.query.get(id)

    db_session.delete(user)
    db_session.commit()

    return user_schema.jsonify(user)


@app.route("/skill", methods=['GET'])
def get_skill():
    all_skills = Skill.query.all()
    return skills_schema.jsonify(all_skills)


@app.route("/skill", methods=['POST'])
def create_skill():
    name = request.json['name']

    new_skill = Skill(name)
    db_session.add(new_skill)
    db_session.commit()
    return skill_schema.jsonify(new_skill)


@app.route("/skill/<id>", methods=['PUT'])
def update_skill(id):
    skill = Skill.query.get(id)
    skill.name = request.json['name']
    db_session.commit()

    return user_schema.jsonify(skill)


@app.route("/skill/<id>", methods=['DELETE'])
def delete_skill(id):
    skill = Skill.query.get(id)

    db_session.delete(skill)
    db_session.commit()

    return user_schema.jsonify(skill)

if __name__ == '__main__':
    app.run(debug=True)
