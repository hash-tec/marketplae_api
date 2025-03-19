import requests
from getpass import getpass


username = input("What is your email? \n")
password = getpass("What is your password? \n")
login_endpoint = "http://127.0.0.1:8000/api/token/"
login_response = requests.post(login_endpoint, json={"email":username, "password": password})
print(login_response.json()['access'])


if login_response.status_code == 200:
    access_code = login_response.json()['access']
    endpoints = "http://127.0.0.1:8000/api/products/update/3/"
    data = {"product_name": "Third brand patch" }
    headers = {
        "Authorization": f"Bearer {access_code}" 
    }
    get_response = requests.put(endpoints, json=data, headers=headers)
    print(get_response.json())