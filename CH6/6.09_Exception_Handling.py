# Modify the program that you wrote for exercise 6 so it handles the following exceptions:
# *It should handle any IOError exceptions that are raised when the file is opened and data
#  is read from it.
# *It should handle any ValueError exceptions that are raised when the items that are read from the file
#  are converted to a number

# function that read data from file and return a list of numbers and then will find the average of the numbers
# also have 2 excemptions : IOError and ValueError
def read_data():
    # set count to 0
    count = 0
    # set total to 0
    total = 0
    
    # try and else block to handle exceptions
    try:
        # open the file in read mode
        object_file = open('_numbers.txt', 'r')
    except IOError:
        # if IOError is raised print the error message
        print("Error: Unable to open the file")
    except ValueError:
        # if ValueError is raised print the error message
        print("Error: Unable to read the file")
    else:
        # loop through each line in the file
        for i in object_file:
            # total the count and add the number to the total
            total += int(i)
            # increment the count by 1
            count += 1
        # print total average
        print("Average: ", total/count)
        # close the file
        object_file.close()
# call the function
read_data()