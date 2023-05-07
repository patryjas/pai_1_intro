
# V1
# import json
# import requests
#
# url = "https://mdn.github.io/learning-area/javascript/oojs/json/superheroes.json"
#
# try:
#     response = requests.get(url)
#     response.raise_for_status()
#     data = json.loads(response.text)
#     json_data = json.dumps(data, indent=4)
#     print(json_data)
# except requests.exceptions.HTTPError as http_err:
#     print(f"HTTP error occurred: {http_err}")
# except json.JSONDecodeError as json_err:
#     print(f"JSON decoding error occurred: {json_err}")
# except Exception as err:
#     print(f"An error occurred: {err}")

# V2
# import json
# import requests
#
# url = "https://httpbin.org/post"
# data = {"name": "natalia"}
# headers = {"Content-Type": "application/json"}
#
# try:
#     response = requests.post(url, data=json.dumps(data), headers=headers)
#     response.raise_for_status()
#     response_data = response.json()
#     print(json.dumps(response_data, indent=4))
# except requests.exceptions.HTTPError as http_err:
#     print(f"HTTP error occurred: {http_err}")
# except json.JSONDecodeError as json_err:
#     print(f"JSON decoding error occurred: {json_err}")
# except Exception as err:
#     print(f"An error occurred: {err}")

# V3
import json
import requests

url = "https://httpbin.org/delay/2"
data = {"name": "natalia"}
headers = {"Content-Type": "application/json"}

def make_request():
    response = requests.post(url, data=json.dumps(data), headers=headers, timeout=(1,3))
    response.raise_for_status()
    response_data = response.json()
    return response_data

try:
    response_data = make_request()
    print(json.dumps(response_data, indent=4))
except requests.exceptions.Timeout:
    print("The request timed out.")
except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")
except json.JSONDecodeError as json_err:
    print(f"JSON decoding error occurred: {json_err}")
except Exception as err:
    print(f"An error occurred: {err}")

