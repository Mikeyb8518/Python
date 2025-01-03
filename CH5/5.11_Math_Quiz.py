# Write a program that gives simple math quizzes. The program should display 2 random numbers

# import the random module to generate random numbers
import random

# Variables to store the two random numbers
num1 = random.randint(1, 1000)
num2 = random.randint(1, 1000)

# variable to store the total
total = num1 + num2

# print the 2 numbers
print('\t', format(num1, '4.0f'))
print('+\t', format(num2, '4.0f'))

# answer variable to store the user's answer
answer = int(input('Enter the answer: '))

# Function to check for the correct answer
def check_answer(answer, total):
    if answer == total:
        print('Correct')
    else:
        print('Incorrect. The correct answer is', total)
        
check_answer(answer, total) # call the function with the user's answer and the total