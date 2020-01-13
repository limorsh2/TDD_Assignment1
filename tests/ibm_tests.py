import unittest
from src import IBMfunc

class BMITest(unittest.TestCase):
    def test_BMI(self):
        #stub
        h1 = 1.70
        w1 = 60
        h2=1.90
        w2=65
        h3=1.70
        w3=80
        h4=1.70
        w4=90
        h5 =1.50
        w5 =85
        h6 =1.30
        w6 =100
        h7 = 0
        w7 = 50
        h8 = 1.9
        w8 = -1

        #assum
        expected1='Proper weight'
        expected2='Underweight'
        expected3='Overweight'
        expected4='Obese Class 1'
        expected5='Obese Class 2'
        expected6='Obese Class 3'
        expected7 = 'invalid'
        expected8 = 'invalid'

        #action
        result1 = IBMfunc.BMI(h1,w1)
        result2 = IBMfunc.BMI(h2,w2)
        result3 = IBMfunc.BMI(h3,w3)
        result4 = IBMfunc.BMI(h4,w4)
        result5 = IBMfunc.BMI(h5,w5)
        result6 = IBMfunc.BMI(h6,w6)
        result7 = IBMfunc.BMI(h7,w7)
        result8 = IBMfunc.BMI(h8, w8)

        # expect/assert
        self.assertEqual(result1, expected1)
        self.assertEqual(result2, expected2)
        self.assertEqual(result3, expected3)
        self.assertEqual(result4, expected4)
        self.assertEqual(result5, expected5)
        self.assertEqual(result6, expected6)
        self.assertEqual(result7, expected7)
        self.assertEqual(result8, expected8)

if __name__ == '__main__':
    unittest.main()