# Running burns 4.2 calories per minute. Write a program that uses a loop to display 
# the number of calories burned after 10, 15, 20, 25, and 30 minutes of running.

# variable to hold calories burned
calories_burned = 4.2

# Variable to hold total
total = 0

# For loop to display the number of minutes and calories burned per minute
for minutes in range(10, 31, 5):
    total = calories_burned * minutes
    print(f"After {minutes} minutes of running, you burn {total} calories.")