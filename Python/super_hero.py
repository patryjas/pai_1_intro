import json
import urllib.request

url = "https://mdn.github.io/learning-area/javascript/oojs/json/superheroes.json"
response = urllib.request.urlopen(url)
data = json.loads(response.read())

for hero in data['members']:
    print(hero['name'])
