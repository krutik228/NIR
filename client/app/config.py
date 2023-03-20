import os

PROXY_URL = os.environ.get('PROXY_URL', ' http://127.0.0.1:80')
SERVER_NETWORK_URL = os.environ.get('SERVER_NETWORK_URL')
PROXY_NETWORK_URL = os.environ.get('PROXY_NETWORK_URL', 'http://proxy:80/')

SERVER_URLS = ('http://127.0.0.1:443', 'http://172.20.0.3:443')
PROXY_URLS = ('http://127.0.0.1:80', 'http://172.20.0.3:443')

TARGET_URL_ARGUMENT_NAME = '_target'

print()
