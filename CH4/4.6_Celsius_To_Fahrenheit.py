# Write a program that asks the user to enter a degree in celsius and then will convert it to a 
# degree in fahrenheit. The program will then ask the user if they want to convert another temperature

# print table
print('Celsius\t','Fahrenheit')
print('-' * 20)

# for loop to calculate and display results
for c in range(21):
    print(format(c, '2.0f'), '\t', format(9 / 5 * c + 32, '.2f'))