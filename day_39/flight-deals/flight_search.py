import requests

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"

with open("../../ignore_dir/api_key.txt") as key_file:
    key_data = key_file.readlines()
    TEQUILA_API_KEY = key_data[30].strip()


class FlightSearch:

    def get_destination_code(self, city_name):
        # Return "TESTING" for now to make sure Sheety is working. Get TEQUILA API data later.
        code = "TESTING"
        return code
