from app import db
import uuid

class Account(db.Model):
    
    __tablename__ = 'account'
    
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    status = db.Column(db.String(10), default="activo")
    password = db.Column(db.String(250))
    external_id = db.Column(db.VARCHAR(60), default=str(uuid.uuid4()))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(
        db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now()
    )
    person_id = db.Column(
        db.Integer, db.ForeignKey("person.id"), nullable=False, unique=True
    )

    @property
    def serialize(self):
        return {
            "email": self.email,
            "status": self.status,
            "external_id": self.external_id,
        }