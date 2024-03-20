import requests
from datetime import datetime

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


sheet_endpoint = "https://api.sheety.co/451dcd24930fcd95a679b9ea814007ce/myWorkouts/workouts"

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)
    print(sheet_response.text)
