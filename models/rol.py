
from app import db

class Rol(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    rol = db.Column(db.String(100))
    status = db.Column(db.Boolean, default = True)
    external_id = db.Column(db.String(60))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
    
