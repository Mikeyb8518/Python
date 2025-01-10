# Write a program that will take your savings and earns compound monthly interest

# Vairables for present value, monthly interest and amount of months
present_value = float(input('Enter the amount of money in your account: $'))
monthly_interest_rate = float(input('Enter the monthly interest rate: '))
month = int(input('Enter the amount of months that the money will be left for: '))

# Function to calculate the future value
def calculate(present_value, monthly_interest_rate, month):
    f = present_value * ((1 + monthly_interest_rate / 100) ** month)
    # print the result
    print('The amount\'s future value is $', format(f, '.2f'), sep='')

# call function to display results
calculate(present_value, monthly_interest_rate, month)
