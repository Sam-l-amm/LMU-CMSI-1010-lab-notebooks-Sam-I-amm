"""
PS4 Grading Unit Tests
Run this file to check your work! You should not modify this file.
"""

import unittest

from midpoint import midpoint
from not_equal import not_equal
from mousepoint import mouse_in_rectangle


class MidpointTests(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(midpoint([]), None)

    def test_odd_size(self):
        self.assertEqual(midpoint([1]), 1)
        self.assertEqual(midpoint([1, 2, 3]), 2)
        self.assertEqual(midpoint([1, 2, 3, 4, 5]), 3)

    def test_even_size(self):
        self.assertEqual(midpoint([1, 2]), 1.5)
        self.assertEqual(midpoint([1, 2, 3, 4]), 2.5)
        self.assertEqual(midpoint([1, 2, 3, 4, 5, 6]), 3.5)


class NotEqualTests(unittest.TestCase):

    def test_empty(self):
        self.assertEqual(not_equal([], 1), True)

    def test_equal_elements(self):
        self.assertEqual(not_equal(1, 1), False)
        self.assertEqual(not_equal("a", "a"), False)
        self.assertEqual(not_equal([1], [1]), False)

    def test_not_equal_elements(self):
        self.assertEqual(not_equal(1, 2), True)
        self.assertEqual(not_equal("a", "b"), True)
        self.assertEqual(not_equal([1], [2]), True)


class MousepointTests(unittest.TestCase):

    def test_inside(self):
        self.assertEqual(mouse_in_rectangle(150, 150), True)
        self.assertEqual(mouse_in_rectangle(101, 199), True)
        self.assertEqual(mouse_in_rectangle(199, 101), True)
        self.assertEqual(mouse_in_rectangle(101, 101), True)
        self.assertEqual(mouse_in_rectangle(199, 199), True)

    def test_outside(self):
        self.assertEqual(mouse_in_rectangle(50, 50), False)
        self.assertEqual(mouse_in_rectangle(50, 150), False)
        self.assertEqual(mouse_in_rectangle(150, 50), False)
        self.assertEqual(mouse_in_rectangle(250, 250), False)
        self.assertEqual(mouse_in_rectangle(250, 150), False)
        self.assertEqual(mouse_in_rectangle(150, 250), False)


def run_tests(test_case_class):
    """
    Helper function to run unit tests for a given test case class.
    """
    test_suite = unittest.TestLoader().loadTestsFromTestCase(test_case_class)
    unittest.TextTestRunner(verbosity=2).run(test_suite)


if __name__ == '__main__':
    unittest.main()
