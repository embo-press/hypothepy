from ...utils.functions import remove_empty
from ..common import HypoEndpointAbstract
from requests.models import Response


class Annotations(HypoEndpointAbstract):
    '''
    Full representation of Annotation resource and applicable relationships.
    https://h.readthedocs.io/en/latest/api-reference/#tag/annotations
    '''

    api_path: str = '/annotations'

    def create(
        self,
        uri,
        document='',
        text='',
        tags=[],
        group='',
        permissions={},
        target='',
        references=[]
    ) -> Response:
        '''
        Create a new Annotation.
        https://h.readthedocs.io/en/latest/api-reference/#tag/annotations/paths/~1annotations/post
        '''

        payload = {
            'uri': uri,
            'document': document,
            'text': text,
            'tags': tags,
            'group': group,
            'permissions': permissions,
            'target': target,
            'references': references

        }
        response = self.http.post(self.url, json=remove_empty(payload))
        return self._handle_response(response)

    def search(
        self,
        limit=20,
        sort='updated',
        search_after='',
        offset=0,
        order='desc',
        uri='',
        uri_parts='',
        wildcard_uri='',
        user='',
        group='',
        tag='',
        tags=[],
        any='',
        quote='',
        references='',
        text='',
    ) -> Response:
        '''
        Search for Annotations.
        https://h.readthedocs.io/en/latest/api-reference/v1/#tag/annotations/paths/~1search/get
        '''

        url = self.base_url + '/search'
        payload = {
            'limit': limit,
            'sort': sort,
            'search_after': search_after,
            'offset': offset,
            'order': order,
            'uri': uri,
            'uri_parts': uri_parts,
            'wildcard_uri': wildcard_uri,
            'user': user,
            'group': group,
            'tag': tag,
            'tags': tags,
            'any': any,
            'quote': quote,
            'references': references,
            'text': text,
        }

        response = self.http.get(url, params=remove_empty(payload))
        return self._handle_response(response)

    def fetch(self, id) -> Response:
        '''
        Fetch an Annotation.
        https://h.readthedocs.io/en/latest/api-reference/#tag/annotations/paths/~1annotations~1{id}/get
        '''

        response = self.http.get(f"{self.url}/{id}")
        return self._handle_response(response)

    def update(
        self,
        id,
        uri=None,
        document=None,
        text=None,
        tags=None,
        group=None,
        permissions=None,
        target=None,
        references=None,
    ) -> Response:
        '''
        Update an Annotation. This endpoint has PATCH-characteristics as
        defined in RFC5789,
        meaning the request body does not have to include
        the whole annotation object.
        https://h.readthedocs.io/en/latest/api-reference/#tag/annotations/paths/~1annotations~1{id}/patch
        '''

        payload = {
            'uri': uri,
            'document': document,
            'text': text,
            'tags': tags,
            'group': group,
            'permissions': permissions,
            'target': target,
            'references': references
        }

        response = self.http.patch(
            f"{self.url}/{id}", json=remove_empty(payload))
        return self._handle_response(response)

    def delete(self, id) -> Response:
        '''
        Delete an Annotation.
        https://h.readthedocs.io/en/latest/api-reference/#tag/annotations/paths/~1annotations~1{id}/delete
        '''

        url = self.url + f"/{id}"
        response = self.http.delete(url)
        return self._handle_response(response)

    def flag(self, id) -> Response:
        '''
        Flag an annotation for review (moderation). The moderator of the group
        containing the annotation will be notified of the flag and can decide
        whether or not to hide the annotation. Note that flags persist and
        cannot be removed once they are set.
        https://h.readthedocs.io/en/latest/api-reference/#tag/annotations/paths/~1annotations~1{id}~1flag/put
        '''

        url = self.url + f"/{id}/flag"
        response = self.http.put(url)
        return self._handle_response(response)

    def hide(self, id) -> Response:
        '''
        Hide an annotation. The authenticated user needs to have the moderate
        permission for the group that contains the annotation—this permission
        is granted to the user who created the group.
        https://h.readthedocs.io/en/latest/api-reference/#tag/annotations/paths/~1annotations~1{id}~1hide/put
        '''

        url = self.url + f"/{id}/hide"
        response = self.http.put(url)
        return self._handle_response(response)

    def show(self, id) -> Response:
        '''
        Show/"un-hide" an annotation. The authenticated user needs to have the
        moderate permission for the group that contains the annotation—this
        permission is granted to the user who created the group.
        https://h.readthedocs.io/en/latest/api-reference/#tag/annotations/paths/~1annotations~1{id}~1hide/delete
        '''

        url = self.url + f"/{id}/hide"
        response = self.http.delete(url)
        return self._handle_response(response)
