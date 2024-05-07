from models.person import Person
from models.rol import Rol
from models.account import Account
from app import db
import bcrypt
import uuid


class PersonController:
    def listPerson(self):
        return Person.query.all()

    def save_person(self, data):
        person = Person()
        rol = Rol.query.filter_by(rol="admin").first()
        if rol:
            accounts = Account.query.filter_by(email=data["email"]).first()
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

                hashed_password = bcrypt.hashpw(
                    data["password"].encode("utf-8"), bcrypt.gensalt()
                )
                account = Account()
                account.email = data["email"]
                account.password = hashed_password.decode("utf-8")
                account.external_id = uuid.uuid4()
                account.person_id = person.id
                db.session.add(account)

                db.session.commit()
                return 1
        else:
            return -1
