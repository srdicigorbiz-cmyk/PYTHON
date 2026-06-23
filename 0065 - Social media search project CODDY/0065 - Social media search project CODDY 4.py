import json
def search(filter_query, full_json):
    json_data = json.loads(full_json)['result']
    #filter query
    filter = {}
    if len(filter_query)==0:
        return json_data
    else:
        filter_query = [x.split("=") for x in filter_query.split("&")]
    for item in filter_query:
        filter[item[0]]=item[1]
    #configuring search engine
    search_result = []
    for record in json_data:
        status = False
        for f,v in filter.items():
            try:
                if record[f] == v:
                    status = True
                else:
                    status = False
            except KeyError as e:
                status = False
        if status == True:
            search_result.append(record)
    
    return search_result










json_string='{"result": [{ 	"name": "Robert McNally", 	"city": "Hawaii", 	"type": "user", "gender": "M"},{ 	"name": "Elizabeth Minelli", 	"city": "Hawaii", 	"type": "user", "gender": "F"}, { 	"name": "Friendly Neighborhood Coder", 	"city": "Trivandrum", 	"type": "page" },{ 	"name": "Coddy Official", 	"city": "Haifa", 	"type": "page" }]}'
json_string1 = '{"result": [{ 	"name": "Virat Kohli", 	"city": "Mumbai", 	"type": "user", "gender": "M", "verified": "true"},{ 	"name": "Tapsee Pannu", 	"city": "Pune", 	"type": "user", "gender": "F", "verified": "true"}, { 	"name": "Stephen Kingo", 	"city": "New York", 	"type": "user", "gender": "M", "verified": "false"},{ 	"name": "Friendly Neighborhood Coder", 	"city": "Trivandrum", 	"type": "page", "youtube": "true"},{ 	"name": "Coddy Official", 	"city": "Haifa", 	"type": "page", "youtube":"true", "verified": "true" },{ 	"name": "Programmers are not Humans", 	"city": "Frankfurt", 	"type": "page", "verified": "true" }]}'

input1 = 'type=user'
input2 = 'type=page&name=Coddy Official'
input3 = 'type=user&gender=M'
input4 = 'type=user&verified=true'

print(search(input1, json_string))
print("************")
print(search(input2, json_string))
print("************")
print(search(input3, json_string))

print("************")
print(search(input4, json_string1))
# [{'name': 'Virat Kohli', 'city': 'Mumbai', 'type': 'user', 'gender': 'M', 'verified': 'true'}, 
# {'name': 'Tapsee Pannu', 'city': 'Pune', 'type': 'user', 'gender': 'F', 'verified': 'true'}]

