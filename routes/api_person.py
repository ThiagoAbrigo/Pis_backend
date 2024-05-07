from flask import Blueprint, jsonify, make_response, request
from controllers.personController import PersonController
from controllers.authenticateController import token_requeird
from utils.utilities.errors import Errors
from flask_expects_json import expects_json
from utils.utilities.schemas import schema_person 

api_person = Blueprint("api_person", __name__)

personC = PersonController()


@api_person.route("/person", methods=["GET"])
@token_requeird
def listPerson():
    return make_response(
        jsonify(
            {
                "msg": "OK",
                "code": 200,
                "data": ([i.serialize for i in personC.listPerson()]),
            }
        ),
        200,
    )

@api_person.route('/modify_person', methods=['POST'])
@expects_json(schema_person)
def modify_person():
    data = request.json
    modified_person = personC.modify_person(data)
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
    success = personC.deactivate_account(external_id)
    if success:
        return make_response(
            jsonify({"msg":"OK", "code":200, "data": {"account":"Deactivated account"}}),200
        )
    else:
        return make_response(
            jsonify({"msg":"ERROR", "code":400,'error': 'The person does not exist'}), 404
        ) 