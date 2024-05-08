from flask import make_response, jsonify

def make_response_ok(data):
    return make_response(
        jsonify({"msg": "OK", "code": 200, "data": data}),
        200
    )

def make_response_error(error_msg, status_code):
    return make_response(
        jsonify({"msg": "ERROR", "code": status_code, "data": {"error": error_msg}}),
        status_code
    )