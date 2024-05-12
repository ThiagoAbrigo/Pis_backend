from models.sensor import Sensor
import uuid
from app import db
import re
class SensorController:
    validate_ip = re.compile(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")

    def validate_latitude_longitude(self, latitude, longitude):
        latitude = float(latitude)
        longitude = float(longitude)
        if not (-90 <= latitude <= 90):
            return -21
        if not (-180 <= longitude <= 180):
            return -22
        return True
    
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
