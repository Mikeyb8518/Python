# Design a program that asks the user to enter a month(in numeric form), a day,
# and a two year digit. THe program should determine whether the month times day equals the year.
# If it does, the program should print out a message saying "the date is magic"
# otherwise, it should print out a message saying "the date is not magic"

# prompt user to enter a month, day, and two year digit
month = int(input("Enter a month (1-12): "))
day = int(input("Enter a day (1-31): "))
year = int(input("Enter a two year digit: "))

# check if the month times day equals the year
if month * day == year:
    print("The date is magic")
else:
    print("The date is not magic")