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
        "identification": {"type": "string"},
        "email": {"type": "string"},
        "password": {"type": "string"},
    },
    "required": ["name", "lastname", "phone", "identification", "email", "password"],
}
