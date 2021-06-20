import unittest
from unittest.case import TestCase
from bakle_helpers.str import Str
from bakle_helpers.helper_exceptions import HelperExceptions


class TestString(unittest.TestCase):

    ##############  is_a_string_tests   ##############

    def test_is_a_string(self):
        result = Str.is_a_string('Test')
        self.assertTrue(result)
    
    def test_is_not_a_string(self):
        result = Str.is_a_string(12345)
        self.assertFalse(result)        
    

    ##############  ends_with_tests   ##############

    def test_it_ends_with_case_sensitive(self):
        result = Str.ends_with('Hello world', 'ld')
        self.assertTrue(result)

    def test_it_not_ends_with_case_sensitive(self):
        result = Str.ends_with('Hello world', 'test')
        self.assertFalse(result)

    def test_it_ends_with_case_insensitive(self):
        result = Str.ends_with('Hello world', 'LD', True)
        self.assertTrue(result)

    def test_it_not_ends_with_case_insensitive(self):
        result = Str.ends_with('Hello world', 'TEST', True)
        self.assertFalse(result)

    def test_ends_with_method_raises_an_exception_with_not_string_type(self):
        with self.assertRaises(TypeError):
            Str.ends_with(3567788, 88)

    
    ##############  starts_with_tests   ##############

    def test_it_starts_with_case_sensitive(self):
        result = Str.starts_with('Hello world', 'Hell')
        self.assertTrue(result)

    def test_it_not_starts_with_case_sensitive(self):
        result = Str.starts_with('Hello world', 'test')
        self.assertFalse(result)

    def test_it_starts_with_case_insensitive(self):
        result = Str.starts_with('Hello world', 'hell', True)
        self.assertTrue(result)

    def test_it_not_starts_with_case_insensitive(self):
        result = Str.starts_with('Hello world', 'TEST', True)
        self.assertFalse(result)

    def test_starts_with_method_raises_an_exception_with_not_string_type(self):
        with self.assertRaises(TypeError):
            Str.starts_with(3567788, 88)

    
    ##############  after_tests   ##############

    def test_it_retrieve_after_part(self):
        result = Str.after('The hello world', 'hello')
        self.assertEqual('world', result)

    def test_it_retrieve_empaty_after_part_if_limit_is_in_the_end(self):
        result = Str.after('The hello world', 'world')
        self.assertEqual('', result)

    def test_it_retrieve_all_string_if_limit_is_empty(self):
        result = Str.after('The hello world', '')
        self.assertEqual('The hello world', result)

    def test_after_method_raises_an_exception_with_not_string_type(self):
        with self.assertRaises(TypeError):
            Str.after(3567788, 88)

    
    ##############  before_tests   ##############

    def test_it_retrieve_before_part(self):
        result = Str.before('The hello world', 'world')
        self.assertEqual('The hello', result)

    def test_it_retrieve_empaty_before_part_if_limit_is_in_the_begining(self):
        result = Str.before('The hello world', 'The')
        self.assertEqual('', result)

    def test_it_retrieve_all_string_if_limit_is_empty(self):
        result = Str.before('The hello world', '')
        self.assertEqual('The hello world', result)

    def test_before_method_raises_an_exception_with_not_string_type(self):
        with self.assertRaises(TypeError):
            Str.before(3567788, 88)

    
    ##############  contains_tests   ##############

    def test_it_contains_string_case_sensitive(self):
        result = Str.contains('The hello world', 'world')
        self.assertTrue(result)

    def test_it_not_contains_string_case_sensitive(self):
        result = Str.contains('The hello world', 'World')
        self.assertFalse(result)

    def test_it_contains_string_case_insensitive(self):
        result = Str.contains('The hello world', 'World', True)
        self.assertTrue(result)

    def test_it_not_contains_string_case_insensitive(self):
        result = Str.contains('The hello world', 'TEST', True)
        self.assertFalse(result)

    def test_before_method_raises_an_exception_with_not_string_type(self):
        with self.assertRaises(TypeError):
            Str.contains(3567788, 88)

    
    ##############  limit_tests   ##############

    def test_it_limit_string_with_ellipses(self):
        result = Str.limit('The hello world', 6)
        self.assertEqual('The he...', result)

    def test_it_limit_string_without_ellipses(self):
        result = Str.limit('The hello world', 6, False)
        self.assertEqual('The he', result)

    def test_it_return_all_string_if_limit_is_greater_than_string_length(self):
        result = Str.limit('The hello world', 16)
        self.assertEqual('The hello world', result)

    def test_limit_method_raises_an_exception_with_not_string_type(self):
        with self.assertRaises(TypeError):
            Str.limit(3567788, 88)

    def test_limit_method_raises_an_exception_with_not_number_limit_type(self):
        with self.assertRaises(TypeError):
            Str.limit('The hello world', 'ad')

    
    ##############  random_tests   ##############

    def test_it_return_a_random_string(self):
        result = Str.random(5)
        self.assertEqual(5, len(result))

    def test_it_return_empty_string_if_lenght_is_zero(self):
        result = Str.random(0)
        self.assertEqual('', result)

    def test_it_return_empty_string_if_lenght_is_less_than_zero(self):
        result = Str.random(-3)
        self.assertEqual('', result)

    def test_random_method_raises_an_exception_with_not_number_length_type(self):
        with self.assertRaises(TypeError):
            Str.random('test')