import requests
from getpass import getpass

email= input("What is your email?\n")
password = getpass("Your password?\n")

# register_endpoints = "http://127.0.0.1:8000/api/register/"

register_data= {"first_name": "First", "last_name": "person", 
     "email":email,"password": password,"password2":password, "gender":"M"}
register_response = requests.post(register_endpoints, json=register_data)






