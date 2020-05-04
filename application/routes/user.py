import typing
from flask import jsonify, request, Response
from sqlalchemy.orm import joinedload

from application import s3_transfer
from application.app import db
from application.model.skill import DbSkill
from application.model.skill_schema import SkillSchema
from application.model.user import DbUser
from application.model.user_schema import UserSchema
from flask import current_app as app

from application.model.user_skill_association import DbUserSkillAssociation


user_schema = UserSchema(many=False)
users_schema = UserSchema(many=True)

skill_schema = SkillSchema(many=False)
skills_schema = SkillSchema(many=True)


@app.route('/', methods=['GET'])
def get() -> str:
    return jsonify({'msg': 'It works'})


@app.route('/users', methods=['GET'])
def get_users() -> Response:
    all_users = DbUser.query.options(joinedload('skill')).all()
    return users_schema.jsonify(all_users)


@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id: str) -> Response:
    user = DbUser.query.options(joinedload('skill')).get(user_id)
    if user is None:
        return user_schema.jsonify(user), 404
    return user_schema.jsonify(user)


@app.route('/users', methods=['POST'])
def create_user() -> typing.Tuple[Response, int]:
    last_name = request.json['last_name']
    first_name = request.json['first_name']
    cv_url = request.json['cv_url']
    cv_url = s3_transfer.upload_file_to_s3(cv_url)

    new_user = DbUser(last_name=last_name, first_name=first_name, cv_url=cv_url)
    db.session.add(new_user)

    skill_list = []
    for key in request.json['skills']:
        skill = db.session.query(DbSkill).filter_by(name=key).first()
        if skill is None:
            skill = DbSkill(name=key)
            db.session.add(skill)

        skill_list.append(
            DbUserSkillAssociation(user=new_user, skill=skill, level=request.json['skills'][key]))
    new_user.skill = skill_list
    db.session.add(new_user)
    db.session.commit()

    return user_schema.jsonify(new_user), 201


@app.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id: str) -> typing.Tuple[str, int]:
    user = DbUser.query.get(user_id)
    if user is None:
        return '', 404
    s3_transfer.remove_file_from_s3(user.cv_url)
    db.session.delete(user)
    db.session.commit()

    return '', 204
