# Program that will have ask the user to enter a purchase amount
# Program should calculate the state and county sales tax
# Sales tax is 5% and the county tax is 2.5%

# Constants to hold sales tax and county sales tax
STATE_TAX = 0.05
COUNTY_TAX = 0.025

# purchase_amount variable to prompt user to enter purchase amount
purchase_amount =  float(input("Enter the purchase amount: $"))

# vriable to hold total state tax
total_state_tax = purchase_amount  * STATE_TAX

# variable to hold total  county tax
total_county_tax = purchase_amount  * COUNTY_TAX

# variable to hold total of sales taxes
total_sales_tax =  total_state_tax + total_county_tax

# variable of the final total
final_total =  purchase_amount + total_sales_tax

# Display results
print('Purchase Amount: $', format(purchase_amount,  ',.2f'), sep='')

print('Total State Tax: $',  format(total_state_tax, ',.2f'), sep='')

print('Total County Tax: $', format(total_county_tax, ',.2f'), sep='')

print('Total Sales Tax: $',  format(total_sales_tax, ',.2f'), sep='')

print('Final Total: $', format(final_total, ',.2f'), sep='', end='\n\n')