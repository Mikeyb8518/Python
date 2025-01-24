# write a program that reads the _numbers.txt an then calculates the average of all numbers
# in the file

def calculate_average():
    # open the file in read mode
    object_file = open('_numbers.txt', 'r')
    # set total to 0
    total = 0
    # set count to 0
    count = 0
    # read the file line by line
    for i in object_file:
        # get the total of each i and add it to total
        total += int(i)
        # increment count by 1
        count += 1
    # print the average of total divided by count    
    print(total /count)
    # close the file
    object_file.close()
# call the function
calculate_average()    