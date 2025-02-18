# Write a program that reads the contents of the file into a list. The program should then
# ask the user to enter a charge account number. The program should determine whether
# the number is valid by searching for it in the list. If the number is in the list, 
# the program should display a message indicating that the number is valid. If the
# number is not in the list, the program should display a message indicating that the
# number is invalid.

# Function that will read the contents of the file into a list
def read(object_file):
    # variable to hold the list of charge account numbers
    account_list = []
    # variable to set index to 0
    index = 0
    # loop to read the file and add each line to the list
    for i in object_file:
        i = i.rstrip('\n')
        account_list.append(i)
    return account_list
# Function that will check if the charge account number is valid
def check(account_list):
    # variable to prompt user to enter a charge account number
    number = input("Please enter a charge account number: ")
    
    # if statement to check if the number is in the list
    if number in account_list:
        # if the number is in the list, print a message indicating that the number is valid
        print(number, 'was found in the list. This number is valid.')
    else:
        # if the number is not in the list, print a message indicating that the number is invalid
        print(number, 'was not found in the list. This number is invalid.')
        
# main function
def main():
    # object_file variable that will open the file and read it into a list
    object_file = open('Charge_Account.txt', 'r')
    # call the read function and store the result in account_list
    account_list = read(object_file)
    # call the check function and pass account_list as an argument
    check(account_list)
# call the main function
main()
#2098457