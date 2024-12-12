# Febuary has 28 days normally, But if it is a leap year, it has 29 days.
# We need to check if the year is a leap year or not.
# Write a program that asks the user to enter a year. The program should then display the number of days
# in February for that year.

# Prompt user to enter a year 
year = int(input("Enter a year: "))

# If statement to determine if year is leap
# Display results
if year % 400 == 0:
    print('Febuary', year, 'has 29 days and year is leap')
elif (year % 100) != 0 and (year % 4) == 0:
    print('Febuary', year, 'has 29 days and year is leap')
else:
    print('Febuary', year, 'has 28 days')