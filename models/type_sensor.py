from enum import Enum 
class TypeSensor(Enum):
    AGUA = 'Agua'
    AIRE = 'Aire'
    @property
    def serialize(self):
        return {
            'name': self.name
        } 
    
