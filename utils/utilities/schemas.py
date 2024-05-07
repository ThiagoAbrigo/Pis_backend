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
        "phone": {"type": "string"},
        "ci": {"type": "string"},
        "email": {"type": "string"},
        "password": {
            "type": "string",
            "pattern": "^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$",
        },
    },
    "required": ["name", "lastname", "phone", "ci", "email", "password"],
}
