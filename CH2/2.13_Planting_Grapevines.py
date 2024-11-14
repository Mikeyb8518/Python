# Program using the formula that needs to know how many grapevines
# to plant in each row after measuring the length of a future row
# Prompt user to enter length of row in feet
row_length = float(input("Enter the length of the row in feet: "))

# Variable that asks user to enter smount of space used by an end
# post assembly in feet
end_post_space = float(input("Enter the space used by an end post assembly in feet: "))

# variable that ask user to enter the amount of space between the vines in feet
vine_space = float(input("Enter the space between the vines in feet: "))

# Formula to calculate the number of grapevines per row
V = (row_length - (2 * end_post_space)) / (vine_space)

# Display results
print("You can plant", V, "grapevines per row.")