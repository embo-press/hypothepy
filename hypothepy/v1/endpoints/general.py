from ..common import HypoEndpointAbstract
from requests.models import Response


class General(HypoEndpointAbstract):
    '''
    Provides a list of links to resources offered by the API.
    https://h.readthedocs.io/en/latest/api-reference/#tag/general
    '''

    api_path: str = '/'

    def __call__(self) -> Response:
        response = self.http.get(self.url)
        return self._handle_response(response)
