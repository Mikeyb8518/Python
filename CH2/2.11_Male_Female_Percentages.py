# Make a program that asks the user for the numner of male and number of female
# registered in a class. Program should display the percentage of males and females in  the class.

# variable to prompt user to enter number of males and females in class
num_Of_Males = int(input('Enter number of Males in class: '))
num_Of_Females = int(input('Enter number of Females in class: '))

#  calculate total number of students in class
total_In_Class =  num_Of_Males + num_Of_Females

# calculate percentage of males in class
percent_Males =  (num_Of_Males / total_In_Class) * 100
# calculate percentage of females in class
percent_Females =  (num_Of_Females / total_In_Class) * 100

# display the percentage of males and females in the class
print('Number of males in class is:', percent_Males,'%')
print('Number of females in class is:', percent_Females,'%')