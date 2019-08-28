import unittest
from hypothepy.utils.http_client import HttpClient
from unittest.mock import patch
import json

class DefaultHeadersTest(unittest.TestCase):
    def setUp(self):
        self.header_name = 'TestHeader'
        self.header_value = 'Test Token'
        self.http = HttpClient(default_headers={
            self.header_name: self.header_value,
        })

    ####################################################################################################################
    # GET Method
    #
    @patch('requests.get')
    def test_get_method_uses_default_headers(self, mock_get):
        self.http.get("www.someurl.com")
        mock_get.assert_called_with("www.someurl.com", headers={self.header_name: self.header_value})

    @patch('requests.get')
    def test_get_method_allows_overwritting_default_headers(self, mock_get):
        self.http.get("www.someurl.com", headers={self.header_name: 'New Value'})
        mock_get.assert_called_with("www.someurl.com", headers={self.header_name: 'New Value'})

    @patch('requests.get')
    def test_get_method_merges_extra_headers(self, mock_get):
        self.http.get("www.someurl.com", headers={'Content-Type': 'application/json'})
        mock_get.assert_called_with("www.someurl.com", headers={self.header_name: self.header_value, 'Content-Type': 'application/json'})

    ####################################################################################################################
    # POST Method
    #
    @patch('requests.post')
    def test_post_method_uses_default_headers(self, mock_post):
        self.http.post("www.someurl.com")
        mock_post.assert_called_with("www.someurl.com", headers={self.header_name: self.header_value})

    @patch('requests.post')
    def test_post_method_allows_overwritting_default_headers(self, mock_post):
        self.http.post("www.someurl.com", headers={self.header_name: 'New Value'})
        mock_post.assert_called_with("www.someurl.com", headers={self.header_name: 'New Value'})

    @patch('requests.post')
    def test_post_method_merges_extra_headers(self, mock_post):
        self.http.post("www.someurl.com", headers={'Content-Type': 'application/json'})
        mock_post.assert_called_with("www.someurl.com", headers={self.header_name: self.header_value, 'Content-Type': 'application/json'})

    ####################################################################################################################
    # DELETE Method
    #
    @patch('requests.delete')
    def test_delete_method_uses_default_headers(self, mock_delete):
        self.http.delete("www.someurl.com")
        mock_delete.assert_called_with("www.someurl.com", headers={self.header_name: self.header_value})

    @patch('requests.delete')
    def test_delete_method_allows_overwritting_default_headers(self, mock_delete):
        self.http.delete("www.someurl.com", headers={self.header_name: 'New Value'})
        mock_delete.assert_called_with("www.someurl.com", headers={self.header_name: 'New Value'})

    @patch('requests.delete')
    def test_delete_method_merges_extra_headers(self, mock_delete):
        self.http.delete("www.someurl.com", headers={'Content-Type': 'application/json'})
        mock_delete.assert_called_with("www.someurl.com", headers={self.header_name: self.header_value, 'Content-Type': 'application/json'})

    ####################################################################################################################
    # PUT Method
    #
    @patch('requests.put')
    def test_put_method_uses_default_headers(self, mock_put):
        self.http.put("www.someurl.com")
        mock_put.assert_called_with("www.someurl.com", headers={self.header_name: self.header_value})

    @patch('requests.put')
    def test_put_method_allows_overwritting_default_headers(self, mock_put):
        self.http.put("www.someurl.com", headers={self.header_name: 'New Value'})
        mock_put.assert_called_with("www.someurl.com", headers={self.header_name: 'New Value'})

    @patch('requests.put')
    def test_put_method_merges_extra_headers(self, mock_put):
        self.http.put("www.someurl.com", headers={'Content-Type': 'application/json'})
        mock_put.assert_called_with("www.someurl.com", headers={self.header_name: self.header_value, 'Content-Type': 'application/json'})

    ####################################################################################################################
    # PATCH Method
    #
    @patch('requests.patch')
    def test_patch_method_uses_default_headers(self, mock_patch):
        self.http.patch("www.someurl.com")
        mock_patch.assert_called_with("www.someurl.com", headers={self.header_name: self.header_value})

    @patch('requests.patch')
    def test_patch_method_allows_overwritting_default_headers(self, mock_patch):
        self.http.patch("www.someurl.com", headers={self.header_name: 'New Value'})
        mock_patch.assert_called_with("www.someurl.com", headers={self.header_name: 'New Value'})

    @patch('requests.patch')
    def test_patch_method_merges_extra_headers(self, mock_patch):
        self.http.patch("www.someurl.com", headers={'Content-Type': 'application/json'})
        mock_patch.assert_called_with("www.someurl.com", headers={self.header_name: self.header_value, 'Content-Type': 'application/json'})
