def get_all_records(full_json_str):
    # Write code here
    result = {"results":[]}
    for key,value in full_json_str.items():
        for dict in value:
            result["results"].append({"full_name":dict["first_name"]+" "+dict["last_name"], "city":dict["city"], "type":dict["type"]})
    return result

full_json_str = {"results": [{"first_name": "Aaron", "last_name": "Taylor", "city": "Paris", "type": "user"}, {"first_name": "Maria", "last_name": "Taylor", "city": "Paris", "type": "user"}]}
print(get_all_records(full_json_str))