# Develop a logic that reads a person's weight and height, calculates their Body Mass Index (BMI), 
# and displays their status according to the table below:

# – BMI below 18.5: Underweight

# – Between 18.5 and 25: Ideal Weight

# – 25 to 30: Overweight

# – 30 to 40: Obesity

# – Above 40: Morbid Obesity

from math import pow

p = float(input('What is your weight in kg?: '))
a = float(input('What is your height?: '))

bmi = p / (pow(a, 2))
# bmi = p / (a**2)

if bmi > 40:
    print('Your BMI is {:.1f}, you are considered Morbidly Obese.'.format(bmi))
elif bmi < 40 and bmi > 30:
    print('Your BMI is {:.1f}, you are considered Obese.'.format(bmi))
elif bmi < 30 and bmi > 25:
    print('Your BMI is {:.1f}, you are Overweight.'.format(bmi))
elif bmi < 25 and bmi > 18.5:
    print('Your BMI is {:.1f}, you are at an Ideal Weight.'.format(bmi))
else:
    print('Your BMI is {:.1f}, you are Underweight.'.format(bmi))
