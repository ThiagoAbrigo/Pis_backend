from models.person import Person
from models.rol import Rol
from models.account import Account
from app import db
import bcrypt
import uuid

class PersonController:
    def listPerson(self):
        return Person.query.all()
    
    def validate_ID(self, identification):
        if len(identification) != 10:
            return False

        coeficientes = [2, 1, 2, 1, 2, 1, 2, 1, 2]
        suma = 0
        for i in range(9):
            digito = int(identification[i]) * coeficientes[i]
            suma += digito if digito < 10 else digito - 9

        total = suma % 10 if suma % 10 == 0 else 10 - suma % 10

        if total == int(identification[9]):
            return True
        else:
            return False

    def save_person(self, data):
        repeated_account = Account.query.filter_by(email=data['email']).first()
        if repeated_account:
            return -2
        
        person = Person()
        rol = Rol.query.filter_by(external_id = data['rol']).first()
        if rol:
            if not self.validate_ID(data['identification']):
                return -8

            person.name = data["name"]
            person.lastname = data["lastname"]
            person.phone = data["phone"]
            person.identification= data["identification"]
            person.external_id = uuid.uuid4()
            person.rol_id = rol.id
            db.session.add(person)
            
            try:
                db.session.commit()
            except:
                db.session.rollback()
                return -4
            
            hashed_password = bcrypt.hashpw(
                    data["password"].encode("utf-8"), bcrypt.gensalt()
                )
            account = Account()
            account.email = data["email"]
            account.password = hashed_password.decode("utf-8")
            account.person_id = person.id
            account.external_id = uuid.uuid4()
            db.session.add(account)
            db.session.commit()
            return 1
        else:
            return -1
    def modify_person(self, data):
        person = Person.query.filter_by(external_id=data["external_id"]).first() 
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