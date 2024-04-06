import requests
import pprint

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/451dcd24930fcd95a679b9ea814007ce/flightDealsFinder/prices"
with open("../../ignore_dir/api_key.txt") as key_file:
    key_data = key_file.readlines()
    bearer_auth_token = key_data[28].strip()

bearer_headers = {
        "Authorization": f"Bearer {bearer_auth_token}"
    }


class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        # 2. Use the Sheety API to GET all the data in that sheet and print it out.
        bearer_headers = {
            "Authorization": f"Bearer {bearer_auth_token}"
        }
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=bearer_headers)
        data = response.json()
        print(data)
        self.destination_data = data["prices"]
        # 3. Try importing pretty print and printing the data out again using pprint() to see it formatted.
        # pprint(data)
        return self.destination_data

    # 6. In the DataManager Class make a PUT request and use the row id from sheet_data
    # to update the Google Sheet with the IATA codes. (Do this using code).
    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data,
                headers=bearer_headers
            )
            print(response.text)
