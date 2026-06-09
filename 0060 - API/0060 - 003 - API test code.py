import requests

# Ez egy teszt API, ami egy képzeletbeli bejegyzést ad vissza
url = "https://jsonplaceholder.typicode.com/posts/1"

# 1. Elküldjük a kérést
response = requests.get(url)

# 2. Megnézzük a státuszt (200 = OK)
print(f"Státuszkód: {response.status_code}")

# 3. Kinyerjük az adatot (a .json() metódus automatikusan szótárrá alakítja)
data = response.json()

print("Adatok a szerverről:")
print(data)

# Mivel ez egy szótár, el tudod érni az egyes mezőket is:
print(f"A bejegyzés címe: {data['title']}")