# In the program, write a function that accepts two arguments; a list, and a number n
# Assume that the list contains only numbers. The function should display all of the numbers
# in the list that are greater than n.

# number_list variable is a list of numbers
number_list = [1, 2, 3, 4, 5]
# n is a number
n = 3
# Function to display numbers greater than n
def compare(number_list, n):
    # Loop through the list and check each number
    for i in number_list:
        # If the number is greater than n, print it
        if i > n:
            print(i)
# call the function to display the results            
compare(number_list, n)