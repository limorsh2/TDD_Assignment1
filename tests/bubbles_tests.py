import unittest
from src import BubblesSort

class BubblesSortTest(unittest.TestCase):
    def test_bubble_sort(self):
        # stub
        stub1 = [7, 2, 0, 9, 6]
        stub2 = [0, 1, 2, 3]
        stub3 = []
        stub4 = [-2, -9, -1]
        stub5 = [9, -9, 6, -7]

        # assume
        expected1 = [0, 2, 6, 7, 9]
        expected2 = [0, 1, 2, 3]
        expected3 = []
        expected4 = [-9, -2, -1]
        expected5 = [-9, -7, 6, 9]

        # action
        result1 = BubblesSort.bubble_sort(stub1)
        result2 = BubblesSort.bubble_sort(stub2)
        result3 = BubblesSort.bubble_sort(stub3)
        result4 = BubblesSort.bubble_sort(stub4)
        result5 = BubblesSort.bubble_sort(stub5)

        # expect/assert
        self.assertIsNotNone(result1)
        self.assertEqual(result1, expected1)

        self.assertIsNotNone(result2)
        self.assertEqual(result2, expected2)

        self.assertIsNotNone(result3)
        self.assertEqual(result3, expected3)

        self.assertIsNotNone(result4)
        self.assertEqual(result4, expected4)

        self.assertIsNotNone(result5)
        self.assertEqual(result5, expected5)


if __name__ == '__main__':
    unittest.main()