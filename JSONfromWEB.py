from urllib.request import urlopen
import json
import requests

url = "https://mdn.github.io/learning-area/javascript/oojs/json/superheroes.json"

try:
    r = requests.get(url,timeout=0.01)
    response = urlopen(url)
    data_json = json.loads(response.read())
    print(data_json)

except requests.ConnectionError:
    print("Connection timeout")
