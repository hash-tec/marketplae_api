import requests

endpoints = "http://127.0.0.1:8000/api/cart/"
data = {"product_name":"Sixth Product cart", "brand": "sixth Brand", 
            "description": "sixth Description",
            "price": 40, "category": "men" }

get_response = requests.post(endpoints, json=data)
print(get_response.json())