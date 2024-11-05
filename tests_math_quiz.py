import unittest
from math_quiz import function_A, function_B, function_C  # replace with updated function names if needed

class TestMathGame(unittest.TestCase):

    def test_function_A(self):
        """Test if random numbers generated are within the specified range."""
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = function_A(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_function_B(self):
        """Test if function_B returns a valid operator from the choices '+', '-', or '*'."""
        valid_operators = ['+', '-', '*']
        for _ in range(1000):  # Test multiple times for consistency
            operator = function_B()
            self.assertIn(operator, valid_operators)

    def test_function_C(self):
        """Test if function_C returns the correct problem and answer for various operators."""
        test_cases = [
            # (num1, num2, operator, expected_problem, expected_answer)
            (5, 2, '+', '5 + 2', 7),
            (5, 2, '-', '5 - 2', 3),
            (5, 2, '*', '5 * 2', 10),
            (10, 3, '+', '10 + 3', 13),
            (10, 3, '-', '10 - 3', 7),
            (10, 3, '*', '10 * 3', 30),
            (0, 5, '+', '0 + 5', 5),
            (0, 5, '-', '0 - 5', -5),
            (0, 5, '*', '0 * 5', 0),
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            problem, answer = function_C(num1, num2, operator)
            self.assertEqual(problem, expected_problem, f"Failed for inputs: {num1}, {num2}, {operator}")
            self.assertEqual(answer, expected_answer, f"Failed for inputs: {num1}, {num2}, {operator}")

if __name__ == "__main__":
    unittest.main()
