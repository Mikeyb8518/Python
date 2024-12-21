# College tuition is $8,000. Tuition increases 3% each year for the next 5 years
# Write a program with a loop that displays the projected semester tuition amount 
# for the next 5 years

# Variable to hold tuition cost
tuition_cost = 8000

# For loop to project the tuition cost for the next 5 years with a 3% increase each year
for year in range(1, 6):
    tuition_cost *= 1.03
    
    if year == 1:
        print('In {} year, the tuition will be ${:.2f}.'.format(year, tuition_cost))
    else:
        print('In {} years, the tuition will be ${:.2f}.'.format(year, tuition_cost))