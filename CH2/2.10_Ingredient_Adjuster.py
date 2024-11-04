# Program that calculates the amount of ingredients it would take
# for the user input of amount of cookies they are looking to make

#User input to get the amount of cookies the user is loooking to make
num_of_cookies =  int(input("How many cookies are you looking to make? "))

#constants  for the ingredients
COOKIES = 48
SUGAR = 1.5
BUTTER =  1
FLOUR = 2.75

# variables to get the amount of ingredients from the amount
# of cookies the user is looking to make
total_sugar = (SUGAR * num_of_cookies) / COOKIES
total_butter = (BUTTER * num_of_cookies) / COOKIES
total_flour = (FLOUR * num_of_cookies) / COOKIES

# Display results
print('\nNumber of cookies =', num_of_cookies, end='\n\n')
print('Total sugar =', format(total_sugar, ',.2f'), 'cups of sugar')
print('Total butter =', format(total_butter,  ',.2f'),  'cup of butter')
print('Total flour =', format(total_flour, ',.2f'), 'cups of flour',  end='\n\n')
