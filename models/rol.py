
from app import db

class Rol(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    rol = db.Column(db.String(100))
    status = db.Column(db.String(10), default='activo', server_default='activo')
    external_id = db.Column(db.String(60))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
    #a role has many people
    
@property

def serialize(self):
    return{
        'rol': self.rol,
        'status': self.status,
        "external_id": self.external_id
    }