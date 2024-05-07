from models.person import Person
from models.rol import Rol
from models.account import Account
from app import db
import uuid

class PersonController:
    
    def modify_person(self, data):
        person = Person.query.filter_by(external_id=data["external_id"]).first() #sql 
        if person:
            if "name" in data:
                person.name = data["name"]
            if "lastname" in data:
                person.lastname = data["lastname"]
            if "phone" in data:
                person.phone = data["phone"]
            if "ci" in data:
                person.ci = data["ci"]
                
            new_external_id = str(uuid.uuid4())
            person.external_id = new_external_id
            db.session.commit()
            modified_person = Person(
                name=person.name,
                lastname=person.lastname,
                phone=person.phone,
                ci=person.ci,
                external_id=new_external_id
            )
            return modified_person
        else:
            return -3
        
    def deactivate_account(self, external_id):
        person = Person.query.filter_by(external_id=external_id).first()
        if person:
            for account in person.account:
                account.status = 'desactivo' 
            db.session.commit()
            return True
        else:
            return False
    