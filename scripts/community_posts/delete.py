import requests
import json

AUTH_ENDPOINT = 'http://127.0.0.1:8000/api/token/'

user_data = {
    'email':'girik1105@gmail.com',
    'password':'TestPassword'
}

headers = {
    "Content-Type": "application/json",
}

r = requests.post(AUTH_ENDPOINT, data=json.dumps(user_data), headers=headers)
token = r.json()['access']

print('Authorization call:', r.status_code)
print('JWT TOken Recieved:', token)

headers2 = {
    "Content-Type": "application/json",
    "Authorization": "JWT " + token,
}

ENDPOINT = "http://127.0.0.1:8000/api/communities/test-community/posts/4/delete/"

r = requests.delete(ENDPOINT,  headers=headers2)
print("Response:", r.status_code)
print(r.json())