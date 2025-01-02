# Write a program that uses a function that will convert feet to inches
# Prompt the user to enter the number of feet to convert

# variable that will ask the user to enter the number of feet to convert
feet = float(input("Enter the number of feet to convert: "))
# Convert feet to inches using the function
def convert(feet):
    inches = feet * 12
    # display the result
    print(feet, "feet is equal to", inches, "inches")
    
convert(feet) # call the function with the user's input