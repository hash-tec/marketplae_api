import requests
from getpass import getpass


username = input("What is your email? \n")
password = getpass("What is your password? \n")
login_endpoint = "http://127.0.0.1:8000/api/token/"
login_response = requests.post(login_endpoint, json={"email":username, "password": password})
print(login_response.json()['access'])


if login_response.status_code == 200:
    access_code = login_response.json()['access']
    endpoints = "http://127.0.0.1:8000/api/v2/products/9/"
    data ={'id': 9, 'seller': 'firstuser@gmail.com', 'discounted_price': 32.0, 'url': 'http://127.0.0.1:8000/api/v2/products/9/', 'product_name': 'Sixth Product', 
           'brand': 'sixth Brand', 'description': 'sixth Description', 'price': '40.00', 
           'discount_percentage': '20', 'category': 'men'}
    headers = {
        "Authorization": f"Bearer {access_code}" 
    }
    get_response = requests.put(endpoints, json=data, headers=headers)
    print(get_response.json())