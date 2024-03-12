# understanding APIs with python
import time
import requests
from datetime import datetime
import smtplib

MY_LAT = 9.925201
MY_LONG = 78.119774
my_email = "nagarajdevtest@gmail.com"
with open("../../ignore_dir/mail_app_password.txt") as passcode:
    password = passcode.read()


def get_iss_coordinates():
    iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_data = iss_response.json()
    longitude = iss_data["iss_position"]["longitude"]
    latitude = iss_data["iss_position"]["latitude"]
    location_info = (latitude, longitude)
    return location_info


def check_iss_within_range():
    location = get_iss_coordinates()
    latitude = location[0]
    longitude = location[1]
    if latitude - MY_LAT <= abs(5.0) and longitude - MY_LONG <= abs(5.0):
        return True
    return False


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now().hour
    if time_now >= sunset or time_now <= sunrise:
        return True
    return False


while True:
    time.sleep(60)
    if check_iss_within_range() and is_night():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                                from_addr=my_email,
                                to_addrs=my_email,
                                msg=f"Subject:Time to watch\n\nSatellite is overhead, go and take a look"
            )
