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
    result = loginController.login(data)
    
    if isinstance(result, tuple):
        response, status_code = result
        return jsonify(response), status_code
    
    # Return success response
    return jsonify(result), 200