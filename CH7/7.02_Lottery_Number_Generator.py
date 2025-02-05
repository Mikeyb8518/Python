# Design a program that generates a seven-digit lottery number. The program should generate
# seven random numbers, each in the range 0-9, and assign each number to a list element

# Import the random module
import random

# function that generates a seven-digit lottery number
def generate_lottery_number():
    # lottery list
    lottery_list = []
    # for loop to generate seven random numbers
    for i in range(7):
        # generate a random number between 0 and 9
        lottery_list.append(random.randrange(0, 10))
    # print the lottery list
    print(lottery_list)
    
    return lottery_list

# function to display the lottery list
def display(lottery_list):
    # for loop to print each number in the list
    for i in lottery_list:
        # print the number
        print(i)
        
# call the function to generate the lottery number    
lottery_list = generate_lottery_number()
display(lottery_list)  # This will print the generated lottery number