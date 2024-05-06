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

@api_person.route('/person/<external>', methods = ["GET"])
def search_external(external):
    search = personController.search_external(external)
    if search is None:
        return make_response(
            jsonify({"msg": "Person not found", "code": "404"}), 
            404
            )
    else:
        return make_response(
            jsonify({"msg": "OK", "code": "200", "data": search.serialize}), 
            200
            )
    
@api_person.route('/person/save', methods = ["GET"])
def createPerson():
    data = request.json
    person_id = personController.save_person(data)
    if (person_id >= 0):
        return make_response(
            jsonify({"msg":"OK", "code":200, "data": {"tag":"saved data"}}),
            200
        )
    else:
        return make_response(
            jsonify({"msg":"ERROR", "code":400, "data": {"error": Errors.error["-1"]}}),
            400
        )
