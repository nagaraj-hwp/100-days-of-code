import requests
from datetime import datetime

USERNAME = "nagarajhwp"
GRAPH_ID = "graph1"
pixela_endpoint = "https://pixe.la/v1/users"

with open("../ignore_dir/api_key.txt") as key_file:
    key_data = key_file.readlines()
    pixela_token = key_data[22].strip()

headers = {
    "X-USER-TOKEN": pixela_token,
}

parameters = {
    "token": pixela_token,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=parameters)
# print(response.text)

pixela_graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Coding",
    "unit": "commit",
    "type": "int",
    "color": "shibafu",

}

# response = requests.post(url=pixela_graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_creation_endpoint = f"{pixela_graph_endpoint}/{GRAPH_ID}"

today = datetime(year=2024, month=1, day=30)
pixel_date = today.strftime("%Y%m%d")

pixel_config = {
    "date": pixel_date,
    "quantity": "1",
}

# response = requests.post(url=pixel_creation_endpoint, json=pixel_config, headers=headers)
# print(response.text)

pixel_update_config = {
    "quantity": "3",
    "optionalData": "{}",
}

pixel_put_endpoint = f"{pixel_creation_endpoint}/{pixel_date}"
print(pixel_put_endpoint)

# response = requests.put(url=pixel_put_endpoint, json=pixel_update_config, headers=headers)
# print(response.text)

pixel_delete_endpoint = f"{pixel_creation_endpoint}/{pixel_date}"
print(pixel_delete_endpoint)

response = requests.delete(url=pixel_delete_endpoint, headers=headers)
print(response.text)
