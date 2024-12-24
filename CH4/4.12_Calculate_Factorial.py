# Write a program that ask the user to enter an intger number 
# Then calculate the factorial of the number and print it out.
# The program should handle the case when the user enters a non-integer value or a negative number

# Prompt the user to enter an integer number
num = int(input('Enter an integer number: '))

# variable to hold the factorial result
factorial = 1

# Check if the number is negative
if num < 0:
    print('Error: The number should be a non-negative integer.')
else:
    # For loop to calculate the factorial of the number entered by the user
    for i in range(2, num + 1):
        factorial *= i
        
    # Display results
    print(f'The factorial of {num} is {factorial}')  # Use an f-string