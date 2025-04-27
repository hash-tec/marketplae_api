import requests
from getpass import getpass
from login import login
endpoints = "http://127.0.0.1:8000/api/review/1/"
headers = login()
data = {'comment': 'nice product', 'rating': 3}
get_response = requests.post(endpoints, json=data, headers=headers)
print(get_response.json())

# endpoints = "http://127.0.0.1:8000/api/products/listing/"
# data = {"product_name":"second Product", "brand": "second Brand", "description": "second Description",
#             "price": 40 }
# get_response = requests.post(endpoints, json=data)
# print(get_response.json())