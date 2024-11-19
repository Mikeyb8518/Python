# Write a program that asks the user for a number
# in the range of 1-7. The program should display the day of the week

# Prompt user to enter a number 1-7
number = int(input("Enter a number between 1 and 7: "))
# Check if the number is in the range 1-7
if number == 1:
    print("The day of the week is Monday")
elif number == 2:
    print("The day of the week is Tuesday")
elif number == 3:
    print("The day of the week is Wednesday")
elif number == 4:
    print("The day of the week is Thursday")
elif number == 5:
    print("The day of the week is Friday")
elif number == 6:
    print("The day of the week is Saturday")
elif number == 7:
    print("The day of the week is Sunday")
# If the number is not in the range 1-7, print an error message
else:
    print("Invalid number. Please enter a number between 1 and 7.")
