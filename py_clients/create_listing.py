import requests
from login import login


endpoints = "http://127.0.0.1:8000/api/products/listing/"
data = {"product_name":"Sixth Product", "brand": "Sixth Brand", "price":"100",
            "description":"Sixth description", "discount_percentage": "17", "category": "skirts", "size": "xl"}
headers = login()
get_response = requests.post(endpoints, json=data, headers=headers)
print(get_response.json())
