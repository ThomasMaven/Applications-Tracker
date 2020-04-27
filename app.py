from flask import Flask, request, jsonify
import db.database
from app_utils import AppUtils
from config import Config
from model.user import User
from model.user_schema import UserSchema

app = Flask(__name__)
app.route = AppUtils.prefix_route(app.route, Config.API_PREFIX)

db_session = db.database.init_db()

user_schema = UserSchema(many=False)
users_schema = UserSchema(many=True)


@app.route('/', methods=['GET'])
def get():
    return jsonify({'msg': 'It works'})


@app.route("/user", methods=['GET'])
def get_users():
    all_users = User.query.all()
    return users_schema.jsonify(all_users)


@app.route("/user", methods=['POST'])
def create_user():
    last_name = request.json['last_name'],
    first_name = request.json['first_name'],
    cv_url = request.json['cv_url'],

    new_user = User(last_name, first_name, cv_url)
    db_session.add(new_user)
    db_session.commit()
    return user_schema.jsonify(new_user)


if __name__ == '__main__':
    app.run(debug=True)
