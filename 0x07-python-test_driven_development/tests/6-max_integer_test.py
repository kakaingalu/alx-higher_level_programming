#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_max_value(self):
        self.assertEqual(max_integer([5, 3, 2]), 5)
        self.assertEqual(max_integer([4, 6, 7]), 7)
        self.assertEqual(max_integer([4, 8, 5]), 8)
        self.assertEqual(max_integer([4, 6, -2]), 6)
        self.assertEqual(max_integer([-4, -5, -8]), -4)
        self.assertEqual(max_integer([-4]), -4)
        self.assertEqual(max_integer([5]), 5)

    def test_empty(self):
        self.assertIsNone(max_integer([]))


if __name__ == "__main__":
    unittest.main()

    def test_floats(self):
        """Test a list of floats."""
        floats = [1.53, 6.33, -9.123, 15.2, 6.0]
        self.assertEqual(max_integer(floats), 15.2)

    def test_ints_and_floats(self):
        """Test a list of ints and floats."""
        ints_and_floats = [1.53, 15.5, -9, 15, 6]
        self.assertEqual(max_integer(ints_and_floats), 15.5)

    def test_string(self):
        """Test a string."""
        string = "Ehoneah"
        self.assertEqual(max_integer(string), 'r')

    def test_list_of_strings(self):
        """Test a list of strings."""
        strings = ["Ehoneah", "is", "my", "name"]
        self.assertEqual(max_integer(strings), "name")

    def test_empty_string(self):
        """Test an empty string."""
        self.assertEqual(max_integer(""), None)

if __name__ == '__main__':
    unittest.main()
