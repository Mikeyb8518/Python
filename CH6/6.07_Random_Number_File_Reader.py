# Write a program that writes a series of random numbers to a file. Each random number should
# be in the range of 1 through 500. The application should let the user specify how many 
# random numbers to generate and write to the file.

# Import the random module to generate random numbers
import random

# function to generate random numbers and write to file
def generate_random_numbers():
    # open the file in write mode
    object_file = open("random_numbers.txt", "w")
    # get the number of random numbers from the user
    num_numbers = int(input("How many random numbers would you like to generate? "))
    # loop to generate and write the random numbers to the file
    for i in range(num_numbers):
        # generate a random number between 1 and 500
        random_number = random.randrange(1, 501)
        # write the random number to the file
        random_number = str(random_number)
        # write the random number to the file followed by a newline character
        object_file.write(random_number)
        # add a newline character after each number
        object_file.write('\n')
    # close the file
    object_file.close()
# print a message to let the user know the file has been written
generate_random_numbers()            