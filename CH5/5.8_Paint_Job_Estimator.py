# Write a program that asks the user to enter the number of square feet of wall space
# that needs to be painted. Then, ask the user to enter the price of the paint
# The prgram should display number of gallons of paint required
# hours of labor required, cost of the paint, labor charges, total cost of the paint job

# variables to prompt the user to enter the square feet of wall space, cost of paint
area = float(input("Enter the number of square feet of wall space: "))
cost_paint = float(input("Enter the price of the paint: "))

# calculate function to calculate the number of gallons of paint required, hours of labor required, cost of the paint, labor
# charges, total cost of the paint job
def calculate(area, cost_paint):
    # number of gallons of paint required
    print('The number of gallons of paint required is', format(area / 112, '.2f'))
    # hours of labor required
    print('The hours of labor required is', format(area / 112 * 8, '.2f'))
    # cost of the paint
    print('The cost of the paint is $', format(area / 112 * cost_paint, '.2f'), sep='')
    # labor charges
    print('The labor charges is $', format(area / 112 * 8 * 35, '.2f'), sep='')
    # total cost of the paint job
    print('The total cost of the paint job is $', format(area / 112 * cost_paint + area / 112 * 8 * 35, '.2f'), sep='')
    
calculate(area, cost_paint)  # call the function with the user input values