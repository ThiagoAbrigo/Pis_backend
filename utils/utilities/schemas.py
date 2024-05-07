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
        },
        "email": {"type": "string"},
        "password": {
            "type": "string",
            "pattern": "^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$",
        },
    },
    "required": ["name", "lastname", "phone", "ci", "email", "password"],
}
