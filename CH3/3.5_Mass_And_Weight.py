# Write a program that asks the user to enter an objects mass,
# then calculates its weight. If the object weighs more than 500 newtons
# it prints a message saying that the object is too heavy.
# If the object is less than 100 newtons it prints a message saying that the object is too light.

# Prompt user to enter the weight of the object
mass = float(input("Enter the mass of the object in kg: "))

# Calculate the weight of the object
weight = mass * 9.81

# Display results
print(f"The weight of the object is {weight} newtons")

# Check if the object is too heavy or too light
if weight > 500:
    print("The object is too heavy")
elif weight < 100:
    print("The object is too light")