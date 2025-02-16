# Design a program that lets the user enter the total rainfall for each 12 months into a list.
# The program should then calculate and display the total rainfall for the year, and the average

# create a function that will display the total rainfall for the year
def total_rainfall():
    # variable to hold total
    total = 0
    # list to hold months
    months = []
    
    # For loop to prompt the user for rainfall for each month
    for i in range(12):
        # variable to hold user input
        rainfall = float(input(f"Enter the rainfall for month {i+1}: "))
        months.append(rainfall)
        # add rainfall to total
        total += rainfall
    print(months)
    # display total rainfall
    print("The total rainfall for the year is: ", total)
    # display average rainfall
    print("The average rainfall for the year is: ", format(total / 12, '.2f'))
    # display the month with the largest rainfall
    print("The month with the largest rainfall is: ", max(months))
    # display the month with the smallest rainfall
    print("The month with the smallest rainfall is: ", min(months))
# call function
total_rainfall()  # call the function to start the program. 