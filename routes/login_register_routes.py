from app import app
from flask import request
from routes.serialise import *
from models.generated_models.login_request import *
from models.generated_models.login_response import *
from models.generated_models.register_request import *
from services.user_manager import *


@app.route('/', methods = ['GET'])
def get_root():
    return "api"

@app.route('/login', methods = ['POST'])
def login_post():
    '''Return a jwt given the users login details if correct'''
    login = Loginrequest(request.json)
    loginresponse = Loginresponse()
    valid, jwt = UserManager.generate_jwt(login.email, login.password)
    if valid:
        loginresponse.jwt = jwt
        return toJSONResponse(loginresponse)
    return "Unauthorised", 401

@app.route('/register', methods = ['POST'])
def register_post():
    #TODO add response json
    '''Return a jwt given the users login details if correct'''
    register = Registerrequest(request.json)
    valid, message = UserManager.register_user(register.email, register.password, register.code)
    if valid:
        return message
    return message, 400
