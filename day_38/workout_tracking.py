import requests

GENDER = "male"
WEIGHT_KG = 72
HEIGHT_CM = 180
AGE = 25


with open("../ignore_dir/api_key.txt") as key_file:
    key_data = key_file.readlines()
    api_key_nutritionix = key_data[24].strip()
    app_id_nutritionix = key_data[26].strip()


exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    'Content-Type': 'application/json',
    'x-app-id': app_id_nutritionix,
    'x-app-key': api_key_nutritionix,
}

input_json = {
    "query": "Ran for 1 hour",
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=exercise_endpoint, headers=headers, json=input_json)
result = response.json()
print(result)
