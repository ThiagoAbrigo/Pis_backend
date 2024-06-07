from flask import Blueprint, jsonify, make_response, request
from controllers.sessions.loginController import LoginController
from utils.utilities.errors import Errors
from flask_expects_json import expects_json
from controllers.authenticateController import token_requeird
from utils.utilities.schemas import schema_login

api_session = Blueprint("api_session", __name__)

loginController = LoginController()


@api_session.route("/login", methods=["POST"])
@expects_json(schema_login)
def session():
    data = request.json
    id = loginController.login(data)

    if type(id) == int:
        return make_response(
            jsonify({"msg" : "ERROR", "code" : 400, "data" :{"error" : Errors.error.get(str(id))}}), 
            400
        )
    else:
        return make_response(
            jsonify({"msg": "OK", "code": 200, "data": id}),
            200
        )