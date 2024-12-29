# Write a program that calculates and displays the county and state sales tax on a purchase.
# Constants to hold state and sales tax
COUNTY_TAX = .025
STATE_TAX = .05

# main function to start
def main():
    user_input()
    
# Function user input to get the user to enter price and calculate taxes
def user_input():
    # Get the purchase price from the user
    purchase_price = float(input("Enter the purchase price:$ "))
    
    # Calculate the county and state sales tax
    state_SalesTax = purchase_price * STATE_TAX
    county_SalesTax = purchase_price * COUNTY_TAX
    
    # Display the results
    print("State sales tax is $ {0:1,.2f}".format(state_SalesTax))
    print("County sales tax $ {0:1,.2f}".format(county_SalesTax))
    
    taxAddition = county_SalesTax + state_SalesTax
    
    # Call function to add final tax
    addition_Of_Tax(taxAddition)
    
    tax_after_purchase = purchase_price + taxAddition
    
    #call from this location to the method purchase_after_tax
    #to print the tax_after_purchase
    purchase_after_tax( tax_after_purchase)

# Function to display the addition of tax    
def addition_Of_Tax(taxAddition):
    print("Tax addition ${0:1,.2f}".format(taxAddition))

# Function to display the purchase after tax
def purchase_after_tax(tax_after_purchase):
    print("Purchase after tax ${0:1,.2f}".format(tax_after_purchase))

# Call main function to start     
main()