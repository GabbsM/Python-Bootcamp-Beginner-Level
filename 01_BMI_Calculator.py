import math

height = int (input('Input your height: '))
weight = int (input('Input your weight: '))

height_pow = math.pow(height,2)
bmi = weight / height_pow

print(f'Your BMI is {bmi}')

