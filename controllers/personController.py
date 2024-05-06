from models.person import Person
from models.rol import Rol
from models.account import Account
from app import db

from datetime import datetime, timedelta
from flask import current_app
import jwt
import bcrypt

class PersonController:
    def listPerson(self):
        return Person.query.all()

    def save_person(self, data):
        person = Person()
        rol = Rol.query.fliter_by(name = 'admin').first  #maybe have to change 'admin'
        if rol:
            accounts = Account.query.filter_by(email = data["email"]).first()
            if accounts:
                return -2
            else:
                person.name = data["name"]
                person.lastname = data["lastname"]
                person.phone = data["phone"]
                person.ci = data["ci"]
                person.external_id = data["external_id"]
                person.rol_id = data["rol_id"]
                db.session.add(person)
                db.session.commit()

                account = Account()
                account.email = data["email"]
                account.password = data["password"]
                account.external_id = data["external_id"]
                account.person_id = person.id
                db.session.add(account)
                db.session.commit()
                return account.id
        else:
            return -1
    
    def search_external(self,external):
        person = Person.query.filter_by(external_id = external).first()
        if person:
            return person
        else:
            return None
        
    def log_in(self, data):
        accountA = Account.query.filter_by(email = data["email"]).first()
        if(accountA):
            ### way to encrypt need to check
            ##https://platzi.com/tutoriales/2514-fastapi-errores/14590-como-encriptar-contrasenas-en-python-y-por-que-hacerlo/
            accountA.password.encode('utf-8')
            salt = bcrypt.gensalt()
            hashed = bcrypt.hashpw(accountA.password, salt)

            if accountA.password ==data["password"]:
                token = jwt.encode(
                    {
                        "external": accountA.external_id,
                        "exp": datetime.now(datetime.UTC) + timedelta(minutes = 15)                        
                    },
                    KEY = current_app.config["SECRET_KEY"],
                    algorithm= "HS512"
                )
                account = Account()
                account.copy(accountA)
                person = Account.person(accountA, id)
                info ={
                    "token": token,
                    "user": person.lastname+ " " +person.name
                }
            else:
                return -4