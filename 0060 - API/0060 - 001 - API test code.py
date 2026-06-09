import requests

def test_api_connection(url):
    try:
        response = requests.get(url)
        # Ellenőrizzük, hogy sikeres volt-e a kapcsolat (200 OK)
        if response.status_code == 200:
            print(f"Siker! Kapcsolat létrejött a {url} címmel.")
            return True
        else:
            print(f"Hiba történt, státuszkód: {response.status_code}")
            return False
    except Exception as e:
        print(f"Nem sikerült elérni a szervert: {e}")
        return False

# Próbáld ki a JSONPlaceholder ingyenes API-jával
test_api_connection("https://jsonplaceholder.typicode.com/posts/1")
