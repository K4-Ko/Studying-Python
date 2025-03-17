# Program to calculate Body Mass Index (BMI) and determine weight status
# BMI Categories:
# – Below 18.5: Underweight
# – Between 18.5 and 25: Ideal Weight
# – 25 to 30: Overweight
# – 30 to 40: Obesity
# – Above 40: Morbid Obesity

# Importing the pow function from math module to calculate power
from math import pow

# Getting user input for weight (in kg) and height
p = float(input('What is your weight in kg?: '))
a = float(input('What is your height?: '))

# Calculating BMI using the formula: weight / (height^2)
bmi = p / (pow(a, 2))
# Alternative way to calculate power using Python's ** operator
# bmi = p / (a**2)

# Series of conditional statements to determine BMI category
# Checking if BMI is above 40 (Morbid Obesity)
if bmi > 40:
    print('Your BMI is {:.1f}, you are considered Morbidly Obese.'.format(bmi))
# Checking if BMI is between 30 and 40 (Obesity)
elif bmi < 40 and bmi > 30:
    print('Your BMI is {:.1f}, you are considered Obese.'.format(bmi))
# Checking if BMI is between 25 and 30 (Overweight)
elif bmi < 30 and bmi > 25:
    print('Your BMI is {:.1f}, you are Overweight.'.format(bmi))
# Checking if BMI is between 18.5 and 25 (Ideal Weight)
elif bmi < 25 and bmi > 18.5:
    print('Your BMI is {:.1f}, you are at an Ideal Weight.'.format(bmi))
# If none of the above conditions are met, BMI is below 18.5 (Underweight)
else:
    print('Your BMI is {:.1f}, you are Underweight.'.format(bmi))
