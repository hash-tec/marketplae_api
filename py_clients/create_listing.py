import requests
from getpass import getpass


username = input("What is your email? \n")
password = getpass("What is your password? \n")
login_endpoint = "http://127.0.0.1:8000/api/token/"
login_response = requests.post(login_endpoint, json={"email":username, "password": password})
print(login_response.json()['access'])


if login_response.status_code == 200:
    access_code = login_response.json()['access']
    endpoints = "http://127.0.0.1:8000/api/products/listing/"
    data = {"product_name":"First Product", "brand": "First Brand", 
            "description": "first Description",
            "price": 40 }
    headers = {
        "Authorization": f"Bearer {access_code}" 
    }
    get_response = requests.post(endpoints, json=data, headers=headers)
    print(get_response.json())

# endpoints = "http://127.0.0.1:8000/api/products/listing/"
# data = {"product_name":"second Product", "brand": "second Brand", "description": "second Description",
#             "price": 40 }
# get_response = requests.post(endpoints, json=data)
# print(get_response.json())