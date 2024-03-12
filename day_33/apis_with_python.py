# understanding APIs with python
import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
print(response.content.decode())

data = response.json()
print(data)

longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

location_info = (latitude, longitude)

print(location_info)

