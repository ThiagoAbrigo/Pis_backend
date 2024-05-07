from app import create_app
from jsonschema import ValidationError
from flask import jsonify, make_response, request

app = create_app()

@app.errorhandler(400)
def bad_request(error):
    if isinstance(error.description, ValidationError):
        message_error = error.description
        return make_response(
            jsonify({"msg":"ERROR", "code":400, "data": {"error":message_error.message}}),
            400
        )
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")