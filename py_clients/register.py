import requests
from getpass import getpass

endpoints = "http://127.0.0.1:8000/api/register/"
password = getpass()
data= {"first_name": "First", "last_name": "person", 
     "email":"firstperson@gmail.com","password": password,"password2":password, "gender":"M"}
get_response = requests.post(endpoints, json=data)

print(get_response.json())