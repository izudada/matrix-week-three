# Import all required modules

from unittest import TestCase
from src.email_parser import EmailParser


class TestEmailClass(TestCase):

    email_parser = EmailParser()

    def test_convert_to_dict(self):
        email = 'tony+anthony@gmail.com'
        email_list = email.split('@')
        data = self.email_parser.convert_to_dict(email_list[0], email_list[1])
        self.assertEqual(type(data), type({}))

    def test_starts_with_str(self):
        data = self.email_parser.parse('tony+anthony@gmail.com')
        self.assertEqual(type(data['username'][0]), type(''))

    def test_true(self):
        data = self.email_parser.parse('tony+anthony@gmail.com')
        result = {'username': 'tony+anthony', 'domain': 'gmail.com'}
        self.assertEqual(data, result)

    def test_for_none(self):
        data = self.email_parser.parse(' tony+anthony@gmail.com')
        self.assertEqual(data, None)
    
    def test_for_none_two(self):
        data = self.email_parser.parse('tony+anthony@gmail.com ')
        self.assertEqual(data, None)
    
    def test_for_none_three(self):
        data = self.email_parser.parse(' tony+anthony@gmail.com ')
        self.assertEqual(data, None)
