from controllers.authenticateController import token_requeird
from flask import Blueprint, jsonify, make_response, request
from controllers.sensor.sensorController import SensorController
from utils.utilities.schemas import schema_sensor
from flask_expects_json import expects_json
from utils.utilities.errors import Errors
from utils.utilities.success import Success
from utils.utilities.response_http import make_response_error, make_response_ok

api_sensor = Blueprint("api_sensor", __name__)
sensorController = SensorController()


@api_sensor.route("/sensor/save", methods=["POST"])
def createSensor():
    data = request.json
    result = sensorController.save_sensor(data)

    if result == -10:
        return make_response_error(Errors.error["-10"], 400)
    elif result == 2:
        return make_response_ok({"success": Success.success["2"]})
    elif result == -9:
        return make_response_error(Errors.error["-9"], 400)

@api_sensor.route('/modify_sensor', methods=['POST'])
@expects_json(schema_sensor)
def modify_sensor():
    data = request.json
    modified_sensor = sensorController.modify_sensor(data)
    if (modified_sensor == -8):
        return make_response(
            jsonify({"msg":"ERROR", "code":400,'error': Errors.error["-3"]}), 400
        ) 
    else:
        return make_response(
            jsonify({"msg":"OK", "code":200, "data": {"sensor_saved":"saved data"}}),200
        )
    