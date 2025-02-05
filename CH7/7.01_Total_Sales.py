# Design a program that asks the user to enter a store's sales for each day of the week. 
# The amounts should be stored in a list. Use a loop to calculate the total sales for the week
# and display the results

# Create a function to calulate the total sales for the week
def total_Sales():
    # Create a list to store the sales for each day of the week
    sales = []
    # Set total to 0
    total = 0
    # set week variable to 7 for the number of days in a week
    week = 7
    
    # for loop to get the sales for each day of the week
    for day in range(week):
        # Ask the user to enter the sales for each day of the week
        sale = input('Enter the store\'s sales for day ' + str(day+1) + ': $')
        # append sale to sales list
        sales.append(sale)
        # caluclate total sales
        total += float(sale)
    print(sales)
    print(total)
    
#call the function to calculate the total sales for the week
total_Sales()  # This will call the function and start the program.