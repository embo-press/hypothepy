from ...utils.functions import remove_empty
from ..common import HypoEndpointAbstract
from requests.models import Response
import enum
from enum import Enum
from typing import List


@enum.unique
class Expand(Enum):
    ORGANIZATION = "organization"
    SCOPES = "scopes"


class Groups(HypoEndpointAbstract):
    '''
    Full representation of Groups resource and applicable relationships.
    https://h.readthedocs.io/en/latest/api-reference/#tag/groups
    '''

    api_path: str = '/groups'

    def get_list(self,
                 authority: str = 'hypothes.is',
                 document_uri: str = None,
                 expand: List[Expand] = None,
                 ) -> Response:
        """
        Retrieve a list of applicable Groups, filtered by authority and target
        document (document_uri). Also retrieve user's private Groups.
        https://h.readthedocs.io/en/latest/api-reference/#tag/groups/paths/~1groups/get
        """
        if expand is None:
            expand = []
        payload = {
            'authority': authority,
            'document_uri': document_uri,
            'expand': list(map(lambda enum: enum.value, expand)),
        }
        response = self.http.get(self.url, params=remove_empty(payload))
        return self._handle_response(response)

    def create(self,
               name: str,
               description: str = None,
               groupid: str = None,
               ) -> Response:
        """
        Create a new, private group for the currently-authenticated user
        https://h.readthedocs.io/en/latest/api-reference/#tag/groups/paths/~1groups/post
        """
        payload = {
            'name': name,
            'description': description,
            'groupid': groupid,
        }
        response = self.http.post(self.url, json=remove_empty(payload))
        return self._handle_response(response)

    def fetch(self,
              id: str,
              expand: List[Expand] = None,
              ) -> Response:
        """
        Fetch a single Group resource
        https://h.readthedocs.io/en/latest/api-reference/#tag/groups/paths/~1groups~1{id}/get
        """
        if expand is None:
            expand = []
        payload = {
            'expand': list(map(lambda enum: enum.value, expand)),
        }
        url = f"{self.url}/{id}"
        response = self.http.get(url, params=remove_empty(payload))
        return self._handle_response(response)

    def update(self,
               id: str,
               name: str = None,
               description: str = None,
               groupid: str = None,
               ) -> Response:
        """
        Update a Group resource.
        https://h.readthedocs.io/en/latest/api-reference/#tag/groups/paths/~1groups~1{id}/patch
        """
        payload = {
            'name': name,
            'description': description,
            'groupid': groupid,
        }
        url = f"{self.url}/{id}"
        response = self.http.patch(url, json=remove_empty(payload))
        return self._handle_response(response)

    def create_or_update(self,
                         id: str,
                         name: str,
                         description: str = None,
                         groupid: str = None,
                         ) -> Response:
        """
        Update the group with the indicated id or create one if it does not
        exist.
        https://h.readthedocs.io/en/latest/api-reference/#tag/groups/paths/~1groups~1{id}/put
        """
        payload = {
            'name': name,
            'description': description,
            'groupid': groupid,
        }
        url = f"{self.url}/{id}"
        response = self.http.put(url, json=remove_empty(payload))
        return self._handle_response(response)

    def members(self, id: str) -> Response:
        """
        Fetch a list of all members (users) in a group. Returned user resource
        only contains public-facing user data. Authenticated user must have
        read access to the group. Does not require authentication for reading
        members of public groups. Returned members are unsorted.
         https://h.readthedocs.io/en/latest/api-reference/#tag/groups/paths/~1groups~1{id}~1members/get
        """
        url = f"{self.url}/{id}/members"
        response = self.http.get(url)
        return self._handle_response(response)

    def add_member(self, *args, **kwargs) -> Response:
        """
        Add a user as a member to a group. This endpoint is only accessible to
        requests authenticated with AuthClient credentials and is restricted to
        users and groups within the associated authority.
        https://h.readthedocs.io/en/latest/api-reference/#tag/groups/paths/~1groups~1{id}~1members/get
        """
        raise NotImplementedError(
            "only accessible to requests authenticated with AuthClient")

    def remove_member(self, id: str) -> Response:
        """
        Remove a user from a group. At present, this endpoint only allows the
        removal as one's self (authenticated with API Key) from the indicated
        group
        https://h.readthedocs.io/en/latest/api-reference/#tag/groups/paths/~1groups~1{id}~1members~1{user}/delete
        """

        user = "me"  # Currently, only the literal value "me" is accepted.
        #              See the official hypothes.is documentation
        url = f"{self.url}/{id}/members/{user}"
        response = self.http.delete(url)
        return self._handle_response(response)
