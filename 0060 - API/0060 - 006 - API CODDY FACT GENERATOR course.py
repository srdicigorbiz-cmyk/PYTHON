# Write code here
import requests
import json

def get_fact():
    response = requests.get("https://uselessfacts.jsph.pl/api/v2/facts/random", search_for)
    content = response.text
    data = json.loads(content)
    return data['text']

print("WELCOME TO RANDOM FACT GENERATOR")
search_for= str(input("Give a word to search fact."))
num = int(input())
if num > 7:
    print("Maximum number of facts per execution is 7")
elif num <= 0:
    print("Minimum number of facts per execution is 1")
else:
    counter = 0
    while counter < num:
        print(get_fact())
        counter += 1
