import unittest
from find_max_in_array import largest


class Testfile(unittest.TestCase):
    def test_empty_array(self):
        arr = []
        self.assertEqual(
            largest(arr, len(arr)), -1, "Should return none for empty array"
        )

    def test_single_element_array(self):
        arr = [42]
        self.assertEqual(
            largest(arr, len(arr)),
            42,
            "Largest element should be the only element in the array",
        )

    def test_all_elements_equal(self):
        arr = [2, 2, 2, 2, 2]
        self.assertEqual(
            largest(arr, len(arr)),
            2,
            "Largest element should be 2 as all elements are equal",
        )

    def test_negative_elements(self):
        arr = [-10, -20, -30, -5]
        self.assertEqual(largest(arr, len(arr)), -5, "Largest element should be -5")

    def test_both_positive_and_negative(self):
        arr = [-10, 4, -3, 98, -99]
        self.assertEqual(largest(arr, len(arr)), 98, "Largest element should be 98")

    def test_largest_numbers(self):
        arr = [1000000000, 999999999, 1234567890, 9876543210]
        self.assertEqual(
            largest(arr, len(arr)), 9876543210, "Largest element should be 9876543210"
        )

    def test_with_duplicates(self):
        """
        Test case to check the scenario where there are duplicate elements
        in the array and the largest element is the duplicate one.
        """
        arr = [9, 8, 9, 7, 3]
        self.assertEqual(largest(arr, len(arr)), 9, "Largest element should be 9")
        self.assertEqual(largest(arr, len(arr)), 9, "Largest element should be 9")


if __name__ == "__main__":
    unittest.main()

