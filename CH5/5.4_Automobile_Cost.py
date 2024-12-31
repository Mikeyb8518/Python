# Write a program that prompts the user to enter the month cost for the following expenses
# incurred from operating his or her automobile: loan payment, insurance, gas, oil, tires
# and maintenance. The program then calculates and displays the total monthly cost of
# operating the automobile.

# Prompt the user to enter the monthly cost for owning a vehicle
loan_payment = float(input("Enter the monthly loan payment: $"))
insurance = float(input("Enter the monthly insurance payment: $"))
gas = float(input("Enter the monthly gas payment: $"))
tires = float(input("Enter the monthly tire payment: $"))
maintance = float(input("Enter the monthly maintenance payment: $"))

# Function to calculate the sum total of the monthly expenses
def calculate_total_expenses(loan_payment, insurance, gas, tires, maintance):
    total_expenses = loan_payment + insurance + gas + tires + maintance
    
    # Print the total monthly expenses
    print(f"The total monthly expenses for owning a vehicle is: ${total_expenses:.2f}")
    
# Call function to display
calculate_total_expenses(loan_payment, insurance, gas, tires, maintance)  # Call