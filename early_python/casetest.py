import unittest
import camelcase

class CaseTest(unittest.TestCase):
    def test_transform_snake_to_camel(self):

        found = camelcase.transform_snake_to_camel('arbitrary_word')
        expected = 'ArbitraryWord'
        assert found == expected

    def test_transform_camel_to_snake(self):

        found = camelcase.transform_camel_to_snake('ArbitraryWord')
        expected = 'arbitrary_word'
        assert found == expected
