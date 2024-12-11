# Write a program that asks the user to enter the number of books that he or she has purchased this month
# then display the number of points awarded

# Prompt the user to enter the number of books purchased for the month
books_purchased = int(input("Enter the number of books purchased this month: "))

# if statement to award points based on the number of books purchased
if books_purchased == 0:
    print("You have not purchased any books this month. You have earned 0 points.")
elif books_purchased <= 2:
    print("You have earned 5 points for the month.")
elif books_purchased <= 4:
    print("You have earned 15 points for the month.")
elif books_purchased <= 6:
    print("You have earned 30 points for the month.")
else:
    print("You have earned 60 points for the month.")  # This is the last condition