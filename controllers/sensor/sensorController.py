from models.sensor import Sensor
import uuid
from app import db

class SensorController:
    def save_sensor(self, data):
        sensor = Sensor()
        sensor.name = data["name"]
        sensor.latitude = data["latitude "]
        sensor.longitude = data["longitude"]
        sensor.ip = data["ip"]
        sensor.type_sensor = data["type_sensor"]
        sensor.external_id = uuid.uuid4()
        db.session.add(sensor)
        db.session.commit()
        return sensor.id