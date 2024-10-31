# Program that asks the user to enter the total square feet in a tact of land 
# and calculates the total number of acres

# Variable to hold square feet of an acre
one_acre =  43560

# ask user to enter the total square feet of the land
land_sqfeet =  float(input("Enter the total square feet of the land: "))

# calculate the total number of acres
total_acres = land_sqfeet / one_acre

# Display results
print('Number of acres in the land is: ', format(total_acres, '.2f'),  'acres')
