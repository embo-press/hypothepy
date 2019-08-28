from ..utils.http_client import HttpClient
from .endpoints.annotations import Annotations
from .endpoints.general import General
from .endpoints.groups import Groups
from .endpoints.profile import Profile
from .helpers import Helpers
API_URL = 'https://api.hypothes.is/api'


class HypoApi:
    def __init__(
        self,
        api_key: str,
        user_name: str,
        base_url: str = None,
    ) -> None:
        if base_url is None:
            base_url = API_URL
        self._base_url = base_url
        self._api_key = api_key
        self._user_name = user_name
        self._http = HttpClient(
            default_headers={
                'Authorization': f"Bearer {self._api_key}",
                'content-type': 'application/json',
                'Accept': 'application/vnd.hypothesis.v1+json',
            }
        )
        self.annotations = Annotations(
            base_url=self._base_url,
            http=self._http,
        )
        self.general = General(
            base_url=self._base_url,
            http=self._http,
        )
        self.groups = Groups(
            base_url=self._base_url,
            http=self._http,
        )
        self.profile = Profile(
            base_url=self._base_url,
            http=self._http,
        )
        self.helpers = Helpers(self._user_name)
