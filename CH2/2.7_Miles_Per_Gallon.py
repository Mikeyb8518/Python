# Program that can calculate the MPG of a car

# miles_driven variable to prompt user to enter the total miles driven
miles_driven = float(input('Enter the  total miles driven: '))

# gallons_used variable to prompt user to enter the total gallons used
gallons_used = float(input('Enter number of  gallons used: '))


# mpg variable to calculate the MPG of the car
mpg =  miles_driven / gallons_used

#Display results
print('The total MPG is: ', format(mpg,  '.2f'), 'MPG')
