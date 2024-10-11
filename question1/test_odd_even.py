import unittest
from odd_even import check_even_odd

class TestEvenOdd(unittest.TestCase):

    def test_even_number(self):
        # Testing standard even numbers
        self.assertEqual(check_even_odd(24), "24 Is Even Number")
        self.assertEqual(check_even_odd(0), "0 Is Even Number")
        self.assertEqual(check_even_odd(-2), "-2 Is Even Number")
        self.assertEqual(check_even_odd(2**31), "2147483648 Is Even Number")  # Large even number

    def test_odd_number(self):
        # Testing standard odd numbers
        self.assertEqual(check_even_odd(19), "19 Is Odd Number")
        self.assertEqual(check_even_odd(-3), "-3 Is Odd Number")
        self.assertEqual(check_even_odd(1), "1 Is Odd Number")
        self.assertEqual(check_even_odd(2**31 - 1), "2147483647 Is Odd Number")  # Large odd number

    def test_edge_cases(self):
        # Minimum and maximum values
        self.assertEqual(check_even_odd(-1), "-1 Is Odd Number")  # Negative odd number
        self.assertEqual(check_even_odd(2**31), "2147483648 Is Even Number")  # Large even number
        self.assertEqual(check_even_odd(-2**31), "-2147483648 Is Even Number")  # Large negative even number

    def test_empty_inputs(self):
        # No empty inputs are applicable for this function since it expects an integer,
        # but if we wanted to handle this case we would need to modify the function.
        with self.assertRaises(TypeError):
            check_even_odd("")  # Testing with an empty string
        with self.assertRaises(TypeError):
            check_even_odd([])  # Testing with an empty list
        with self.assertRaises(TypeError):
            check_even_odd(None)  # Testing with None

    def test_negative_values(self):
        self.assertEqual(check_even_odd(-4), "-4 Is Even Number")  # Negative even number
        self.assertEqual(check_even_odd(-5), "-5 Is Odd Number")    # Negative odd number

    def test_special_cases(self):
        # Since this function does not handle dates, we'll skip this test.
        pass  # You could implement date handling if needed.

    def test_type_variations(self):
        # Testing invalid types to ensure the function raises a TypeError
        with self.assertRaises(TypeError):
            check_even_odd("text")  # Testing with a string
        with self.assertRaises(TypeError):
            check_even_odd(3.14)  # Testing with a float
        with self.assertRaises(TypeError):
            check_even_odd([])  # Testing with an empty list
        with self.assertRaises(TypeError):
            check_even_odd({})  # Testing with an empty dictionary

if __name__ == '__main__':
    unittest.main()
    