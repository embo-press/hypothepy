import responses
import re

from ..common import (
    HypoApiTest,
    TEST_HYPOTHESIS_API_URL,
)

class AnnotationSearchTest(HypoApiTest):
    @responses.activate
    def test_search(self):
        responses.add(
            method=responses.GET,
            url=re.compile(f"{TEST_HYPOTHESIS_API_URL}/*"),
        )

        result = self.hypo.annotations.search(limit=20, sort='updated', order='asc')
        self.assertEqual(len(responses.calls), 1)
        self.assertEqual(responses.calls[0].request.method, responses.GET)
        self.assertEqual(responses.calls[0].request.path_url, f"/search?limit=20&sort=updated&order=asc")

class AnnotationCreateTest(HypoApiTest):
    @responses.activate
    def test_it_creates_a_new_annotation(self):
        responses.add(
            method=responses.POST,
            url=re.compile(f"{TEST_HYPOTHESIS_API_URL}/*"),
        )

        result = self.hypo.annotations.create(
            uri='www.google.com',
            text='test'
        )
        self.assertEqual(len(responses.calls), 1)
        self.assertEqual(responses.calls[0].request.path_url, f"/annotations")
        self.assertEqual(responses.calls[0].request.method, responses.POST)
        self.assertEqual(responses.calls[0].request.body, b'{"uri": "www.google.com", "text": "test"}')

class AnnotationFetchTest(HypoApiTest):
    @responses.activate
    def test_it_fetches_an_annotation(self):
        responses.add(
            method=responses.GET,
            url=re.compile(f"{TEST_HYPOTHESIS_API_URL}/*"),
        )
        annotation_id = 'xxx'
        result = self.hypo.annotations.fetch(annotation_id)
        self.assertEqual(len(responses.calls), 1)
        self.assertEqual(responses.calls[0].request.method, responses.GET)
        self.assertEqual(responses.calls[0].request.path_url, f"/annotations/{annotation_id}")

class AnnotationUpdateTest(HypoApiTest):
    @responses.activate
    def test_it_updates_an_annotation(self):
        responses.add(
            method=responses.PATCH,
            url=re.compile(f"{TEST_HYPOTHESIS_API_URL}/*"),
        )
        annotation_id = 'xxx'
        result = self.hypo.annotations.update(annotation_id)
        self.assertEqual(len(responses.calls), 1)
        self.assertEqual(responses.calls[0].request.method, responses.PATCH)
        self.assertEqual(responses.calls[0].request.path_url, f"/annotations/{annotation_id}")

    def test_it_runs_a_real_update(self):
        if False:
            from src.hypo.v1.api import HypoApi
            from datetime import datetime
            API_KEY=''
            USER_NAME=''
            hypo = HypoApi(
                api_key=API_KEY,
                user_name=USER_NAME,
            )
            annotation_id = 'K-kIAMM5EemXcd8fXjKg1A'
            result = hypo.annotations.update(annotation_id, text=f"updating from tests - {datetime.now()}")
            self.assertEqual(result.status_code, 200)

class AnnotationDeleteTest(HypoApiTest):
    @responses.activate
    def test_it_deletes_an_annotation(self):
        responses.add(
            method=responses.DELETE,
            url=re.compile(f"{TEST_HYPOTHESIS_API_URL}/*"),
        )
        annotation_id = 'xxx'
        result = self.hypo.annotations.delete(annotation_id)
        self.assertEqual(len(responses.calls), 1)
        self.assertEqual(responses.calls[0].request.method, responses.DELETE)
        self.assertEqual(responses.calls[0].request.path_url, f"/annotations/{annotation_id}")


class AnnotationFlagTest(HypoApiTest):
    @responses.activate
    def test_it_flags_an_annotation(self):
        responses.add(
            method=responses.PUT,
            url=re.compile(f"{TEST_HYPOTHESIS_API_URL}/*"),
        )
        annotation_id = 'xxx'
        result = self.hypo.annotations.flag(annotation_id)
        self.assertEqual(len(responses.calls), 1)
        self.assertEqual(responses.calls[0].request.method, responses.PUT)
        self.assertEqual(responses.calls[0].request.path_url, f"/annotations/{annotation_id}/flag")

class AnnotationHideTest(HypoApiTest):
    @responses.activate
    def test_it_hides_an_annotation(self):
        responses.add(
            method=responses.PUT,
            url=re.compile(f"{TEST_HYPOTHESIS_API_URL}/*"),
        )
        annotation_id = 'xxx'
        result = self.hypo.annotations.hide(annotation_id)
        self.assertEqual(len(responses.calls), 1)
        self.assertEqual(responses.calls[0].request.method, responses.PUT)
        self.assertEqual(responses.calls[0].request.path_url, f"/annotations/{annotation_id}/hide")

class AnnotationShowTest(HypoApiTest):
    @responses.activate
    def test_it_shows_an_annotation(self):
        responses.add(
            method=responses.DELETE,
            url=re.compile(f"{TEST_HYPOTHESIS_API_URL}/*"),
        )
        annotation_id = 'xxx'
        result = self.hypo.annotations.show(annotation_id)
        self.assertEqual(len(responses.calls), 1)
        self.assertEqual(responses.calls[0].request.method, responses.DELETE)
        self.assertEqual(responses.calls[0].request.path_url, f"/annotations/{annotation_id}/hide")


