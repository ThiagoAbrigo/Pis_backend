from flask_expects_json import expects_json

schema_login = {
    "type": "object",
    "properties": {
        "email": {"type": "string"},
        "password": {"type": "string"},
    },
    "required": ["email", "password"],
}

schema_person ={
    'type': 'object',
    'properties':{
        'name': {'type': 'string'},
        'lastname':{'type': 'string'},
        'phone': {'type': 'string'},
        'ci': {'type': 'string'},
        'email':{'type': 'string'},
        'password':{'type':'string'},
    },
    'required': ['name', 'lastname', 'phone', 'ci','email','password']
}