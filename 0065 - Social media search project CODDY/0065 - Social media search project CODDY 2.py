import json
def searchby_entity(all_entities, filter_entity):
    data = json.loads(all_entities)
    return list(filter(lambda x: x["type"]==filter_entity, data["result"]))
    
    """
    result = []
    for key, value in data.items():
        for dict in value:
            if dict["type"]==filter_entity:
                result.append({"name":dict["name"], "city":dict["city"],"type":dict["type"]})
    return result
    """


json_data = '{"result": [{ 	"name": "Robert McNally", 	"city": "Hawaii", 	"type": "user" },{ 	"name": "Friendly Neighborhood Coder", 	"city": "Trivandrum", 	"type": "page" },{ 	"name": "Coddy Official", 	"city": "Haifa", 	"type": "page" }]}'
filter_entity = "page"
print(searchby_entity(json_data, filter_entity))