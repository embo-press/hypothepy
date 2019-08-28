import responses
import re

from ..common import (
    HypoApiTest,
    TEST_HYPOTHESIS_API_URL,
)

class GeneralTest(HypoApiTest):
    @responses.activate
    def test_general(self):
        responses.add(
            method=responses.GET,
            url=re.compile(f"{TEST_HYPOTHESIS_API_URL}/*"),
        )

        result = self.hypo.general()
        self.assertEqual(len(responses.calls), 1)
        self.assertEqual(responses.calls[0].request.method, responses.GET)
        self.assertEqual(responses.calls[0].request.path_url, f"/")
