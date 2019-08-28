from ..common import HypoEndpointAbstract
from requests.models import Response


class Profile(HypoEndpointAbstract):
    api_path: str = '/profile'

    def __call__(self) -> Response:
        """
        Fetch profile information for the currently-authenticated user.
        https://h.readthedocs.io/en/latest/api-reference/#tag/profile/paths/~1profile/get
        """
        response = self.http.get(self.url)
        return self._handle_response(response)

    def groups(self) -> Response:
        """
        Fetch the groups for which the currently-authenticated user is a member
        https://h.readthedocs.io/en/latest/api-reference/#tag/profile/paths/~1profile~1groups/get
        """
        url = f"{self.url}/groups"
        response = self.http.get(url)
        return self._handle_response(response)
