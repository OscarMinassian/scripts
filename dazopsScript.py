# "Your Python challenge for next week: write a script that will return the weather for Bronte NSW"
# Pull data from the API and return the current temp for Bronty
import requests
import json

# Params for weather I'm interested in. 
# Long/Lat set to Bronty NSW

longitude = 151.26
latitude = -33.9
timezone = "Australia/NSW"
forecast_days = 3
temperature_2m = "°C"

response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&timezone={timezone}&forecast_days={forecast_days}&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m")

# create a formatted string of the Python JSON object
def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

jprint(response.json())