import unittest
from unittest import result
from unittest.case import TestCase
from src.bakle_helpers.email import Email

class TestNumber(unittest.TestCase):

    ##############  is_a_number_tests   ##############

    def test_it_passes_is_valid_method_with_valid_email(self):
        result = Email.is_valid('test@test.com')
        self.assertTrue(result)

    def test_it_fails_is_valid_method_with_invalid_email(self):
        result = Email.is_valid('test')
        self.assertFalse(result)
