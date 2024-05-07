from flask_expects_json import expects_json

schema_login = {
    "type": "object",
    "properties": {
        "email": {"type": "string"},
        "password": {"type": "string"},
    },
    "required": ["email", "password"],
}
schema_person = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "lastname": {"type": "string"},
        "phone": {
            "type": "string",
            "pattern": "^[0-9]{10}$"
        },
        "ci": {
            "type": "string",
            "pattern": "^[0-9]{10}$"
        }
    },
    "required": ["name", "lastname", "phone", "ci"]
}
