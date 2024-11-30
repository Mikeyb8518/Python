# Design a program that prompts the user to enter the names of two primary colors to mix
# If the user enters anthing other than red, blue, or yellow, the program should display an error message and ask for the color
# The program should then mix the two colors and display the resulting color

# Prompt the user to enter the names of two primary colors to mix
color1 = input("Enter the name of the first primary color (red, blue, or yellow): ")
color2 = input("Enter the name of the second primary color (red, blue, or yellow: ")

# Check if the user entered valid primary color
if color1 == "red" and color2 == "blue" or color1 == "blue" and color2 == "red":
    print("Purple")
elif color1 == "red" and color2 == "yellow" or color1 == "yellow" and color2 == "red":
    print("Orange")
elif color1 == "blue" and color2 == "yellow" or color1 == "yellow" and color2 == "blue":
    print("Green")
else:
    print("Invalid color. Please enter red, blue, or yellow.")