import os

REQUEST_METHODS = {
    'post': 'POST',
    'get': 'GET'
}

HOST = os.environ.get('HOST')
SERVER_NETWORK_URL = os.environ.get('SERVER_NETWORK_URL')

TARGET_URL_ARGUMENT_NAME = '_target'

SERVER_URLS = ('http://127.0.0.1:443', 'http://172.20.0.3:443')
