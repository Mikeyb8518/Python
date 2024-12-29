# Write a program that uses a function to convert kilometers to miles

# prompt user to enter a value in kilometers
km = float(input("Enter a value in kilometers: "))
# define a function to convert kilometers to miles
def convert(km):
    miles = km * 0.621371
    print(format(miles, "0.2f") + " miles")

# call the function with the user's input
convert(km)