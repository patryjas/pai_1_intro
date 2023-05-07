### Python vs Python+jmespath


```python
import json
import urllib.request

url = "https://mdn.github.io/learning-area/javascript/oojs/json/superheroes.json"
response = urllib.request.urlopen(url)
data = json.loads(response.read())

for hero in data['members']:
    print(hero['name'])
```


```Python
# Python+jmespath
import json
import urllib.request
import jmespath

url = "https://mdn.github.io/learning-area/javascript/oojs/json/superheroes.json"
response = urllib.request.urlopen(url)
data = json.loads(response.read())

query = "members[].name"
result = jmespath.search(query, data)

for name in result:
    print(name)
```