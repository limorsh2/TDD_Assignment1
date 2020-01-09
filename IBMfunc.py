import unittest


def BMI(height,weight):
    tmp_bmi=weight/(height*height)
    if(tmp_bmi<18.5):
        return 'Underweight'
    elif(tmp_bmi>18.5 and tmp_bmi<25):
        return 'Proper weight'
    elif (tmp_bmi>25 and 29.9>tmp_bmi):
        return 'Overweight'
    elif (tmp_bmi>30 and 34.9>tmp_bmi):
        return 'Obese Class 1'
    elif (tmp_bmi>35 and 39.9>tmp_bmi):
        return 'Obese Class 2'
    else: #tmp_bmi>40
        return 'Obese Class 3'


class BMITest(unittest.TestCase):
    def test_BMI(self):
        #stub
        h1=1.70
        w1=60
        h2=1.90
        w2=65
        h3=1.50
        w3=80
        h4=1.70
        w4=90
        h5 =1.50
        w5 =85
        h6 =1.30
        w6 =100

        #assum
        expected1='Proper weight'
        expected2='Underweight'
        expected3='Overweight'
        expected4='Obese Class 1'
        expected5='Obese Class 2'
        expected6='Obese Class 3'

        #action
        result1 =BMI(h1,w1)
        result2 =BMI(h2,w2)
        result3 =BMI(h3,w3)
        result4 = BMI(h4,w4)
        result5 = BMI(h5,w5)
        result6 = BMI(h6,w6)


        # expect/assert
        self.assertEqual(result1,expected1)
        self.assertEqual(result2, expected2)
        self.assertEqual(result3, expected3)
        self.assertEqual (result4, expected4)
        self.assertEqual (result5, expected5)
        self.assertEqual (result6, expected6)

if __name__ == '__main__':
    unittest.main()







