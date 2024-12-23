# Write a program where the user will enter there starting weight
# on average a person will lose 4 pounds per month 
# the program will calculate the weight loss over a period of 6 months

# Prompt user to enter the starting weight of the user
starting_Weight = int(input("Enter your starting weight in pounds: "))

# Variable to hold weight loss
monthly_Loss = 4

# For loop to calculate weight loss over 6 months
for month in range(1, 7):
    # Calculate weight loss for each month
    starting_Weight -= monthly_Loss
    
    # Display results    
    print(month, '\t', starting_Weight)