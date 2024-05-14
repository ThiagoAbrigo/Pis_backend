from datetime import datetime
from models.sensor import Sensor
from models.sensordata import SensorData
from app import db


class SensorDataController:
    def list_sensor_data(self):
        today_date = datetime.now().date()
        sensors = (db.session.query(Sensor).join(SensorData).filter(SensorData.date == today_date).all())
        data = []
        for sensor in sensors:
            sensor_info = {
                "name": sensor.name,
                "latitude": sensor.latitude,
                "longitude": sensor.longitude,
                "ip": sensor.ip,
                "type_sensor": sensor.type_sensor.serialize,
                "datoRecolectado": []
            }
            
            for sensor_data in sensor.dato_recolectado:
                sensor_info["datoRecolectado"].append(
                    {
                        "data": sensor_data.data,
                        "date": str(sensor_data.date),
                        "hour": str(sensor_data.hour),
                    }
                )
            data.append(sensor_info)
        return data
    
    def list_sensor_type(self, value):
        list = Sensor.query.filter_by(type_sensor=value).all()
        if not list:
            return -20
        datos = []
        for sensor in list:
            data_sensor = {
                "name": sensor.name,
                "latitude": sensor.latitude,
                "longitude": sensor.longitude,
                "type_sensor": sensor.type_sensor.serialize,
                "dato_recolectado": [
                    {
                        "data": str(dato.data),
                        "date": str(dato.date),
                        "hour": dato.hour
                    } for dato in sensor.dato_recolectado
                ]
            }
            datos.append(data_sensor)
        return datos

    def list_sensor_name(self, value):
        list = Sensor.query.filter_by(name=value).all()
        if not list:
            return -20
        datos = []
        for sensor in list:
            data_sensor = {
                "name": sensor.name,
                "latitude": sensor.latitude,
                "longitude": sensor.longitude,
                "type_sensor": sensor.type_sensor.serialize,
                "dato_recolectado": [
                    {
                        "data": str(dato.data),
                        "date": str(dato.date),
                        "hour": dato.hour
                    } for dato in sensor.dato_recolectado
                ]
            }
            datos.append(data_sensor)
        return datos

