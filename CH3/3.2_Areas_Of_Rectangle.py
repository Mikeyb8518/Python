# The area of a rectangle is the rectangle's length times width
# Write a program that asks for the length and width of two rectangle's
# The program should tell the user which rectangle has the greater area or same area

#  Prompt user for the length and width of the first rectangle
length1 = float(input("Enter the length of the first rectangle: "))
width1 = float(input("Enter the width of the first rectangle: "))

# Prompt user for the length and width of the second rectangle
length2 = float(input("\nEnter the length of the second rectangle: "))
width2 = float(input("Enter the width of the second rectangle: "))

# Calculate the area of the first rectangle
area1 = length1 * width1

# Calculate the area of the second rectangle
area2 = length2 * width2

# Determine which rectangle has the greater area or same area
if area1 > area2:
    print("\nThe first rectangle has a greater area.")
elif area1 < area2:
    print("\nThe second rectangle has a greater area.")
else:
    print("\nBoth rectangles have the same area.")