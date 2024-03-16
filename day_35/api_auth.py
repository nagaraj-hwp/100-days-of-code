# understanding API keys and authentication using python


import requests

with open("../ignore_dir/api_key.txt") as key_file:
    api_key = key_file.read()


MY_LAT = 17.05
MY_LONG = 174.11

base_url = "https://api.openweathermap.org/data/2.5/forecast"

weather_params = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
    "cnt": 4
}

response = requests.get(url=base_url, params=weather_params)
response.raise_for_status()
weather_data = response.json()
print(weather_data)
for data in weather_data["list"]:
    if data["weather"][0]["id"] < 700:
        print("Bring an umbrella.")
        break
