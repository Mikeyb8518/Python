# Write a program that user pay a penny for the day then doubles it every day 

# Prompt user to enter the number of days
days = int(input("Enter the number of days: "))

# Display table
print('Day\t\t', 'Salary')
print('-' * 25)

# Variable to hold total
total = 0

# For loop to get the ramge of days and total salary
for i in range(1, days + 1):
    salary = 0.01 * 2 ** (i - 1)
    print(format(i, '3.0f'), '\t\t', format(salary, '8.2f'))
    total += salary

# Display results    
print('The total pay at the end of the period is $', total)