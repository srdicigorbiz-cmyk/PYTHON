import requests

# Step 1: Send GET request with parameters
response = requests.get("https://api.open-meteo.com/v1/forecast",
    # Your URL here
    params={
    "latitude": 52.52,
    "longitude": 13.41,
    "current_weather": "true"
}
        
)

# Step 2: Parse JSON response
data = response.json()

# Step 3: Print current temperature
print(f"Current temperature:", data["current_weather"]["temperature"], "°C")