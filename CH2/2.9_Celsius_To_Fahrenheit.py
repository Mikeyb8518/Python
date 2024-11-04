# Write a program that caluclates Celsius to fahrenheit

#prompt user to enter a  temperature in Celsius
celsius =  float(input("Enter a temperature in Celsius: "))

# Constant that hold the conversion of  Celsius to Fahrenheit
CELSIUS_TO_FAHRENHEIT = ((9/5) * celsius) + 32

# display results
print('The degree in  Fahrenheit is: ', CELSIUS_TO_FAHRENHEIT, sep='')