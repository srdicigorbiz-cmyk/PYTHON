import requests

url = "https://api.example.com/data"

# A fejléc egy szótár, amiben a kulcsot az API által elvárt névvel adjuk át
headers = {
    "Authorization": "Bearer YOUR_API_KEY_HERE",
    "Content-Type": "application/json"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    print("Sikeresen hitelesítettük magunkat!")
    data = response.json()
else:
    print(f"Hiba: {response.status_code} - A szerver elutasította a kulcsot.")