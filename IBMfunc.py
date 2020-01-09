import unittest


def BMI(height,weight):
    tmp_bmi=weight/(height*height)
    if(tmp_bmi<18.5):
        return 'Underweight'
    elif(tmp_bmi>18.5 and tmp_bmi<25):
        return 'Proper weight'
    else: #tmp_bmi>25
        return 'Overweight'

class BMITest(unittest.TestCase):
    def test_BMI(self):
        #stub
        h1=1.70
        w1=60
        h2=1.90
        w2=65
        h3=1.50
        w3=80

        #assum
        expected1='Proper weight'
        expected2='Underweight'
        expected3='Overweight'

        #action
        result1 =BMI(h1,w1)
        result2 =BMI(h2,w2)
        result3 =BMI(h3,w3)

        # expect/assert
        self.assertEqual(result1,expected1)
        self.assertEqual(result2, expected2)
        self.assertEqual(result3, expected3)

if __name__ == '__main__':
    unittest.main()







