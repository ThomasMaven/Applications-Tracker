from flask import jsonify, request

from application.app import db
from application.model.skill import DbSkill
from application.model.skill_schema import SkillSchema
from application.model.user import DbUser
from application.model.user_schema import UserSchema
from flask import current_app as app

from application.model.user_skill_association import DbUserSkillAssociation
from application.s3_transfer import s3Transfer

user_schema = UserSchema(many=False)
users_schema = UserSchema(many=True)

skill_schema = SkillSchema(many=False)
skills_schema = SkillSchema(many=True)


@app.route('/', methods=['GET'])
def get():
    return jsonify({'msg': 'It works'})


@app.route('/users', methods=['GET'])
def get_users():
    all_users = DbUser.query.all()
    return users_schema.jsonify(all_users)


@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    user = DbUser.query.get(user_id)
    if user is None:
        return user_schema.jsonify(user), 404
    return user_schema.jsonify(user)


@app.route('/users', methods=['POST'])
def create_user():
    last_name = request.json['last_name']
    first_name = request.json['first_name']
    cv_url = request.json['cv_url']
    cv_url = s3Transfer.upload_file_to_s3(cv_url)

    new_user = DbUser(last_name=last_name, first_name=first_name, cv_url=cv_url)
    db.session.add(new_user)
    db.session.commit()

    skill_list = []
    for key in request.json['skills']:
        skill = db.session.query(DbSkill).filter_by(name=key).scalar()
        if skill is not None:
            skill_id = skill.id
        else:
            new_skill = DbSkill(name=key)
            db.session.add(new_skill)
            db.session.commit()
            skill_id = new_skill.id

        skill_list.append(
            DbUserSkillAssociation(user_id=new_user.id, skill_id=skill_id, level=request.json['skills'][key]))
    new_user.skill = skill_list
    db.session.add(new_user)
    db.session.commit()

    return user_schema.jsonify(new_user), 201


@app.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    user = DbUser.query.get(user_id)
    if user is None:
        return user_schema.jsonify(user), 404
    last_name = request.json['last_name']
    first_name = request.json['first_name']
    cv_url = request.json['cv_url']
    cv_url = s3Transfer.upload_file_to_s3(cv_url)

    user.first_name = first_name
    user.last_name = last_name
    user.cv_url = cv_url

    db.session.commit()

    return user_schema.jsonify(user)


@app.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = DbUser.query.get(user_id)
    if user is None:
        return user_schema.jsonify(user), 404
    db.session.delete(user)
    db.session.commit()

    return '', 204
