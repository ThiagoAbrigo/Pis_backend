
from app import db
import uuid

class Person(db.Model):
    __tablename__ = 'person'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    lastname = db.Column(db.String(100))
    phone = db.Column(db.Integer())
    identification = db.Column(db.Integer())
    external_id = db.Column(db.VARCHAR(60), default=str(uuid.uuid4()))
    rol_id = db.Column(db.Integer, db.ForeignKey("rol.id"))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(
        db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now()
    )
    account = db.relationship("Account", backref="person", uselist=False, lazy=True)
    rol = db.relationship("Rol", backref="people", lazy=True)

    @property
    def serialize(self):
        return {
            "name": self.name,
            "lastname": self.lastname,
            "phone": self.phone,
            "identification": str(self.identification)
        }
        