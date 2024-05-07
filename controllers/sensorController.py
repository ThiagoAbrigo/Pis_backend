from models.sensor import Sensor
from app import db
import uuid

class SensorController:
    def listSensor(self):
        return Sensor.query.all()
    
    def save_sensor(self, data):
        sensor = Sensor()
        sensor.name = data["name"]
        sensor.status = data["status"]
        sensor.latitude = data["latitude"]
        sensor.longitude = data["longitude"]
        sensor.external_id = uuid.uuid4()
        db.session.add(sensor)
        db.session.commit()                      
        return sensor

    def search_external(self, external):
        sensor = Sensor.query.filter_by(external_id=external).first()
        if sensor:
            return sensor
        else:
            return None

    def modify_sensor(self, data):
        sensor = Sensor.query.filter_by(external_id=data["external_id"]).first()
        if sensor:
            if "name" in data:
                sensor.name = data["name"]
            if "status" in data:
                sensor.state = data["state"]
            if "latitude" in data:
                sensor.latitude = data["latitude"]
            if "longitud" in data:
                sensor.longitude = data["longitude"]
                
            new_external_id = str(uuid.uuid4())
            sensor.external_id = new_external_id
            modified_sensor = Sensor(
                name=sensor.name,
                status=sensor.status,
                longitude=sensor.longitude,
                latitude=sensor.latitude,
                external_id=new_external_id
            )
            return modified_sensor
        else:
            return -3
