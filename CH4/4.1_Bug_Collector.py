# A bug collects bugs every day for 5 days. Write a program that keeps a running total of the number
# of bugs collected during the 5 days. The loop should ask for the number of bugs collected each day and
# then print the total number of bugs collected at the end of the 5 days.

# variable to hold total
total = 0

# for loop to get the user to enter the total of bugs collected for each day
for day in range(1, 6):
    # ask for number of bugs collected each day
    bugs_collected = int(input("How many bugs were collected on day " + str(day)
                               + "? "))
    # add bugs collected to total
    total += bugs_collected

# print the total number of bugs collected at the end of the 5 days
print("The total number of bugs collected over 5 days is " + str(total) + ".")