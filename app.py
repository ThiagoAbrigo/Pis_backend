from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql

pymysql.install_as_MySQLdb()
import MySQLdb
import config.config

db = SQLAlchemy()


def create_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object("config.config.config")
    db.init_app(app)
    with app.app_context():
        from routes.api_person import api_person
        from routes.api_sessions import api_session
        from models.rol import Rol

        app.register_blueprint(api_person)
        app.register_blueprint(api_session)
        # create table bd
        db.create_all()
        # db.drop_all()
    return app
