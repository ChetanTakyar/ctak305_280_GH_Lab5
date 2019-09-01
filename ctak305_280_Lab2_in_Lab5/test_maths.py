import unittest     # Import the Python unit testing framework
import maths        # Our code to test
from maths import convert_base


class MathsTest(unittest.TestCase):
    ''' Unit tests for our maths functions. '''

    def test_add(self):
        result = maths.add(5,5)
        self.assertEqual(result, 10, "The add function returns an incorrect value")
        ''' Tests the add function. '''
        pass # TODO

    def test_fibonacci(self):
        ''' Tests the fibonacci function. '''
       
        self.assertEqual(maths.fibonacci(5), 5)
        
        pass # TODO

    def test_convert_base_under_ten(self):
        ""
        self.assertEqual(convert_base(8, 9), 10)
    
    def test_convert_base_over_ten(self):
        ""
        self.assertEqual(convert_base(12, 13), 'C')


# This allows running the unit tests from the command line (python test_maths.py)
if __name__ == '__main__':
    unittest.main()
