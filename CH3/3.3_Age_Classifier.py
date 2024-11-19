# Write a program that asks the user to enter a person's age
# The program should display a message indicating whether the person
# is an infant, a child, a teenager, an adult

# prompt the user to ener a person's age
age = input("Enter a person's age: ")

# convert the input to an integer
age = int(age)

# check the age and display a message
if age < 1:
    print("The person is an infant")
elif age < 13:
    print("The person is a child")
elif age < 20:
    print("The person is a teenager")
else:
    print("The person is an adult")