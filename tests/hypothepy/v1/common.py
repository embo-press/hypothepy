import os
import unittest
from hypothepy.v1.api import HypoApi


TEST_HYPOTHESIS_API_URL = 'https://dummy-hypothes.is'
TEST_API_KEY = 'MY API KEY'
TEST_USER_NAME = 'MY USER NAME'


class HypoApiTest(unittest.TestCase):
    def setUp(self):
        self.hypo = HypoApi(
            base_url=TEST_HYPOTHESIS_API_URL,
            api_key=TEST_API_KEY,
            user_name=TEST_USER_NAME,
        )
