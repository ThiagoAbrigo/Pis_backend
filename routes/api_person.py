from flask import Blueprint, jsonify, make_response, request
from controllers.personController import PersonController
from controllers.authenticateController import token_requeird

api_person = Blueprint("api_person", __name__)

personController = PersonController()


@api_person.route("/person", methods=["GET"])
@token_requeird
def listPerson():
    return make_response(
        jsonify(
            {
                "msg": "OK",
                "code": 200,
                "data": ([i.serialize for i in personController.listPerson()]),
            }
        ),
        200,
    )
