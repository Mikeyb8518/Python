# Program that will calculate the total amount of a meal purchased
# at a resturant. The program should ask the user to enter the charge 
# for the food, then calculate the amounts of a 18%  tip and a 7% sales tax.

# constants to hold  the tip and sales tax
TIP =  0.18
SALES_TAX = 0.07

#  get the charge for the food from the user
meal_purchased = float(input('Food charge: $'), end='\n\n')

# calculate the tip and sales tax
total_tip =  meal_purchased * TIP
total_sales_tax =  meal_purchased * SALES_TAX

# calculate the total amount of the meal purchased
meal_total =  (meal_purchased + total_tip + total_sales_tax)

# Display the results
print('Meal total: $', format(meal_purchased,  ',.2f'),  sep='')
print('Tip: $', format(total_tip,  ',.2f'), sep='')
print('Sales Tax: $', format(total_sales_tax, ',.2f'), sep='')
print('Final Total: $',  format(meal_total, ',.2f'), end='\n\n')