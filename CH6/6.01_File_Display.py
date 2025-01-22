# Assume a file containing a series of integers is named 'numbers.txt' and exsist on the computer disk.
# Write a program that displays all the numbers in the file.

def display_numbers():
    # open the numbers.txt file to read
    file_object = open('_numbers.txt', 'r')
    
    # line object is used to read the file line by line
    line = file_object.readline()
    # strip the line from its newline character
    line = line.rstrip('\n')
    
    # while loop is used to read all the lines in the file
    while line != '':
        # print the line
        print(line)
        # read the next line
        line = file_object.readline().rstrip('\n')
        # strip the line from its newline character
        line = line.rstrip('\n')
    # close the file
    file_object.close
# call the function to display the numbers
display_numbers()
    