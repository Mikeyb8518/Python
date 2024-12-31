# Write a program that asks for the actual value of a piece of property and displays the assessment value
# and property tax. Which is 60 percent of the actual value. The property tax is .72 cents for each 
# $100 of the assessment value.

# Prompt the user to enter the actual value of the property
actual_value = float(input("Enter the actual value of the property: $"))

# Create a function to calculate the assessment value
def calculate_assessment_value(actual_value):
    tax = actual_value * 0.6 * 0.72 / 100
    print('The property tax is $', format(tax, ',.2f'), sep='')
    
# Call function to display results
calculate_assessment_value(actual_value)  # This line is not needed as the function already prints