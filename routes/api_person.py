from controllers.authenticateController import token_requeird
from flask import Blueprint, jsonify, make_response, request
from controllers.personController import PersonController
from utils.utilities.schemas import schema_person
from flask_expects_json import expects_json
from utils.utilities.errors import Errors
from utils.utilities.success import Success

api_person = Blueprint("api_person", __name__)
personController = PersonController()


@api_person.route("/person", methods=["GET"])
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

@api_person.route("/person/save", methods=["POST"])
@expects_json(schema_person)
def createPerson():
    data = request.json
    person_id = personController.save_person(data)
    if person_id >= 0:
        return make_response(
            jsonify(
                {"msg": "OK", "code": 200, "data": {"success": Success.success["1"]}}
            ),
            200,
        )
    else:
        return make_response(
            jsonify(
                {"msg": "ERROR", "code": 400, "data": {"error": Errors.error["-1"]}}
            ),
            400,
        )
