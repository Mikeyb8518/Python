# Program that calculates compound interest over amount of years
# User will need to enter the principal amount deposited
# User will need to enter the interest rate paid by the account
# User will need to enter number of times per year the interest is compounded
# User will enter the number of years the account will be left to earn income

# Variable to hold the principal amount
P = float(input('Enter the principal amount: $'))

# Variable to hold the interest rate
r = float(input('Enter the interest rate %'))

# variable number of times per year interest is compounded
n = float(input('Enter the number of times per year interest is compounded: '))

# variable to hold the number of years the account will be left to earn income
t = float(input('Enter the number of years the account will be left to earn income: '))

# formula to turn percentage to decimal
r /= 100

# Formula to calculate compound interest
A = P * ((1 + r/n)**(n*t))

# Display results
print('After ', t, ' years, $', format(A, ',.2f'), ' will be in the account. ', sep='')