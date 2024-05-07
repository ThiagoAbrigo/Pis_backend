from app import db
import uuid
from models.type_sensor import TypeSensor

class Sensor(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    status = db.Column(db.String(100))
    latitude = db.Column(db.Integer())
    longitude = db.Column(db.Integer())
    ip = db.Column(db.String(20))
    type_sensor = db.Column(db.Enum(TypeSensor))
    external_id = db.Column(db.VARCHAR(60), default=str(uuid.uuid4()))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(
        db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now()
    )
    dato_recolectado = db.relationship('SensorData', backref='sensor', lazy=True)


    @property
    def serialize(self):
        return {
            "name": self.name,
            "status": self.status,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "external_id": self.external_id,
        }