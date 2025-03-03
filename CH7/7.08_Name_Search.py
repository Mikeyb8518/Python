# Write a program that reads the contents of the two files into two seperate lists.
# The user should be able to enter a boys name, girls name, or both, and the application 
# will display messages indicating whether the boy and girl are in the lists or not.

# Create a main function that opens and reads the two files into two lists
def main():
    # Boy file variable to store the contents of the boy file
    boy_file = open("BoyNames.txt", "r")
    # Girl file variable to store the contents of the girl file
    girl_file = open("GirlName.txt", "r")
    # boy list variable to store the contents of the boy file as a list
    boy_list = boy_file.readlines()
    # girl list variable to store the contents of the girl file as a list
    girl_list = girl_file.readlines()
    # variable to store the boy name
    boy_names = boy_name(boy_list)
    # variable to store the girl name
    girl_names = girl_name(girl_list)
    # variable to call the user input function
    user_input(boy_names, girl_names)
    
# Boy name function to check if the boy name is in the boy list
def boy_name(boys):
    # for loop to iterate over the boy list
    for index in range(len(boys)):
        # strip the newline character from the boy name
        boys[index] = boys[index].rstrip("\n")
    return boys

# Girl name function to check if the girl name is in the girl list
def girl_name(girls):
    # for loop to iterate over the girl list
    for index in range(len(girls)):
        # strip the newline character from the girl name
        girls[index] = girls[index].rstrip("\n")
    return girls
    
# user function to prompt the user for input
def user_input(boy_names, girl_names):
    # name variable to store the user input
    name = input("Enter a name (boy/girl/both): ")
    # if statement to check the users input
    if name in boy_names and name in girl_names:
        print(name, "is in both lists")
    elif name in boy_names:
        print(name, "is in the boy list")
    elif name in girl_names:
        print(name, "is in the girl list")
    else:
        print(name, "is not in either list")
        
# call the main function
main()