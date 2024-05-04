from app import db
import uuid

class Person(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    lastname = db.Column(db.String(100))
    phone = db.Column(db.String(10))
    ci = db.Column(db.Integer(10))
    external_id = db.Column(db.VARCHAR(60), default=str(uuid.uuid4()))
    rol_id = db.Column(db.Integer, db.ForeignKey('rol.id'), unique=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
    account = db.relationship('Account', backref='person', lazy=True)