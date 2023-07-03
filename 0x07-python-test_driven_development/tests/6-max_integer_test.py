#!/usr/bin/python3
"""unittest for max_integer([...])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integer([..])"""


    def test_empty_list(self):
        """test an empty list"""
        self.assertEqual(max_integer([]), None)

    def test_max_at_beginning(self):
        """Checks if the max is at the beginning"""
        nums = [2, -1, -3]
        self.assertEqual(max_integer(nums), nums[0])

    def test_ordered_list(self):
        """checks if the list is sorted"""
        nums = [1, 2, 3, 4]
        self.assertEqual(max_integer(nums), 4)

    def test_unorderd_list(self):
        """checks if the list is not sorted"""
        nums = [4, 2, 5, 1]
        self.assertEqual(max_integer(nums), 5)

    def test_floats_num(self):
        """checks for float numbers"""
        nums = [2.4, 3.5, 4.5, -21.5]
        self.assertEqual(max_integer(nums), 4.5)

    def test_single_num(self):
        """checks for list with a single int"""
        nums = [9]
        self.assertEqual(max_integer(nums), 9)

    def test_ints_and_floats(self):
        """checks for list with floats and ints"""
        nums = [2.5, 4, -15.2, 21.5, 21]
        self.assertEqual(max_integer(nums), 21.5)

    def test_large_nums(self):
        """"checks for list with large numbers"""
        large_list = list(range(2, 10000, 3)) + list(range(3000, 100, -2))
        self.assertEqual(max_integer(large_list), max(large_list))

    def test_string(self):
        """checks for single string"""
        strr = "Ekemini"
        self.assertEqual(max_integer(strr), 'n')

    def test_list_of_strings(self):
        """Test a list of strings."""
        strs = ["Ekemini", "is", "nice"]
        self.assertEqual(max_integer(strs), "nice")

    def test_empty_string(self):
        """Test an empty string."""
        self.assertEqual(max_integer(""), None)

if __name__ == "__main__":
    unittest.main()


