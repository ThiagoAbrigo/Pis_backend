from flask import Blueprint, jsonify, make_response, request
from controllers.sensorController import SensorController
from utils.utilities.errors import Errors
from flask_expects_json import expects_json
api_sensor = Blueprint('api_sensor', __name__)

sensorC = SensorController()

schema = {
    'type': 'object',
    'properties': {
        'name': {'type': 'string'},
        'state': {'type': 'string'},
        'longitud': {'type': 'Float'},
        'latitud': {'type': 'Float'},
    },
    'required': ['name', 'state', 'longitud', 'latitud']
}

#API for sensor
@api_sensor.route('/sensor', methods=["GET"])
def list():
    sensors = sensorC.listSensor()
    return make_response(
        jsonify({"msg":"OK", "code":200, "data":([sensor.serialize() for sensor in sensors])}),
        200
    )


@api_sensor.route('/sensor/save', methods=["POST"])
# @expects_json(schema)
def create():
    data = request.json
    sensor = sensorC.save_sensor(data)

    if sensor:
        return make_response(
            jsonify({"msg":"OK", "code":200, "data": {"tag":"saved data"}}),
            200
        )
    else:
        return make_response(
            jsonify({"msg":"ERROR", "code":400, "data": {"error": Errors.error[str(sensor)]}}),
            400
        )

api_sensor.route('/modify_sensor', methods=['POST'])
def modify_sensor():
    data = request.json
    modified_sensor = sensorC.modify_sensor(data)
    if (modified_sensor == -3):
        return make_response(
            jsonify({"msg":"ERROR", "code":400,'error': Errors.sensor_not_found["-3"]}), 400
        ) 
    else:
        return make_response(
            jsonify({"msg":"OK", "code":200, "data": {"sensor_saved":"saved data"}}),200
        )
