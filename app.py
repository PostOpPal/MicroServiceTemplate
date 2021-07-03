from configs.configs import JWTConfig
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from configs.configs import *
import json
import os

# create app
#app = Flask(__name__)
#db = SQLAlchemy(app)

# def create_app(test_config = None, local = False):
#     print("test_config",test_config)
#     # create and configure the app
#     app = Flask(__name__, instance_relative_config=True)

#     app.config.from_mapping(
#         SECRET_KEY='dev',
#         SQLALCHEMY_DATABASE_URI=os.path.join(app.instance_path, 'flask.sqlite'),
#         SQLALCHEMY_TRACK_MODIFICATIONS = False
#     )
#     if test_config is not None:
#         app.config.from_mapping(test_config)

#     db = SQLAlchemy(app)
#     if local:
#         with app.app_context():
#             db.create_all()
    
#     print(app.config)
#     return app

app = Flask(__name__, instance_relative_config=True)

if os.environ.get("DEPLOY") == "test":
    print()
    print("Testing")
    app.config.from_mapping(
        SECRET_KEY='dev',
        SQLALCHEMY_DATABASE_URI = 'sqlite:///test.sqlite',
        SQLALCHEMY_TRACK_MODIFICATIONS = False
    )

elif os.environ.get("DEPLOY") == "local":
    print()
    print("Local")
    app.config.from_mapping(
        SECRET_KEY='dev',
        SQLALCHEMY_DATABASE_URI = 'sqlite:///test.sqlite',
        SQLALCHEMY_TRACK_MODIFICATIONS = False
    )

else:
    print("Deployment")
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        SQLALCHEMY_DATABASE_URI=os.path.join(app.instance_path, 'sqlite:///basic_app.sqlite'),
        SQLALCHEMY_TRACK_MODIFICATIONS = False
    )

db = SQLAlchemy(app)
from sqlalchemy_models.models import *
db.create_all()


#add an import to any route folders here
from routes.login_register_routes import *
