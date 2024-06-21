import logging
from models.person import Person
from models.rol import Rol
from models.account import Account
from app import db
import uuid
import re
import bcrypt

class PersonController:
    def listPerson(self):
        return Person.query.all()

    def listPersonAccount(self):
        persons = Person.query.all()
        person_List = []
        for person in persons:
            account = person.account
            rol = person.rol
            person_data = {
                "external_id": person.external_id,
                "name": person.name,
                "lastname": person.lastname,
                "phone": person.phone,
                "identification": person.identification,
                "email": account.email if account else None,
                "status": account.status if account else None,
                "rol": rol.rol if rol else None,
            }
            person_List.append(person_data)
        return person_List

    def validate_ID(self, identification):
        identification_str = str(identification)

        if len(identification_str) != 10:
            return False

        coeficientes = [2, 1, 2, 1, 2, 1, 2, 1, 2]
        suma = 0
        for i in range(9):
            digito = int(identification_str[i]) * coeficientes[i]
            suma += digito if digito < 10 else digito - 9

        total = suma % 10 if suma % 10 == 0 else 10 - suma % 10

        if total == int(identification_str[9]):
            return True
        else:
            return False

    def validate_Email(self, email):
        format = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

        if re.match(format, email):
            return True
        else:
            return False

    def validate_Phone(self, phone):
        format = r"^[0-9]{10}$"

        if re.match(format, phone):
            return True
        else:
            return False

    def save_person(self, data):
        repeated_account = Account.query.filter_by(email=data["email"]).first()
        if repeated_account:
            return -2
        
        repeated_identification = Person.query.filter_by(identification=data["identification"]).first()
        if repeated_identification:
            return -9
        
        person = Person()
        rol_name = data["rol"]
        rol = Rol.query.filter_by(rol=rol_name).first()
        if rol:
            if not self.validate_ID(data["identification"]):
                return -8
            elif not self.validate_Email(data["email"]):
                return -11

            person.name = data["name"]
            person.lastname = data["lastname"]
            person.phone = data["phone"]
            person.identification = data["identification"]
            person.external_id = uuid.uuid4()
            person.rol_id = rol.id
            db.session.add(person)

            try:
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                logging.error(f'Error committing person: {e}')
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

            try:
                db.session.commit()
                return 1
            except Exception as e:
                db.session.rollback()
                logging.error(f'Error committing account: {e}')
                return -4
        else:
            return -1

    def modify_person(self, external_id, data):
        person = Person.query.filter_by(external_id=external_id).first()
        if person:
            if not self.validate_ID(data["identification"]):
                return -8
            elif not self.validate_Email(data["email"]):
                return -11
            rol_name = data["rol"]
            rol = Rol.query.filter_by(rol=rol_name).first()
            if rol:
                person.name = data.get("name", person.name)
                person.lastname = data.get("lastname", person.lastname)
                person.phone = data.get("phone", person.phone)
                person.identification = data.get("identification", person.identification)
                person.rol_id = rol.id
                if 'email' in data or 'password' in data:
                    account = Account.query.filter_by(person_id=person.id).first()
                    if account:
                        account.email = data.get('email', account.email)
                        if 'password' in data and data['password']:
                            hashed_password = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt())
                            account.password = hashed_password.decode('utf-8')
                    else:
                        return -10
                db.session.commit()

                return person
            else:
                return -3
        else:
            return -3

    def deactivate_account(self, external_id):
        person = Person.query.filter_by(external_id=external_id).first()
        if person:
            account = person.account
            if account:
                if account.status == "activo":
                    account.status = "desactivo"
                else:
                    account.status = "activo"
                db.session.commit()
                return account.status 
            else:
                return False
        else:
            return False

    def search_person(self, atribute):
        identification = Person.query.filter_by(identification=atribute).first()
        name = Person.query.filter_by(name=atribute).first()
        if identification:
            return identification
        else:
            if name:
                return name
            else:
                return -3

    def all_rol(self):
        roles = Rol.query.all()
        roles_data = [
            {"name": role.rol, "external_id": role.external_id} for role in roles
        ]
        return roles_data
