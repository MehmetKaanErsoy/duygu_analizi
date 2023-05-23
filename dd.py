import requests

url = 'http://localhost:8000/login/'
data = {
    'username': 'myusername',
    'password': 'mypassword'
}
response = requests.post(url, data=data)

print(response.json())
