"""Tests for lambdata modules."""

import unittest
from random import randint
# unittest supports a type of tests called unit tests
# A unit is the smallest cohesive piece of code we can test
# (usually something like a function or method)

# Other types of tests (you won't write now, just to be aware):
# - Integration: testing multiple pieces working together
# - End to end: testing a full "flow"/use case
# There are also manual/non-code test that are common
# - Use aceptance testing: show it to a user, get feedback
# - Manual running and checking


# from example_module import increment, COLORS
# from oop_examples import SocialMediaUser
from dataframe_helper import MathFunctions


# class ExampleUnitTests(unittest.TestCase):
#     """Making sure our examples behave as expected."""
#     def test_increment(self):
#         """Testing that increment adds one to a number."""
#         x1 = 5
#         y1 = increment(x1)
#         x2 = -106
#         y2 = increment(x2)
#         # Now we make sure the output is as expected with assertions
#         self.assertEqual(y1, 6)
#         self.assertEqual(y2, -105)
        
#     def test_increment_random(self):
#         x1 = randint(1, 1000000)
#         y1 = increment(x1)
#         self.assertEqual(y1, x1 + 1)

#     def test_colors(self):
#         """Testing presence/absence of expected colors."""
#         self.assertIn('Orange', COLORS)
#         self.assertNotIn('Aquamarine', COLORS)
#         self.assertEqual(len(COLORS), 6)


# class SocialMediaUserTests(unittest.TestCase):
#     """Test the instantiation and use of SocialMediaUser."""
#     def test_name(self):
#         """Test that the name field is assigned correctly."""
#         user1 = SocialMediaUser('Jane')
#         user2 = SocialMediaUser('Joe')
#         self.assertEqual(user1, 'Jane')
#         self.assertEqual(user2, 'Joe')
    
#     def test_default_upvotes(self):
#         """Test that the default upvotes of a new user is 0."""
#         user1 = SocialMediaUser('Jane')
#         self.assertEqual(user1.upvotes, 0)
        
#     def test_unpopular(self):
#         """Test that a user with <=100 upvotes is not popular."""
#         user1 = SocialMediaUser('Joe')
#         for _ in range(randint(1, 100)):
#             user1.receive_upvote()


class DFHelperUnitTest(unittest.TestCase):
    """Making sure the Math class performs as expected"""
    def test_num1(self):
        """Tests the num1 field is assigned correctly"""
        x = MathFunctions(2)
        y = MathFunctions(-3)
        self.assertEqual(x.n1, 2)
        self.assertEqual(y.n1, -3)
    
    def test_add(self):
        x = MathFunctions(2)
        y = x.addition(5)
        self.assertEqual(y, 7)
            
    def test_subtract(self):
        x = MathFunctions(2)
        y = x.subtract(5)
        self.assertEqual(y, -3)
    
    def test_multiply(self):
        x = MathFunctions(2)
        y = x.multiply(5)
        self.assertEqual(y, 10)
    
    def test_divide(self):
        x = MathFunctions(2)
        y = x.divide(5)
        self.assertEqual(y, .4)




if __name__ == '__main__':
    # This conditional is for code that will be run
    # when we execute our file from the command line
    unittest.main()