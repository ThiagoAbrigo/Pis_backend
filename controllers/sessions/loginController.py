from models.account import Account
import jwt
from datetime import datetime, timedelta
from flask import current_app
from models.person import Person

class LoginController:
    def getPerson(self, id_p):
        return Person.query.filter_by(id=id_p).first()

    def login(self, data):
        accountA = Account.query.filter_by(email=data["email"]).first()
        if accountA:
            if accountA.password == data["password"]:
                expire_time = datetime.now() + timedelta(minutes=30)
                token_payload = {
                    "external_id": accountA.external_id,
                    "expire": expire_time.strftime("%Y-%m-%d %H:%M:%S"),
                }
                token = jwt.encode(
                    token_payload,
                    key=current_app.config["SECRET_KEY"],
                    algorithm="HS512",
                )
                person = self.getPerson(accountA.person_id)
                user_info = {
                    "token": token,
                    "user": person.lastname + " " + person.name,
                }
                return user_info
            else:
                -6
        else:
            return -6
