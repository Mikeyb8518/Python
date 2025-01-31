# Write a program that reads the random numbers from the file, displays the numbers,
# then displays the following data: 
# Total of numbers
# The number of random numbers read from the file

# read random numbers function
def read_random_numbers():
    # open the file in read mode
    object_file = open("random_numbers.txt", "r")
    # Set total to 0
    total = 0
    # Set count to 0
    count = 0
    # for each line in the file
    for i in object_file:
        # strip the line of leading/trailing spaces
        i = i.rstrip('\n')
        # convert the line to an integer
        i = int(i)
        # print i
        print(i)
        # add i to total
        total += i
        # increment count by 1
        count += 1
    # print total    
    print('\nTotal is:',total)
    # print count
    print('Number of random numbers read from the file:',count)
    # close the file
    object_file.close
# call the function
read_random_numbers()