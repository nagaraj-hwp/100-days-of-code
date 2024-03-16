# understanding API keys and authentication using python


import requests

with open("../ignore_dir/api_key.txt") as key_file:
    api_key = key_file.read()


MY_LAT = 9.92
MY_LONG = 78.11

base_url = "https://api.openweathermap.org/data/2.5/forecast"

weather_params = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
    "cnt": 4
}

response = requests.get(url=base_url, params=weather_params)
response.raise_for_status()
print(response.status_code)
print(response.json())
