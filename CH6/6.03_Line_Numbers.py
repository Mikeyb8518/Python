# write a program that asks the user for the name of the a file. The program should display
# the contents of the file with each line preceded with a line number followed by a colon.
# The line numbering should start at 1.

def read():
    # Ask the user for the name of the file
    filename = input("Enter the name of the file: ")
    # Open the file in read mode
    object_file = open(filename, 'r')
    # Read the contents of the file
    line = object_file.readline()
    # Initialize a counter to keep track of the line number
    line = line.rstrip('\n')
    line_num = 1
    # while there are still lines in the file
    while line != "":
        # print the line number and the line
        print(line_num, ":", line, sep='')
        # read the next line
        line = object_file.readline()
        # remove the newline character and increment the line number
        line = line.rstrip('\n')
        line_num += 1
    # close the file
    object_file.close()
# call the function
read()        