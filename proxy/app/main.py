import requests

from flask import Flask, request

from config import (
    HOST,
    SERVER_URLS,
    REQUEST_METHODS,
    SERVER_NETWORK_URL,
    TARGET_URL_ARGUMENT_NAME,
)

app = Flask(__name__)


@app.route('/', methods=[*REQUEST_METHODS.values()])
def index():
    args = request.args.copy() or request.form.copy()
    target = args.pop(TARGET_URL_ARGUMENT_NAME)
    if target in SERVER_URLS:
        target = SERVER_NETWORK_URL
        if request.method == REQUEST_METHODS['post']:
            request_data = args.copy()
            if request.form.get('name'):
                request_data.update({'name': f'1:{request.form["name"]}'})
            if request.form.get('last_name'):
                request_data.update({'last_name': f'2:{request.form["last_name"]}'})
            args = request_data

    return requests.request(url=target, method=request.method, data=args).text


if __name__ == '__main__':
    app.run(host=HOST, port=80)
