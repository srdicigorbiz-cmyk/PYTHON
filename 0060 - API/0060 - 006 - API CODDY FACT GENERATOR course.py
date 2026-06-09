# Write code here
import requests
import json

def get_fact():
    response = requests.get("https://uselessfacts.jsph.pl/api/v2/facts/random")
    content = response.text
    data = json.loads(content)
    return data['text']



num = int(input())


counter = 0
while counter < num:
    print(get_fact())
    counter += 1
