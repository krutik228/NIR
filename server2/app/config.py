import os

HOST = os.environ.get('HOST')
DB_USER = os.environ.get('DB_USER')
DB_NAME = os.environ.get('DB_NAME')
DB_HOST = os.environ.get('DB_HOST')
DB_PASSWORD = os.environ.get('DB_PASSWORD')

REQUEST_METHODS = {
    'post': 'POST',
    'get': 'GET'
}
