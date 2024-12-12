# Create a program that leads a person through the steps of fixing a bad network connection
# The program will ask the user for their network connection status and then guide them through the steps to fix

# print reboot the computer and try to connect
print('Reboot the computer and try to connect\n (Y/N) Enter Y for yes, N for no')

# User input to get (Y/N) from user
user_answer = input('Did that fix the problem? ')

# if statement to get the results from the user
if user_answer == 'Y' or user_answer == 'y' or user_answer == 'N' or user_answer == 'n':
    if user_answer == 'N' or user_answer == 'n':
        print("Reboot the router and try to connect.")
        user_answer = input("Did that fix the problem? ")
        
        if user_answer == "Y" or user_answer == "y" or user_answer == "n" or user_answer == "N":
            if user_answer == "n" or user_answer == "N":
                print(" Make sure the cables \n between the router & modem\n are plugged in firmly.")
                user_answer = input("Did that fix the problem? ")

                if user_answer == "Y" or user_answer == "y" or user_answer == "n" or user_answer == "N":
                    if user_answer == "n" or user_answer == "N":
                        print("Move the router to\n to a new location\n and try to connect")
                        user_answer = input("Did that fix the problem? ")

                        if user_answer == "Y" or user_answer == "y" or user_answer == "n" or user_answer == "N":
                            print("Get a new router")
                        else:
                            print("Please enter \"Y\" for yes or \"N\" for no.\n Rerun program and try again.")
                else:
                    print("Please enter \"Y\" for yes or \"N\" for no.\n Rerun program and try again.")
        else:
            print("Please enter \"Y\" for yes or \"N\" for no.\n Rerun program and try again.")
else:
    print("Please enter \"Y\" for yes or \"N\" for no.\n Rerun program and try again.")