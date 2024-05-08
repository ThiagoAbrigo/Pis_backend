from enum import Enum 
class TypeSensor(Enum):
    AGUA = 'Agua'
    AIRE = 'Aire'
    @staticmethod
    def choices():
        return [(estado.name, estado.value) for estado in TypeSensor]