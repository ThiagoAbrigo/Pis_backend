from models.account import Account
import jwt

from datetime import datetime, timedelta, timezone
from flask import current_app
from models.person import Person
import bcrypt

from models.rol import Rol
class LoginController:
    def getPerson(self, id_p):
        return Person.query.filter_by(id=id_p).first()

    def login(self, data):
        accountA = Account.query.filter_by(email=data["email"]).first()
        if accountA:
            if bcrypt.checkpw(data["password"].encode("utf-8"), accountA.password.encode("utf-8")):
                if accountA.status == 'activo':
                    token_payload = {
                        "external_id": accountA.external_id,
                        "expire": (datetime.now(timezone.utc) + timedelta(minutes=60)).isoformat(),
                    }
                    token = jwt.encode(
                        token_payload,
                        key=current_app.config["SECRET_KEY"],
                        algorithm="HS512",
                    )
                    person = self.getPerson(accountA.person_id)
                    role = Rol.query.filter_by(id=person.rol_id).first().rol
                    user_info = {
                        "token": token,
                        "user": person.name,
                        "role": role
                    }
                    return user_info
                else:
                    return {"error": "Su cuenta ha sido deshabilitada"}, 403 
            else:
                return {"error": "Sus credenciales son incorrectas"}, 401 
        else:
            return {"error": "Sus credenciales son incorrectas"}, 404  