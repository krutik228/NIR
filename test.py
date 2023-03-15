import requests
import ssl
import flask

req = requests.post('http://localhost:443/post', {'first_name': 'nikita', 'last_name': 'krutikov'})
print(req.text)
# requests.get('https://google.com', verify=False)
# print(ssl.OPENSSL_VERSION)

# flask.request.

