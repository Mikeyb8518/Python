# Write a program that asks the user to enter a weight of a package then displays the shipping charges

# Prompt the user to enter the weight of the package
weight = float(input("Enter the weight of the package in pounds: "))

# if statement to determine the shipping charge based on the weight of the package
if weight < 2:
    shipping_charge = 1.50
elif weight > 2 and weight <= 6:
    shipping_charge = 3.00
elif weight > 6 and weight <= 10:
    shipping_charge = 4.00
else:
    shipping_charge = 4.75
    
# Display the shipping charge to the user
print('The shipping charge for the package is $', format(shipping_charge, ',.2f'))