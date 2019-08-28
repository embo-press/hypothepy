import requests
from typing import Dict
from requests.models import Response


class HttpClient:
    def __init__(self, default_headers: Dict[str, str] = None) -> None:
        if default_headers is None:
            default_headers = {}
        self._headers = default_headers

    ###########################################################################
    # HTTP Verbs
    #
    def get(self, *args, **kwargs) -> Response:
        kwargs.setdefault('headers', {})
        kwargs['headers'] = {**self._headers, **kwargs['headers']}
        return requests.get(*args, **kwargs)

    def post(self, *args, **kwargs) -> Response:
        kwargs.setdefault('headers', {})
        kwargs['headers'] = {**self._headers, **kwargs['headers']}
        return requests.post(*args, **kwargs)

    def delete(self, *args, **kwargs) -> Response:
        kwargs.setdefault('headers', {})
        kwargs['headers'] = {**self._headers, **kwargs['headers']}
        return requests.delete(*args, **kwargs)

    def put(self, *args, **kwargs) -> Response:
        kwargs.setdefault('headers', {})
        kwargs['headers'] = {**self._headers, **kwargs['headers']}
        return requests.put(*args, **kwargs)

    def patch(self, *args, **kwargs) -> Response:
        kwargs.setdefault('headers', {})
        kwargs['headers'] = {**self._headers, **kwargs['headers']}
        return requests.patch(*args, **kwargs)
