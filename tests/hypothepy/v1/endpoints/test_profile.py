import responses
import re

from ..common import (
    HypoApiTest,
    TEST_HYPOTHESIS_API_URL,
)


class ProfileTest(HypoApiTest):
    @responses.activate
    def test_get_users_profile(self):
        responses.add(
            method=responses.GET,
            url=re.compile(f"{TEST_HYPOTHESIS_API_URL}/*"),
        )

        result = self.hypo.profile()
        self.assertEqual(len(responses.calls), 1)
        self.assertEqual(responses.calls[0].request.method, responses.GET)
        self.assertEqual(responses.calls[0].request.path_url, f"/profile")

class ProfileGroupsTest(HypoApiTest):
    @responses.activate
    def test_get_users_groups(self):
        responses.add(
            method=responses.GET,
            url=re.compile(f"{TEST_HYPOTHESIS_API_URL}/*"),
        )

        result = self.hypo.profile.groups()
        self.assertEqual(len(responses.calls), 1)
        self.assertEqual(responses.calls[0].request.method, responses.GET)
        self.assertEqual(responses.calls[0].request.path_url, f"/profile/groups")
