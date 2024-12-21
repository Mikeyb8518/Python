# The ocean rises at 1.6 millimeters per year. Create an application that displays the number 
# of millimeters that the ocean will have risen each year for the next 25 years

# Print the header year and millimeter
print('Year\t', 'millimeters')

# For loop to display  results
for i in range(1, 26):
    print(format(i, '2.0f'), '\t', format(i * 1.6, '5.2f'), 'millimeter')