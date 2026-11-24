USER_SCHEMA = {
    "type": "object",
    "properties": {
        "id": {
            "type": "integer",
            "minimun": 1,
        },
        "name": {
            "type": "string",
            "minLenght": 1,
        },
        "username": {
            "type": "string",
            "minLenght": 1,
        },
        "email": {
            "type": "string",
            "format": "email",
        },
    },
    "required": [
        "id",
        "name",
        "username",
        "email",
    ],
}
