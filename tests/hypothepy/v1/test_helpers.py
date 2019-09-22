import responses
import re
import unittest

from .common import HypoApiTest, TEST_USER_NAME

class test_new_dc(HypoApiTest):
    def test_create_dc(self):
        identifier = 'my_identifier'
        tested = self.hypo.helpers.dc(identifier=[identifier])
        expected = {'identifier': [identifier]}
        self.assertEqual(tested, expected)

class test_new_link(HypoApiTest):
    def test_create_link(self):
        href = 'my_href'
        type = 'my_type'
        tested = self.hypo.helpers.link(
            href=href,
            type=type
        )
        expected = {
            'href': href,
            'type': type,
        }
        self.assertEqual(tested, expected)

class HelpersHighwireTest(HypoApiTest):
    def test_create_new_highwire(self):
        tested = self.hypo.helpers.highwire(
            doi=['my_doi_123'],
            pdf_url='my_pdf_url_123'
        )
        expected = {
            'doi': ['my_doi_123'],
            'pdf_url': 'my_pdf_url_123'
        }
        self.assertEqual(tested, expected)


class HelpersDocumentTest(HypoApiTest):
    def test_create_new_document(self):
        title = 'my_title'
        doi = 'my_doi'
        identifier = 'my_identifier'
        href = 'my_href'
        type = 'my_type'
        highwire = self.hypo.helpers.highwire(doi=['my_doi'])
        dc = self.hypo.helpers.dc(identifier=[identifier])
        link = self.hypo.helpers.link(href=href, type=type)
        tested = self.hypo.helpers.documents(
            title=title,
            dc=dc,
            highwire=highwire,
            link=[link],
        )
        expected = {
            'title': title,
            'dc': {'identifier': [identifier]},
            'highwire': {
                'doi': [doi],
            },
            'link': [{'href':href, 'type':type}],
        }
        self.assertEqual(tested, expected)

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