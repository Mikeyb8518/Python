# Write a program that will calculate the total sales for the month
# the amount of state and county sales tax collected. The state rate is 5% and the county is 2.5%
# Ask the user to enter the total sales for the month and display
# amount of county sales tax, state sales tax, and total sales tax collected.

# Prompt the user to enter the total sales for the month
total_sales = float(input("Enter the total sales for the month: $"))

# function to calcualte the taxes and display the results
def calculate_taxes(total_sales):
    # Calculate the state sales tax
    state_tax = total_sales * 0.05
    # Calculate the county sales tax
    county_tax = total_sales * 0.025
    # Calculate the total sales tax collected
    total_tax = state_tax + county_tax
    # Display the results
    print(f"State Sales Tax: ${state_tax:.2f}")
    print(f"County Sales Tax: ${county_tax:.2f}")
    print(f"Total Sales Tax: ${total_tax:.2f}")
    
calculate_taxes(total_sales) # Call the function with the total sales as an argument