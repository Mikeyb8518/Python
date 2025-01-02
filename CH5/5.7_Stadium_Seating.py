# Write a program for stadium seating there are 3 categories of seats, A, B, and C.
# The price of the seats are $20, $15, and $10 respectively.
# The program should ask the user for the number of seats they want to buy and the category of
# seats they want to buy. Then it should calculate the total cost of the seats and display it

# Call the function to start the program
class_A = int(input('Enter the number of seats sold for class A: '))
class_B = int(input('Enter the number of seats sold for class B: '))
class_C = int(input('Enter the number of seats sold for class C: '))

def total(class_A, class_B, class_C):
    a = class_A * 20
    b = class_B * 15
    c = class_C * 10
    # Print total
    print(f'Total cost of seats sold is ${a + b + c}')
    
total(class_A, class_B, class_C)  # Call the function with the user input