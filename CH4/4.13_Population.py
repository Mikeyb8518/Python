# Write a program that predicts the approximate size of the population of organisms
# The application should use boxes to allow the user to enter a starting number of organisms
# and the average daily population increase(as a percentage), and the number of days the organisms
# will be left to multiply

# Prompt user to enter the starting amount of organisms
starting_organisms = int(input("Enter the starting number of organisms: "))

# Prompt user to enter the average daily population increase as a percentage
increase_percentage = int(input("Enter the average daily population increase (as a percentage): "))

# Prompt user to enter the number of days the organisms will be left to multiply
days = int(input("Enter the number of days the organisms will be left to multiply: "))

# Display results
print("Day Approximate\t", "Population")
for i in range(1, days + 1):
    print(i, "\t\t", starting_organisms)
    starting_organisms += starting_organisms * increase_percentage / 100