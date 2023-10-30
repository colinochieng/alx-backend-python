#!/usr/bin/env python3
'''
Module that  Parameterize a unit test
'''
import unittest
from parameterized import parameterized, param
from typing import (
    Mapping,
    Sequence,
    Any
)
from utils import access_nested_map, get_json


class TestAccessNestedMap(unittest.TestCase):
    '''
    desc: Testcase child class for testing functionality
        of utils.access_nested_map function
    '''
    @parameterized.expand([
        param(nested_map={"a": 1}, path=("a",), expected_result=1),
        param(nested_map={"a": {"b": 2}}, path=("a",),
              expected_result={'b': 2}),
        param(nested_map={"a": {"b": 2}}, path=("a", "b"), expected_result=2)
    ])
    def test_access_nested_map(
                            self, nested_map: Mapping, path: Sequence,
                            expected_result: Any) -> None:
        '''
        desc: Method to test the functionlity of
            utils.access_nested_map function
            test that the method returns what it is supposed to
        '''
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

    @parameterized.expand([
        param(nested_map={}, path=("a",), err=KeyError),
        param(nested_map={"a": 1}, path=("a", "b"), err=KeyError)
    ])
    def test_access_nested_map_exception(
                                    self, nested_map: Mapping,
                                    path: Sequence,
                                    err: KeyError) -> None:
        '''
        desc: test exception raising from utils.access_nested_map function
        Use the assertRaises context manager
        '''
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    '''
    desc: Testcase child class for testing functionality
        of utils.get_json function
    '''
    @parameterized.expand([
        param("http://example.com", {"payload": True}),
        param("http://holberton.io", {"payload": False})
    ])
    @unittest.mock.patch('utils.requests.get', autospec=True)
    def test_get_json(
            self, test_url: str,
            test_payload: Any,
            mock_obj: unittest.mock.MagicMock) -> None:
        '''
        desc: method to test the functionality of
            utils.get_json function
            - test if the return value is what is expected
            - No making of any actual external HTTP calls
            - Use unittest.mock.patch to patch requests.get to
                Use unittest.mock.patch to patch requests.get
        '''
        mock_obj.return_value = unittest.mock.MagicMock(
            json=unittest.mock.MagicMock(return_value=test_payload)
        )
        result = get_json(test_url)
        mock_obj.assert_called_once_with(test_url)
        self.assertEqual(result, test_payload)
