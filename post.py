import requests

req = requests.post(
    url='http://127.0.0.2:80',
    data={
        '_target': 'http://127.0.0.1:443',
        'name': 'nikita2', 'last_name': 'krutikov2'
    }
)
print(req.text)