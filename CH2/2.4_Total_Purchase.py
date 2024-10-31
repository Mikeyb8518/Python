# Customer in store is purchasing 5 items
# Write a program that displays subtotal of the sale, amount of sales tax .07%  and total amount

# constant sales_tax set to 0.07
SALES_TAX = .07

# create 5 item variables to  hold the price of each item
item1 = float(input('\nEnter the price  of item 1: $'))
item2 =  float(input('Enter the price  of item 2: $'))
item3 =   float(input('Enter the price  of item 3: $'))
item4 =   float(input('Enter the price  of item 4: $'))
item5 =   float(input('Enter the price  of item 5: $'))

# subtotal variable  to hold the total price of all items
subtotal = (item1  + item2 + item3 + item4 + item5)

# calculate  sales tax by multiplying subtotal by sales_tax
sales_tax_amount = subtotal * SALES_TAX

# calculate total
total = subtotal + sales_tax_amount

# display results
print('\nTotal = $', format(total, ',.2f'), sep='', end='\n\n')