import requests
import time

url = 'http://127.0.0.1:8000'

request = requests.get(f"{url}/lights")
print(request.json())


light = {'id': 31, 'on': True, 'bri': 254, 'sat': 40, 'hue': 40654}
request = requests.post(f"{url}/light/", json  = light)
print(request.json())

time.sleep(1)

light = {'id': 31, 'on': False}
request = requests.post(f"{url}/light/", json  = light)
print(request.json())

time.sleep(1.5)

light = {'id': 31, 'on': True, 'bri': 254, 'sat': 254, 'hue': 47104}
request = requests.post(f"{url}/light/", json  = light)
print(request.json())

time.sleep(1)

light = {'id': 31, 'on': False}
request = requests.post(f"{url}/light/", json  = light)
print(request.json())