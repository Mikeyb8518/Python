# Write a program that displays
# The amount of money Joe paid for the stock
# The amount of commission Joe paid his broker when buying the stock
# The amount for which Joe sold the stock
# The amount of commission Joe paid his broker when selling the stock
# The amount of profit Joe made from the sale of the stock positive  or negative

purchased = 2000
buyValue = 40.00
commission = .03
sellValue = 42.75
sold = 2000

# Calculate the amount of money Joe paid for the stock
amountPaid = purchased * buyValue

#  Calculate the amount of commission Joe paid his broker when buying the stock
commissionPaidBuy = amountPaid * commission

# Calculate the  amount for which Joe sold the stock
amountSold = sold  * sellValue

# Caluclate the amount of comission Joe paid his broker when selling his  stock
commissionPaidSell = amountSold * commission

# The total profit made from Joe after paying his broker
amountLeft =  amountSold - commissionPaidSell -  amountPaid - commissionPaidBuy

# Display results
print('Joe paid $', format(amountPaid, ',.2f'))

print('Joe paid a commission of $', format(commissionPaidBuy, ',.2f'))

print('Joe sold his stocks for $', format(amountSold, ',.2f'))

print('Joe paid his broker after the sale $', format(commissionPaidSell, ',.2f'))

if amountLeft < 0:
    print('Joe made a loss of $', format(abs(amountLeft), ',.2f'))
else:
    print('Joe made a profit of $', format(amountLeft, ',.2f'))