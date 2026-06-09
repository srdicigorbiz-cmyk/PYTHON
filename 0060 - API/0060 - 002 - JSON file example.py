json = {
    "errors": [
        {
            "status": "422",
            "source": {
                "pointer": "/data/attributes/firstName"
            },
            "title": "Invalid Attribute",
            "detail": "First name must contain at least two characters."
        }
    ]
}

### Write Your Code Below This Line
print(json["errors"])