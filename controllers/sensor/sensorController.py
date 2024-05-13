from models.sensor import Sensor
import uuid
from app import db
import re

class SensorController:
    validate_ip = re.compile(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$')
    
    def save_sensor(self, data):
        if self.validate_ip.match(data['ip']):
            try:               
                sensor = Sensor()
                sensor.name = data["name"]
                sensor.latitude = data["latitude"]
                sensor.longitude = data["longitude"]
                sensor.ip = data["ip"]
                sensor.type_sensor = data["type_sensor"]
                sensor.external_id = uuid.uuid4()
                db.session.add(sensor)
                db.session.commit()
                return 2
            except:
                db.session.rollback()
                return -9
        else:
            return -10

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
            return -11