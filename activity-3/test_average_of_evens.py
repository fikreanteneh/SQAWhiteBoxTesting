import unittest
from average_of_evens import average_of_evens


class TestAverageOfEvens(unittest.TestCase):
    def test_average_of_evens(self):
        # Test Case 1 - Empty List
        self.assertEqual(average_of_evens([]), 0)

        # Test Case 2 - No Even Numbers
        self.assertEqual(average_of_evens([1, 3, 5]), 0)

        # Test Case 3 - Only Even Numbers
        self.assertEqual(average_of_evens([2, 4, 6]), 4.0)

        # Test Case 4 - Mix of Even and Odd
        self.assertEqual(average_of_evens([1, 2, 3, 4]), 3.0)

        # Test Case 5 - Single Even Number
        self.assertEqual(average_of_evens([8]), 8.0)
