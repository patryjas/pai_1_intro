from urllib.request import urlopen
import json
import requests

url = "https://mdn.github.io/learning-area/javascript/oojs/json/superheroes.json"

response = urlopen(url)
data_json = json.loads(response.read())


try:
    r = requests.get("https://mdn.github.io/learning-area/javascript/oojs/json/superheroes.json")
    print(data_json)

except requests.ConnectionError:
    print("Connection timeout")