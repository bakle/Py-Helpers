import unittest
from unittest import result
from unittest.case import TestCase
from bakle_helpers.email import Email

class TestNumber(unittest.TestCase):

    ##############  is_valid_tests   ##############

    def test_it_passes_is_valid_method_with_valid_email(self):
        result = Email.is_valid('test@test.com')
        self.assertTrue(result)

    def test_it_fails_is_valid_method_with_invalid_email(self):
        result = Email.is_valid('test')
        self.assertFalse(result)


    ##############  random_tests   ##############
    def test_it_gets_random_email(self):
        result = Email.random()
        self.assertTrue(Email.is_valid(result))
