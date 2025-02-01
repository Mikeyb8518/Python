# Write a program that will hold the names and scores of a golf tournment.
# The program will ask the player for their name and score, then add it to the list.
# The program will then print out the list of players and their scores.

# Funtion that will write the name and score of each players in the golf tournament to a file
def write_to_file():
    # Get the number of memebers in the golf tournament
    num_members = int(input("How many members are in the golf tournament? "))
    # Open and wrtie the number of memebers to the file called golf.txt
    object_file = open("golf.txt", "w")
    # Write the number of memebers to the file
    for i in range(num_members):
        # get the name of each member
        name = input('Enter the player\'s name: ')
        # get the score of each member
        score = input('Enter the player\'s score: ')
        # write the name and score of each member to the file
        object_file.write(name + '\n')
        object_file.write(score + '\n')
    # close the file
    object_file.close()
    return object_file

# function that will read the name and score of each players in the golf tournament from a file
def read_from_file():
    # Open the file called golf.txt
    object_file = open("golf.txt", "r")
    # read the file
    for i in object_file:
        # strip the newline character from the end of the line
        i = i.rstrip('\n')
        # print the name and score of each player
        print(i)
# call the fucntion to write the names and scores to the file
write_to_file()        
# call the function to read the names and scores from the file
read_from_file()