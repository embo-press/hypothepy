import responses
import re
import unittest

from .common import HypoApiTest, TEST_USER_NAME

class HelpersPermissionTest(HypoApiTest):
    def test_read_all_preset(self):
        self.assertEqual(
            self.hypo.helpers.permissions.READ_ALL,
            {
                'read': ['group:__world__'],
                'update': [f'acct:{TEST_USER_NAME}@hypothes.is'],
                'delete': [f'acct:{TEST_USER_NAME}@hypothes.is'],
                'admin': [f'acct:{TEST_USER_NAME}@hypothes.is'],
            }
        )

    def test_create_new_permissions(self):
        read   = ['group:MyGroup']
        update = ['group:MyGroup', 'acct:MyExternalCollaborator@hypothes.is']
        delete = ['acct:MyUserName@hypothes.is']
        admin  = ['acct:MyUserName@hypothes.is']
        self.assertEqual(
            self.hypo.helpers.permissions(
                read=read,
                update=update,
                delete=delete,
                admin=admin,
            ),
            {
                'read':read,
                'update':update,
                'delete':delete,
                'admin':admin,
            }
        )

    def test_converts_params_to_list(self):
        user_account = 'acct:MyUserName@hypothes.is'
        permissions = self.hypo.helpers.permissions(read=user_account)
        self.assertEqual(permissions, { 'read': [user_account] })