# Write a program that asks a user to enter the amount that he or she has budgeted
# for a month. A loop should then prompt the user to enter each of his or her expenses
# for the month and keep a running total. When the loop finishes, the program should display
# the amount that the user is under or over budget

# budget variable to hold user input
budget = float(input("Enter your monthly budget: $"))

# vairables to hold total and variable to continue loop
total = 0.00
another = "y"

# loop to get user expenses and add to total
# Display results and messages
while another == "y" or another == "Y":
    expense = float(input("Please input the amount of your expense: $"))
    total += expense
    another = input('Do you want to enter another amount? Enter y or Y for yes:')
    
    if total > budget:
        print("You are over budget by $", total - budget)
    else:
        print("You are under budget by $", budget - total)