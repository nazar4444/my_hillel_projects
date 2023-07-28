import requests
import csv
import time

url = "http://api.open-notify.org/iss-now.json"

csv_filename = "mks_positions.csv"


def get_mks_position():
    response = requests.get(url)
    data = response.json()
    return data["mks_position"]["latitude"], data["mks_position"]["longitude"]


def write_csv(lat, lon):
    with open(csv_filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([lat, lon])


while True:
    latitude, longitude = get_mks_position()
    write_csv(latitude, longitude)
    time.sleep(5)

