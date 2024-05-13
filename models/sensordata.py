from app import db
import uuid
from datetime import datetime
class SensorData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.DECIMAL(10, 2), default=0.0)
    date = db.Column(db.Date, default=datetime.now().date)
    hour = db.Column(db.String(10))
    external_id = db.Column(db.VARCHAR(60), default=str(uuid.uuid4()))
    id_sensor = db.Column(db.Integer, db.ForeignKey('sensor.id'))