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