import requests
import json

# GET Method.
api_url = "https://jsonplaceholder.typicode.com/todos/1"
get_response = requests.get(api_url)
get_response_info = [get_response.json(), get_response.status_code, get_response.headers["Content-Type"]]

# POST Method.
api_url = "https://jsonplaceholder.typicode.com/todos"
todo = {"userId": 1, "title": "Buy Milk", "completed": False}
post_response = requests.post(api_url, json=todo)
post_response_info = [post_response.json(), post_response.status_code, post_response.headers["Content-Type"]]

with open("post_response.json", "w", encoding="utf-8") as write_file:
    json.dump(post_response_info, write_file, indent=2)
