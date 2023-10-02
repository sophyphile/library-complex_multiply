import unittest
import math
from complex_multiply import Multiplication

class MultiplicationTestCase(unittest.TestCase):
    def setUp(self):
        self.multiplier = Multiplication(2)
    
    def test_zero(self):
        """Test 0 multiplied by 2"""

        # 0 multiplied by 2 return 0
        result = self.multiplier.multiply(0)
        self.assertEqual(result, 0)

    def test_natural_number(self):
        """Test natural number 5 multiplied by 2"""

        # 5 multiplied by 2 return 10
        result = self.multiplier.multiply(5)
        self.assertEqual(result, 10)

    def test_integer_number(self):
        """Test integer number -7 multiplied by 2"""
        
        # -7 multiplied by 2 return -14
        result = self.multiplier.multiply(-7)
        self.assertEqual(result, -14)
    
    def test_rational_number(self):
        """Test rational number 6/17 multiplied by 2"""

        # 6/17 multiplied by 2 return (6/17) * 2
        result = self.multiplier.multiply(6/17)
        self.assertEqual(result, (6/17) * 2)

    def test_real_number(self):
        """Test real number pi multiplied by 2"""

        # pi multiplied by 2 return 2pi
        result = self.multiplier.multiply(math.pi)
        self.assertEqual(result, math.pi * 2)

if __name__ == '_main_':
    unittest.main()