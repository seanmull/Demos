from unittest.mock import patch
from unittest import TestCase


class adder():
    def add(self, x, y):
        return x + y

    def if_add_do_something(self, x, y, z):
        added = self.add(x, y)
        sum = int(z + added)
        print(int(added))
        print(sum)
        print(type(sum))
        if sum > 10:
            return "something"
        return "something else"


class TestAdder(TestCase):
    def setUp(self):
        self.adder = adder()

    @patch('Mock.adder.add', return_value=11)
    def test_over_10_sum(self, add):
        self.assertEqual(self.adder.if_add_do_something(2, 3, 1), "something")

    @patch('Mock.adder.add', return_value=1)
    def test_less_10_sum(self, add):
        self.assertEqual(self.adder.if_add_do_something(12, 13, 1), "something else")
