from models.person import Person

class PersonController:
    def listPerson(self):
        return Person.query.all()
    