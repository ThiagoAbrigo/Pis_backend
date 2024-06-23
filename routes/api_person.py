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
@api_person.route("/person/account", methods=["GET"])
def listPersonAccount():
    return make_response_ok(personController.listPersonAccount())
    
@api_person.route("/person/save", methods=["POST"])
@expects_json(schema_person)
def createPerson():
    data = request.json
    result = personController.save_person(data)
    if result == -2:
        return make_response(jsonify({"error": "El correo electrónico ya está registrado"}), 400)
    if result == -9:
        return make_response(jsonify({"error": "Cédula ya registrada"}), 400)
    elif result == 1:
        return make_response_ok({"success": "Person and account saved successfully"})
    elif result == -1:
        return make_response_error(Errors.error["-1"], 404)
    elif result == -4:
        return make_response_error(Errors.error["-4"], 500)
    elif result == -8:
        return make_response(jsonify({"error": "cédula inválida"}), 400)
    elif result == -11:
        return make_response_error(Errors.error["-11"], 400)
    elif result == -12:
        return make_response_error(Errors.error["-12"], 400)
    else:
        return make_response_error("Error desconocido", 500)



@api_person.route('/modify_person/<external_id>', methods=['POST'])
# @expects_json(schema_person)
def modify_person(external_id):
    data = request.json
    modified_person = personController.modify_person(external_id, data)
    print(external_id)
    if (modified_person == -3):
        return make_response_error(Errors.error["-3"], 404)
    elif modified_person == -8:
        return make_response_error(Errors.error["-8"], 400)
    else:
        return make_response_ok({"success": Success.success["1"]})
    
    
@api_person.route('/deactivate_person/<external_id>', methods=['GET'])
def deactivate_person(external_id):
    success = personController.deactivate_account(external_id)
    if success:
        return make_response_ok(success)
    else:
        return make_response_error(Errors.error["-3"], 404)
    
@api_person.route('/roles', methods=['GET'])
def list_roles():
    return make_response(
        jsonify(
            {
                "msg": "OK",
                "code": 200,
                "data": personController.all_rol(),
            }
        ),
        200,
    )

@api_person.route("/search/person/<attribute>", methods = ['GET'])
def search_person(attribute):
    
    result = personController.search_person(attribute)
    if (result == -3):
        return make_response_error(Errors.error["-3"], 404)
    else: 
        return result
