# Write a program that determines whether a number is even or odd. It should generate 100 random numbers between 1 and 100
# and keeps count of how many of those random numbers are even and how many are odd.

# import random
import random

# function to check if a number is even or odd
def odd_even():
    # variables to hold count, odd, even
    count = 0
    odd = 0
    even = 0
    
    while count < 100:
        # generate a random number between 1 and 100
        num = random.randint(1, 101)
        # add the count
        count += 1
        print(num)
        
        # if statment to check if the number is even or odd
        if num % 2 != 0:
            even += 1
        else:
            odd += 1
    print('The time of odd is', odd, 'and the time of even is', even)
    
# call the function
odd_even()