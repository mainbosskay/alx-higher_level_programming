#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest 
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Unittest test max_integer defined class"""

    def test_non_empty_list(self):
        """maxinteger for non empty list integers"""
        regvalue = max_integer([1, 3, 5, 7, 9])
        self.assertEqual(regvalue, 9)

    def test_neg_values(self):
        """maxinteger for negative value integers"""
        negvalue = max_integer([-6, -5, -4, -3, -2, -1])
        self.assertEqual(negvalue, -1)

    def test_single_value(self):
         """maxinteger test for single value"""
         singleval = max_integer([5])
         self.assertEqual(singleval, 5)

    def test_float_values(self):
        """maxinteger for float values"""
        floatval = max_integer([2.4, 5.6, 1.2, 8.9])
        self.assertEqual(floatval, 8.9)

    def test_ints_floats(self):
        """maxinteger for integers and floats values"""
        intflt = max_integer([2, 3.4, -5, 4.8, 8, 8.4])
        self.assertEqual(intflt, 8.4)

    def test_empty_list(self):
        """maxinteger test for empty list"""
        emptylist = max_integer([])
        self.assertEqual(emptylist, None)

    def test_beginning_maxval(self):
        """maxinteger test for max value at the beginning"""
        beginmaxval = max_integer([8,6, 4, 2])
        self.assertEqual(beginmaxval, 8)

    def test_middle_maxval(self):
        """maxinteger test for max value at the middle"""
        middlemaxval = max_integer([2, 3, 9, 5, 1])
        self.assertEqual(middlemaxval, 9)


if __name__ == '__main__':
    unittest.main()
