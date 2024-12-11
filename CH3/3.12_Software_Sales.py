# A software company sells a package that retials for $99
# Write a program that asks the user to enter the number of packages purchased
# Program should then display the amount of the discount(if any) and the total amount of 
# the purchase after discount

package_price = 99

# prompt user to enter the number of packages purchased
num_packages = float(input("Enter the number of packages purchased: "))

# if statement to check for discount amount if any
if num_packages < 10:
    discount_amount = 0
elif num_packages < 20:
    discount_amount = .1
elif num_packages < 50:
    discount_amount = .2
elif num_packages < 100:
    discount_amount = .3
else:
    discount_amount = .4
    
# variables to hold total and discount total
sub_total = num_packages * package_price
discount_total = sub_total * discount_amount
# calculate total after discount
final_total = sub_total - discount_total

# Display the Result
print("the amount of the discount is : $" + \
      format(discount_total, ",.2f"))
print("total amount of the purchase after the discount is : $" + \
       format(final_total, ",.2f"))