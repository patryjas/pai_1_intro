from urllib.request import urlopen
import json

url = "https://mdn.github.io/learning-area/javascript/oojs/json/superheroes.json"

response = urlopen(url)
data_json = json.loads(response.read())

print(data_json)
