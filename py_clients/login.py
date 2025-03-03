import requests
from getpass import getpass

email= input("What is your email?\n")
password = getpass("Your password?\n")

login_endpoints = "http://127.0.0.1:8000/api/token/"
view = "http://127.0.0.1:8000/api/testing/"

login_data = {"email": email, "password": password}
login_response = requests.post(login_endpoints, json=login_data)
print(login_response.json())
if login_response.status_code == 200:
    access_code =  login_response.json()["access"]
    headers = {
        "Authorization": f"Bearer {access_code}",
    }
    view_response = requests.get(view, headers=headers)
    print(view_response.json())