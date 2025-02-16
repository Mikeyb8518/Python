# Deisgn a proram that asks the user to enter a series of 20 numbers. 
# The program should store the numbers in a list then display the following data:
# 1. The lowest number in the list
# 2. The highest number in the list
# 3. The total of the numbers in the list
# 4. The average of the numbers in the list

# variable to store the list of numbers
numbers = []
# variable to hold the total of the numbers
total = 0

# loop to get 20 numbers from the user
for i in range(20):
    # get a number from the user and add it to the list
    number = int(input("Enter a number: "))
    # append the number to the list
    numbers.append(number)
    # add the number to the total
    total += number
    
# Display results
# Print the lowest number in the list
print("The lowest number in the list is: ", min(numbers))
# Print the highest number in the list
print("The highest number in the list is: ", max(numbers))
# Print the total of the numbers in the list
print("The total of the numbers in the list is: ", total)
# Print the average of the numbers in the list
print("The average of the numbers in the list is: ", total / 20)  