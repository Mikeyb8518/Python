# Write a program that lets the user to enter 2 values and check to see which one is greater

# Prompt the user to enter two integer values
a = int(input("Enter the first value: "))
b = int(input("Enter the second value: "))

# function to check the max value of two numbers
def max_value(a, b):
    if a > b:
        print(a, 'is bigger than', b)
    else:
        print(b, 'is bigger than', a)
        
max_value(a,b) # call the function with the two values as arguments