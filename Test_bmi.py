import Lab2.bmi as BMI

'''def test_bmi_under_weight():
    expected_result = -1
    result = BMI.calculate_bmi(1.73,40)
    assert (result == expected_result)

def test_bmi_over_weight():
    expected_result = 1
    result = BMI.calculate_bmi(1.73,90)
    assert (result == expected_result)

def test_bmi_normal_weight():
    expected_result = 0
    result = BMI.calculate_bmi(1.73,70)
    assert (result == expected_result)'''



def test_bmi_underweight():
    expected_result = -1
    result = BMI.calculate_bmi(1.73, 40)
    assert (result == expected_result)
    # assert BMI.calculate_bmi(1.73, 40) == -1

def test_bmi_normal():
    expected_result = 0
    result = BMI.calculate_bmi(1.73, 57)
    assert (result == expected_result)
    # assert BMI.calculate_bmi(1.73, 57)  == 0

def test_bmi_overweight():
    expected_result = 0
    result = BMI.calculate_bmi(1.73, 77)
    assert (result == expected_result)
    # assert BMI.calculate_bmi(1.73, 77) == 1