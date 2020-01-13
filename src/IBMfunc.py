
def BMI(height, weight):
    if(height <=0 or weight <= 0):
        return 'invalid'
    tmp_bmi= weight/(height*height)
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










