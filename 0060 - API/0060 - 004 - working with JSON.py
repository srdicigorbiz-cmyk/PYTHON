data = {
    "errors": [
        {
            "status": "422",
            "source": {"pointer": "/data/attributes/firstName"},
            "title": "Invalid Attribute",
            "detail": "First name must contain at least two characters." 
        },
        {
            "status": "432",
            "source": {"pointer": "/data/attributes/firstName"},
            "title": "Invalid ",
            "detail": "example error." 
        }
    ] 
}
search_for = ("422")
result = []
for error in data["errors"]:
    if error["status"]==search_for:
        result.append(error["detail"])
if len(result)==0:
    print("No error code found")
else:
    print(f"Errors found: {result}")
    
    
