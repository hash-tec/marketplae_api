import requests
from login import login


endpoints = "http://127.0.0.1:8000/api/products/listing/"
data = {"product_name":"Third Product", "brand": "Third Brand", "price":"100",
            "description":"Third description", "discount_percentage": "17", "category": "Man Shoes", "size": "xl"}
headers = login()
get_response = requests.post(endpoints, json=data, headers=headers)
print(get_response.json())
