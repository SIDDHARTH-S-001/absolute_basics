import requests
import json

api_url = "https://jsonplaceholder.typicode.com/todos/1"
response = requests.get(api_url).json()
with open("response.json", "w", encoding="utf-8") as write_file:
    json.dump(response, write_file)
