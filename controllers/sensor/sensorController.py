from models.sensor import Sensor
import uuid
from app import db
import re

class SensorController:
    validate_ip = re.compile(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$')

    def modify_sensor(self, data):
        sensor = Sensor.query.filter_by(external_id=data["external_id"]).first() 
        if sensor:
            if "name" in data:
                sensor.name = data["name"]
            if "status" in data:
                sensor.status = data["status"]
            if "latitude" in data:
                sensor.latitude = data["latitude"]
            if "longitude" in data:
                sensor.longitude = data["longitude"]
            if "type_sensor" in data:
                sensor.type_sensor = data["type_sensor"]
                
            new_external_id = str(uuid.uuid4())
            sensor.external_id = new_external_id
            db.session.commit()
            modified_sensoy = Sensor(
                name=sensor.name,
                status=sensor.status,
                longitude=sensor.longitude,
                latitude=sensor.latitude,
                external_id=new_external_id,
                type_sensor= type_sensor,
            )
            return modified_sensor
        else:

    def validate_latitude_longitude(self, latitude, longitude):
        latitude = float(latitude)
        longitude = float(longitude)
        if -90 <= latitude <= 90 and -180 <= longitude <= 180:
            return True
        else:
            return -21
        
    def listSensor(self):
        return Sensor.query.all()

    def save_sensor(self, data):
        if not self.validate_ip.match(data['ip']):
            return -10 
        
        latitude = data["latitude"]
        longitude = data["longitude"]
        validation_result = self.validate_latitude_longitude(latitude, longitude)
        if validation_result != True:
            return validation_result
        
        try:
            sensor = Sensor(
                name=data["name"],
                latitude=float(latitude),
                longitude=float(longitude),
                ip=data["ip"],
                type_sensor=data["type_sensor"],
                external_id=uuid.uuid4()
            )
            db.session.add(sensor)
            db.session.commit()
            return 2 
        except:
            db.session.rollback()
            return -9

    def deactivate_sensor(self, external_id):
        sensor = Sensor.query.filter_by(external_id=external_id).first()
        if sensor:
            sensor.status = "desactivo"
            db.session.commit()
            return 5
        else:
            return -20

        
    def search_sensor(self, name):
        name = Sensor.query.filter_by(name = name).first()
        if name:
            return name
        else:
            return -3

