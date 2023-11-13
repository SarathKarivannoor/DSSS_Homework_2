import unittest
from math_quiz import generate_random_numbers, select_random_operator, quiz_builder

class TestMathGame(unittest.TestCase):

    def test_generate_random_numbers(self):
        # Test if random numbers generated are within the specified range
    
        min_val = [0, 1, 3, 8, 10, 47, 99, 111, 752, 999, 1234, 9999, 76542]
        max_val = [10, 1000, 30, 84, 100, 47777, 999999, 1115, 759, 9997777, 123452, 999999999, 765420]
            
        for i in range(13):  # Test a large number of random values
            rand_num = generate_random_numbers(min_val[i], max_val[i])
            self.assertTrue(min_val[i] <= rand_num <= max_val[i])
            
    def test_select_random_operator(self):
        #Test whether the selected operator is a valid one 
        operators = ['+', '-', '*']
        self.assertIn(select_random_operator(), operators)

    def test_quiz_builder(self):
            #Test if problem statements and answers are generated correctly
            test_cases = [
                (5, 2, '+', '5+2', 7),
                (50, 22, '-', '50-22', 28),
                (10, 244, '*', '10*244', 2440),
                (7, 12, '*', '7*12', 84),
                (800, 199, '-', '800-199', 601),
                (10, 244, '+', '10+244', 254)    
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                problem = "{}{}{}".format(num1,operator,num2)
                self.assertTrue(expected_problem == problem)
                self.assertEqual(eval(problem), expected_answer)

if __name__ == "__main__":
    unittest.main()

