# Write a program that asks the user to enter valus for mass and velocity, then calls a function
# called kinetic_energy function to get the objects kinetic energy

# Prompt user to enter mass and velocity
mass = float(input("Enter the mass of the object in kg: "))
velocity = float(input("Enter the velocity of the object in m/s: "))

# function for kinetic energy
def kinetic_energy(mass, velocity):
    # formula to calculate kinetic energy
    KE = (1 / 2) * mass * (velocity ** 2)
    
    # print the amount of kinetic energy
    print('The amount of kinetic energy that the object has', KE)
    
    #return the amount of kinetic energy
    return KE

# call the function with the mass and velocity entered by the user
kinetic_energy(mass, velocity)