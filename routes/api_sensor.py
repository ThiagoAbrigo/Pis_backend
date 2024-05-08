from controllers.authenticateController import token_requeird
from flask import Blueprint, request
from controllers.sensor.sensorController import SensorController
from utils.utilities.errors import Errors
from utils.utilities.success import Success
from utils.utilities.response_http import make_response_error, make_response_ok

api_sensor = Blueprint("api_sensor", __name__)
sensorController = SensorController()


@api_sensor.route("/sensor/save", methods=["POST"])
def createPerson():
    data = request.json
    result = sensorController.save_sensor(data)

    if result == -10:
        return make_response_error(Errors.error["-10"], 400)
    elif result == 2:
        return make_response_ok({"success": Success.success["2"]})
    elif result == -9:
        return make_response_error(Errors.error["-9"], 400)
