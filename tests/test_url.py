import unittest
from bakle_helpers.url import Url

class TestUrl(unittest.TestCase):

    ##############  is_valid_tests   ##############

    def test_it_passes_is_valid_method_with_valid_url(self):
        result = Url.is_valid('http://test.com')
        self.assertTrue(result)

    def test_it_fails_is_valid_method_with_invalid_url(self):
        result = Url.is_valid('test')
        self.assertFalse(result)


    ##############  random_tests   ##############
    def test_it_gets_random_url(self):
        result = Url.random()
        self.assertTrue(Url.is_valid(result))