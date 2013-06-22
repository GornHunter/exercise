_author_ = 'Nancy'


print("before import")


import cls_test

import unittest
from Fibonacci import fibonacci1

print("after import")
print("self", __name__)

class Testfibo(unittest.TestCase):
    def test(self):
        fib = [1, 1, 2, 3, 5, 8]

        self.assertEqual(fibonacci1(4), fib[3])



if __name__ == "__main__":


    print (__name__)