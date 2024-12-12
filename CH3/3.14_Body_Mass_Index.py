# Write a program that calculates the and displays a person's body mass index(BMI)

# Prompt user to enter the weight and height
weight = float(input('Please enter user weight: '))
height = float(input('Please enter user height: '))

# Calculate BMI
BMI = (weight * 703) / (height ** 2)

# Check all conditions 
if BMI < 18.5:
    print("Your BMI is : " + format(BMI,".2f") + \
          " So You Considered to be Underweight")
if BMI >= 18.5 and BMI <= 25:
    print("Your BMI is : " + format(BMI,".2f") + \
          " You have Optimal Weight")
else:
    print("Your BMI is : " + format(BMI,".2f") + \
          " So You Considered to be Overweight")