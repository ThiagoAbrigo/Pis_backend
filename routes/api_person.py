from controllers.authenticateController import token_requeird
from flask import Blueprint, jsonify, make_response, request
from controllers.personController import PersonController
from utils.utilities.schemas import schema_person
from flask_expects_json import expects_json
from utils.utilities.errors import Errors
from utils.utilities.success import Success
from utils.utilities.response_http import make_response_error, make_response_ok
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
    result = personController.save_person(data)
    if result == -2:
        return make_response_error({"success": Errors.error["-2"]})
    elif result == 1:
        return make_response_ok({"success": Success.success["1"]})
    elif result == -1:
        return make_response_error(Errors.error["-1"], 404)
    elif result == -4:
        return make_response_error(Errors.error["-4"], 500)
    elif result == -8:
        return make_response_error(Errors.error["-8"], 400)

@api_person.route('/modify_person', methods=['POST'])
@expects_json(schema_person)
def modify_person():
    data = request.json
    modified_person = personController.modify_person(data)
    if (modified_person == -3):
        return make_response(
            jsonify({"msg":"ERROR", "code":400,'error': Errors.error["-3"]}), 400
        ) 
    else:
        return make_response(
            jsonify({"msg":"OK", "code":200, "data": {"person_saved":"saved data"}}),200
        )
    
@api_person.route('/deactivate_person/<external_id>', methods=['GET'])
def deactivate_person(external_id):
    success = personController.deactivate_account(external_id)
    if success:
        return make_response(
            jsonify({"msg":"OK", "code":200, "data": {"account":"Deactivated account"}}),200
        )
    else:
        return make_response(
            jsonify({"msg":"ERROR", "code":400,'error': 'The person does not exist'}), 404
        ) 
