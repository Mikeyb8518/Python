# Write a program that displays the number of names that are stored in the file

def count():
    # open the file in read mode
    object_file = open('_names.txt', 'r')
    # read the file
    line = object_file.readline()
    # strip the newline character
    line = line.rstrip('\n')
    # set count to 0
    count = 0
    # loop through the file
    while line != '':
        # increment count by 1
        count += 1
        # read the next line
        line = object_file.readline()
        # strip the newline character
        line = line.rstrip('\n')
        # close the file
    object_file.close()
    # return the count
    return count
# Call the function and print the result
print(count())
