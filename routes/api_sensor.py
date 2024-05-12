from controllers.authenticateController import token_requeird
from flask import Blueprint, request
from controllers.sensor.sensorController import SensorController
from controllers.sensor.sensordataController import SensorDataController
from utils.utilities.errors import Errors
from utils.utilities.success import Success
from utils.utilities.response_http import make_response_error, make_response_ok

api_sensor = Blueprint("api_sensor", __name__)
sensorController = SensorController()
sensorDataController = SensorDataController()

@api_sensor.route("/sensor/save", methods=["POST"])
def createSensor():
    data = request.json
    result = sensorController.save_sensor(data)
    if result == -10:
        return make_response_error(Errors.error["-10"], 400)
    if result == -21:
        return make_response_error(Errors.error["-21"], 400)
    if result == -22:
        return make_response_error(Errors.error["-22"], 400)
    elif result == 2:
        return make_response_ok({"success": Success.success["2"]})
    elif result == -9:
        return make_response_error(Errors.error["-9"], 400)

@api_sensor.route("/sensor/list_data", methods=["GET"])
def listSensorData():
    result = sensorDataController.list_sensor_data()
    return make_response_ok(result)

@api_sensor.route("/sensor/list_sensor_type/<type>", methods=["GET"])
def listSensorType(type):
    result = sensorDataController.list_sensor_type(type)
    if result == -20:
        return make_response_error(Errors.error["-20"], 404)
    else:
        return make_response_ok(result)

@api_sensor.route("/sensor/list_sensor_name/<name>", methods=["GET"])
def listSensorName(name):
    result = sensorDataController.list_sensor_name(name)
    if result == -20:
        return make_response_error(Errors.error["-20"], 404)
    else:
        return make_response_ok(result)
    
@api_sensor.route("/sensor/status/<external_id>", methods=["GET"])
def desactivateSensor(external_id):
    result = sensorController.deactivate_sensor(external_id)
    if result == 5:
        return make_response_ok({"success": Success.success["5"]})
    elif result == -20:
        return make_response_error(Errors.error["-20"], 404)
    
