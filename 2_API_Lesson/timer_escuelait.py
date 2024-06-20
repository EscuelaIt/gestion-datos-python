import requests
import json

base_url = 'https://timer.escuelait.com/'

register_path = 'api/auth/register'
login_path = 'api/auth/login'
user_path = 'api/auth/user'

password = '3scul41t'

# Register User
'''

body = {
    'name': 'Jean Pierre Mandujano',
    'email': 'jeanpierre@escuelait.com',
    'password': password
}
response = requests.post(base_url + register_path, data=body)

print(response.status_code)
print(response.text)
'''

# Login / Get User

body = {
    'email': 'jeanpierre@escuelait.com',
    'password': password
}

response = requests.post(base_url + login_path, data=body)
dict = json.loads(response.text)
token = dict['token']

print(token)

headers = {
    'Authorization': 'Bearer ' + token,
    'Accept': 'application/json',
    'X-Requested-With': 'XMLHttpRequest'
}

response = requests.get(base_url + user_path, headers=headers)

print(response.text)
