from models.person import Person
from models.rol import Rol
from models.account import Account
from app import db

from datetime import datetime, timedelta
from flask import current_app
import uuid;

class PersonController:
    def listPerson(self):
        return Person.query.all()
    def save_person(self, data):
        person = Person()
        rol = Rol.query.filter_by(rol = 'admin').first()  
        if rol:
            accounts = Account.query.filter_by(email = data["email"]).first()
            if accounts:
                return -2
            else:

                person.name = data["name"]
                person.lastname = data["lastname"]
                person.phone = data["phone"]
                person.ci = data["ci"]
                person.external_id = uuid.uuid4()
                person.rol_id = rol.id
                db.session.add(person)
                db.session.commit()

                account = Account()
                account.email = data["email"]
                account.password = data["password"]
                account.external_id = uuid.uuid4()
                account.person_id = person.id
                db.session.add(account)
                db.session.commit()
                return account.id
        else:
            return -1