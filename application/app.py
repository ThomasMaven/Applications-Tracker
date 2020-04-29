from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

from application.app_utils import AppUtils
from application.config import Config

app = Flask(__name__)
app.route = AppUtils.prefix_route(app.route, Config.API_PREFIX)
app.config['SQLALCHEMY_DATABASE_URI'] = Config.SQLALCHEMY_DATABASE_URI
db = SQLAlchemy(app)
ma = Marshmallow(app)

with app.app_context():
    from application.routes import user

