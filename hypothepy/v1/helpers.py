"""
A collection of handy helpers meant to facilitate creating some common objects
required by the hypothes.is API.


All of them are grouped under a general `Helpers` class, that after
instantiating it give shorthand access to the methods and may save some typing
and importing.

None of these are intended for direct, a handy shortcut is offered through the
HypoApi instance, eg:

    ```
    hypo = HypoApi(api_key='...', user_name='...')
    hypo.helpers.permissions.READ_ALL
    ```


In the end they all return a dictionary representation of the given parameters.
It is arguable how much value this helpers can add. At the very least they may
help you remember the parameters that this different objects require through
you editor hints.

At present only `Permissions` and `Documents` are supported. More helpers will
be added as requested, for example: `Dc`, `HighWire`, `Link`...
"""

from typing import Dict
from ..utils.functions import remove_empty


class PermissionsHelper:
    """
    PermissionsHelper will provide some sensible predefined defaults for direct
    usage.
    At the moment only one default is provided:

        - `READ_ALL`: open for everyone to read, but only you have write,
        delete and admin privileges

    Example of usage:

        ```
        permissions_helper = PermissionsHelper(user_name='MyUserName')
        permissions_helper.READ_ALL.dict()
            # => {
            #     'read': ['group:__world__'],
            #     'update': ['acct:MyUserName@hypothes.is'],
            #     'delete': ['acct:MyUserName@hypothes.is'],
            #     'admin': ['acct:MyUserName@hypothes.is'],
            # }
        ```

    It may also be used to create your own custom set of permissions that can
    be passed to api calls:

        ```
        permissions_helper(
            read   = [
                'acct:MyUserName@hypothes.is',
                'acct:MyFriendsUserName@hypothesis.is',
            ],
            update = ['acct:MyUserName@hypothes.is'],
            delete = ['acct:MyUserName@hypothes.is'],
            admin  = ['acct:MyUserName@hypothes.is'],
        )
        ```
    """

    def __init__(self,
                 user_name: str,
                 authority: str = 'hypothes.is'
                 ):
        user_account = f'acct:{user_name}@{authority}'

        self.GROUP_WORLD = 'group:__world__'
        self.READ_ALL = {
            'read': [self.GROUP_WORLD],
            'update': [user_account],
            'delete': [user_account],
            'admin': [user_account],
        }

    def __call__(self, read=[], update=[], delete=[], admin=[]) -> Dict:
        """
        Returns a dictionary including only the permissions that have been set.
        It ensures that all set permissions are inside of a list.
        """
        permissions = {
            'read': self._to_list(read),
            'update': self._to_list(update),
            'delete': self._to_list(delete),
            'admin': self._to_list(admin),
        }
        return remove_empty(permissions)

    def _to_list(self, input):
        if isinstance(input, list):
            return input
        return [input]

class DcHelper:
    def __call__(self, identifier=[]):
        dc = {'identifier': identifier}
        return remove_empty(dc)

class HighwireHelper:
    def __call__(self, doi=[], pdf_url=[]) -> Dict:
        highwire = {
            'doi': doi,
            'pdf_url': pdf_url,
        }
        return remove_empty(highwire)

class LinkHelper:
    def __call__(self, href, type=''):
        link = {
            'href': href,
            'type': type,
        }
        return link

class DocumentsHelper:
    def __call__(self, title='', dc={}, highwire={}, link=[]) -> Dict:
        document = {
            'title': title,
            'dc': dc,
            'highwire': highwire,
            'link': link,
        }
        return remove_empty(document)


class Helpers:
    def __init__(self, user_name):
        self.permissions = PermissionsHelper(user_name=user_name)
        self.highwire = HighwireHelper()
        self.dc = DcHelper()
        self.link = LinkHelper()
        self.documents = DocumentsHelper()
