import requests

from config import PROXY_NETWORK_URL, TARGET_URL_ARGUMENT_NAME


def request_proxy(method, url, **kwargs):
    if kwargs.get('data'):
        if kwargs['data'].get(TARGET_URL_ARGUMENT_NAME):
            raise TypeError('Argument name "_target" is reserved')
    kwargs['data'][TARGET_URL_ARGUMENT_NAME] = url
    return requests.request(method, PROXY_NETWORK_URL, **kwargs).text


if __name__ == '__main__':
    req = request_proxy(
        method='POST',
        url='http://127.0.0.1:443',
        data={
            'name': 'nikita2', 'last_name': 'krutikov2'
        }
    )
    print(req)
