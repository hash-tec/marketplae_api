import requests


endpoints = "http://127.0.0.1:8000/api/products/delete/13/"
get_response = requests.delete(endpoints)
print(get_response.json())