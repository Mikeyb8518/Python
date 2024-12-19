# Write a program that uses nested loops to collect data and calculate the average 
# rainfall over a period of years

# Ask user to enter the amount of years of data they want to enter
years = int(input("Enter the number of years of data: "))

# variable to hold monthly rainfall
month_rainfall = 0
# neted loop to get the verage rainfall from the user 
for i in range(1, years + 1):
    for m in range(1, 13):
        rainfall_inch = float(input('Enter the inches of rainfall for this month: '))
        month_rainfall += rainfall_inch
# Variable to convert years to the total number of months
months = years * 12

# Display results
print('The number of months', months, '\nThe total inches of rainfall is',
      month_rainfall, '\nThe average rainfall is', format(month_rainfall / months, '.2f'))