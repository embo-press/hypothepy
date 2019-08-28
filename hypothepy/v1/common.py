from ..utils.http_client import HttpClient
from requests.models import Response


class HypoEndpointAbstract:
    api_path: str = '/'

    def __init__(self, base_url: str, http: HttpClient) -> None:
        self.base_url: str = base_url
        self.url: str = base_url + self.__class__.api_path
        self.http: HttpClient = http

    def _handle_response(self, response: Response) -> Response:
        return response
