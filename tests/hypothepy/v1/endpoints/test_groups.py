import responses
import re

from ..common import (
    HypoApiTest,
    TEST_HYPOTHESIS_API_URL,
)

class GroupsGetListTest(HypoApiTest):
    @responses.activate
    def test_it_gets_the_list(self):
        responses.add(
            method=responses.GET,
            url=re.compile(f"{TEST_HYPOTHESIS_API_URL}/*"),
        )

        result = self.hypo.groups.get_list(authority='mycustom.com', document_uri='myDocumentUri')
        self.assertEqual(len(responses.calls), 1)
        self.assertEqual(responses.calls[0].request.method, responses.GET)
        self.assertEqual(responses.calls[0].request.path_url, f"/groups?authority=mycustom.com&document_uri=myDocumentUri")

    @responses.activate
    def test_it_used_hypothesis_as_default_authority(self):
        responses.add(
            method=responses.GET,
            url=re.compile(f"{TEST_HYPOTHESIS_API_URL}/*"),
        )

        result = self.hypo.groups.get_list(document_uri='myDocumentUri')
        self.assertEqual(len(responses.calls), 1)
        self.assertEqual(responses.calls[0].request.method, responses.GET)
        self.assertEqual(responses.calls[0].request.path_url, f"/groups?authority=hypothes.is&document_uri=myDocumentUri")

    @responses.activate
    def test_it_passes_the_expand_attributes(self):
        from hypothepy.v1.endpoints.groups import Expand
        responses.add(
            method=responses.GET,
            url=re.compile(f"{TEST_HYPOTHESIS_API_URL}/*"),
        )

        result = self.hypo.groups.get_list(expand=[Expand.ORGANIZATION, Expand.SCOPES])
        self.assertEqual(len(responses.calls), 1)
        self.assertEqual(responses.calls[0].request.method, responses.GET)
        self.assertEqual(responses.calls[0].request.path_url, f"/groups?authority=hypothes.is&expand=organization&expand=scopes")


class GroupsCreateTest(HypoApiTest):
    @responses.activate
    def test_create_a_new_group(self):
        responses.add(
            method=responses.POST,
            url=re.compile(f"{TEST_HYPOTHESIS_API_URL}/*"),
        )

        result = self.hypo.groups.create(name='EMBO SourceData AI', description='AI links and notes')
        self.assertEqual(len(responses.calls), 1)
        self.assertEqual(responses.calls[0].request.method, responses.POST)
        self.assertEqual(responses.calls[0].request.path_url, f"/groups")
        self.assertEqual(responses.calls[0].request.body, b'{"name": "EMBO SourceData AI", "description": "AI links and notes"}')


class GroupsFetchTest(HypoApiTest):
    @responses.activate
    def test_fetch_a_group(self):
        responses.add(
            method=responses.GET,
            url=re.compile(f"{TEST_HYPOTHESIS_API_URL}/*"),
        )

        group_id = '123456'
        result = self.hypo.groups.fetch(id=group_id)
        self.assertEqual(len(responses.calls), 1)
        self.assertEqual(responses.calls[0].request.method, responses.GET)
        self.assertEqual(responses.calls[0].request.path_url, f"/groups/{group_id}")


class GroupsUpdateTest(HypoApiTest):
    @responses.activate
    def test_update_a_group(self):
        responses.add(
            method=responses.PATCH,
            url=re.compile(f"{TEST_HYPOTHESIS_API_URL}/*"),
        )

        group_id = '123456'
        result = self.hypo.groups.update(id=group_id, name='EMBO SourceData AI', description='AI links and notes')
        self.assertEqual(len(responses.calls), 1)
        self.assertEqual(responses.calls[0].request.method, responses.PATCH)
        self.assertEqual(responses.calls[0].request.path_url, f"/groups/{group_id}")
        self.assertEqual(responses.calls[0].request.body, b'{"name": "EMBO SourceData AI", "description": "AI links and notes"}')


class GroupsCreateOrUpdateTest(HypoApiTest):
    @responses.activate
    def test_creates_or_updates_a_group(self):
        responses.add(
            method=responses.PUT,
            url=re.compile(f"{TEST_HYPOTHESIS_API_URL}/*"),
        )

        group_id = '123456'
        result = self.hypo.groups.create_or_update(id=group_id, name='EMBO SourceData AI', description='AI links and notes')
        self.assertEqual(len(responses.calls), 1)
        self.assertEqual(responses.calls[0].request.method, responses.PUT)
        self.assertEqual(responses.calls[0].request.path_url, f"/groups/{group_id}")
        self.assertEqual(responses.calls[0].request.body, b'{"name": "EMBO SourceData AI", "description": "AI links and notes"}')

class GroupsMembersTest(HypoApiTest):
    @responses.activate
    def test_retrieves_the_groups_members(self):
        responses.add(
            method=responses.GET,
            url=re.compile(f"{TEST_HYPOTHESIS_API_URL}/*"),
        )
        group_id = '123456'
        result = self.hypo.groups.members(group_id)
        self.assertEqual(len(responses.calls), 1)
        self.assertEqual(responses.calls[0].request.method, responses.GET)
        self.assertEqual(responses.calls[0].request.path_url, f"/groups/{group_id}/members")


class GroupsAddMemberTest(HypoApiTest):
    def test_it_raises_a_not_implemented_error(self):
        with self.assertRaises(NotImplementedError):
            group_id = '123456'
            user = 'acct:EMBO@hypothes.is'
            self.hypo.groups.add_member(group_id, user)



class GroupsRemoveMemberTest(HypoApiTest):
    @responses.activate
    def test_removes_yourself_from_a_group(self):
        responses.add(
            method=responses.DELETE,
            url=re.compile(f"{TEST_HYPOTHESIS_API_URL}/*"),
        )
        group_id = '123456'
        result = self.hypo.groups.remove_member(group_id)
        self.assertEqual(len(responses.calls), 1)
        self.assertEqual(responses.calls[0].request.method, responses.DELETE)
        self.assertEqual(responses.calls[0].request.path_url, f"/groups/{group_id}/members/me")
