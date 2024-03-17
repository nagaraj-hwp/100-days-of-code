# understanding API keys and authentication using python
import requests
from twilio.rest import Client

with open("../ignore_dir/api_key.txt") as key_file:
    keys_data = key_file.readlines()
    from_number = keys_data[5].strip("\n")
    to_number = keys_data[7].strip("\n")
    account_sid = keys_data[9].strip("\n")
    auth_token = keys_data[11].strip("\n")
    api_key = keys_data[0].strip("\n")

MY_LAT = 29.11
MY_LONG = 93.09

base_url = "https://api.openweathermap.org/data/2.5/forecast"

weather_params = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
    "cnt": 8
}

response = requests.get(url=base_url, params=weather_params)
response.raise_for_status()
weather_data = response.json()
print(weather_data)
will_rain = False
for data in weather_data["list"]:
    if data["weather"][0]["id"] < 700:
        print("Bring an umbrella.")
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_=from_number,
        to=to_number,
        body="Its going to rain today, bring an umbrella with you!."
    )
    print(message.sid)
    print(message.status)
