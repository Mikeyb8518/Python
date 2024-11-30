# Write a program that prompts the user to enter a number within the range of 1-10
# The program should display the roman numeral equivalent of the entered number
# If a number is outside the range of 1-10, the program should display an error message

# Prompt user to enter a number 1-10
num = input("Enter a number between 1 and 10: ")

# convert input to integer
num = int(num)

# check if number is within range of 1-10
if 1 <= num <= 10:
    # display roman numeral equivalent of the number
    if num == 1:
        print("I")
    elif num == 2:
        print("II")
    elif num == 3:
        print("III")
    elif num == 4:
        print("IV")
    elif num == 5:
        print("V")
    elif num == 6:
        print("VI")
    elif num == 7:
        print("VII")
    elif num == 8:
        print("VIII")
    elif num == 9:
        print("IX")
    elif num == 10:
        print("X")
else:
    print("Error: Number is outside the range of 1-10")