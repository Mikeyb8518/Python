# Write a program that uses a loop that asks the user to enter a series of positive numbers
# The user should enter a negative number to stop the loop and end the series

# ask the user to enter a series of positive numbers
number = float(input('Enter a positive number or enter a negative number to stop: '))

# total variable to hold the sum of the numbers
total = 0
# loop to ask the user to enter a series of positive numbers
while number > 0:
    total += number
    number = float(input('Enter a positive number: '))

# display results
print('The sum of the numbers is: ', total)