# Write a program that will calculate the how much insurance you will need on your home
# Prompt the user to enter the replacemnt cost of the building
cost = float(input("Enter the replacement cost of the building: $"))

# Create a function to display the results
def calculate(cost):
    # Formula that takes the user input an calculates the insurance at 80% of the cost
    insurance = cost * 0.8
    
    # Display the results
    print("The minimum amount of insurance you should buy for the property is $", format(insurance, ",.2f"))
    
# Call calulate function to display the results
calculate(cost)