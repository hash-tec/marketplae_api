import requests
import time
from getpass import getpass
start_time = time.time()
register_endpoints = "http://127.0.0.1:8000/api/register/"
email= input("What is your email?\n")
password = getpass("Your password?\n")
password2 = getpass("Confirm password\n")
register_data= {"first_name": "First", "last_name": "person", 
     "email":email,"password": password,"password2":password, "gender":"M"}
register_response = requests.post(register_endpoints, json=register_data)
print(register_response.json())


# login_data = {'email': email, 'password':password}
# login_endpoints = "http://127.0.0.1:8000/api/token/"
# login_response = requests.post(login_endpoints, json=login_data)
# if login_response.status_code == 200:
#     access_token = login_response.json()['access']
#     print(login_response.json())
#     print(login_response.json()['access'])
#     header = {
#         "authorization": f"Bearer {access_token}"
#     }



end_time = time.time()
print(end_time - start_time)






# header = {
#     "AUTHORIZATION": f"Bearer {}"
# }
# register_response = requests.post(register_endpoints, json=register_data )






