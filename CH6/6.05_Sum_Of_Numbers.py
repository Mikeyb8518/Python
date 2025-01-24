# Assume a file containing a series of integers is named numbers.txt and exsists on the computers disk
# Write a program that reads all of the numbers stored in the file and calculates their total

def calculate_total():
    # Open the file in read mode
    object_file = open('_numbers.txt', 'r')
    # set total to 0
    total = 0
    # Loop through each line in the file
    for i in object_file:
        # Strip the line of any leading or trailing whitespace
        i = int(i.rstrip('\n'))
        # Add the number to the total
        total += i
        # print the number to the console
        print(i)
    # print the total to the console
    print('The total is:', total)
    # Close the file
    object_file.close()
# Call the function to start the program
calculate_total()    