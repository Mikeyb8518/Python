# A roulette wheel has pockets. The pockets are numbered from 0 - 36. The colors are as followed
# Pocket 0 is green. Pocket 1-10, the odd numbered pockets are red, the even numbered pockets are black.
# Pocket 11-18, the odd numbered pockets are black, the even numbered pockets are red
# Pocket 19-28, the odd numbered pockets are red, the even numbered pockets are black
# Pocket 29-36, the odd numbered pockets are black, the even numbered pockets are red

# Write a program that asks the user to enter a pocket number and display whether the pocket is
# red, black or green. If number is out of range an error message should display.

# prompt user to enter a pocket number
pocket_number = int(input("Enter a pocket number in range of(0-36): "))

if pocket_number == 0:
    print("The pocket is green")
elif pocket_number >= 1 and pocket_number <= 10:
    if pocket_number % 2 != 0:
        print("The pocket is red")
    else:
        print("The pocket is black")
elif pocket_number >= 11 and pocket_number <= 18:
    if pocket_number % 2 != 0:
        print("The pocket is black")
    else:   
        print("The pocket is red")
elif pocket_number >= 19 and pocket_number <= 28:
    if pocket_number % 2 != 0:
        print("The pocket is red")
    else:
        print("The pocket is black")
elif pocket_number >= 29 and pocket_number <= 36:
    if pocket_number % 2 != 0:
        print("The pocket is black")
    else:   
        print("The pocket is red")
else:
    print("Error: Pocket number is out of range")