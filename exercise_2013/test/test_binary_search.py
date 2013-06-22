__author__ = 'Nancy'

import unittest
from binary_search import binary_search  , binary_search2


class TestBinarySearch(unittest.TestCase):
    def test_method1(self):
        arr = range(0, 10)

        self.assertEqual(binary_search(arr, 1), 1)


        for i in arr:
            self.assertEqual(binary_search(arr, i), i)

        self.assertEqual(binary_search(arr, -1), -1)
        self.assertEqual(binary_search(arr, 100), -1)


    def test_method2(self):
        arr = range(0, 10)

        self.assertEqual(binary_search2(arr, 1), 1)


        for i in arr:
            self.assertEqual(binary_search2(arr, i), i)

        self.assertEqual(binary_search2(arr, -1), -1)
        self.assertEqual(binary_search2(arr, 100), -1)
