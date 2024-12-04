# Assume hotdogs come in a package of 10, and hotdog buns come in package of 8
# Design a program that will calculate the number of packages of hotdogs and buns needed to make a certain number of
# hotdogs. The program should ask the user for the number of people attending the cookout and the number of hotdogs each
# person will eat. It should then calculate and display the number of packages of hotdogs and buns needed.

# Prompt user for the number of people attending the cookout and the number of hotdogs each person will eat
people = int(input('Please enter the number of people attending the cookout: '))
hotdogs = int(input('Please enter the number of hot dogs each person will be given: '))

# Calculate the total number of hotdogs needed
if people * hotdogs % 8 == 0 and people * hotdogs % 10 == 0:
    print(people * hotdogs // 8, 'of packages of hot dog buns required.')
    print(people * hotdogs // 10, 'of packages of hot dogs required.')
    print('The number of hot dog buns that will be left over is 0')
    print('The number of hot dogs that will be left over is 0')
elif people * hotdogs % 8 == 0 and people * hotdogs % 10 != 0:
    print(people * hotdogs // 8, 'of packages of hot dog buns required.')
    print(people * hotdogs // 10 + 1, 'of packages of hot dogs required.')
    print('The number of hot dog buns that will be left over is', people * hotdogs % 8)
    print('The number of hot dogs that will be left over is', 
         (people * hotdogs // 10 + 1) * 10 - people * hotdogs)  
elif people * hotdogs % 8 != 0 and people * hotdogs % 10 == 0:
    print(people * hotdogs // 8 + 1, 'of packages of hot dog buns required.')
    print(people * hotdogs // 10, 'of packages of hot dogs required.')
    print('The number of hot dog buns that will be left over is',
         (people * hotdogs // 8 + 1) * 8 - people * hotdogs)
    print('The number of hot dogs that will be left over is', people * hotdogs % 10)
else:
    print(people * hotdogs // 8 + 1, 'of packages of hot dog buns required.')
    print(people * hotdogs // 10 + 1, 'of packages of hot dogs required.')
    print('The number of hot dog buns that will be left over is',
         (people * hotdogs // 8 + 1) * 8 - people * hotdogs)
    print('The number of hot dogs that will be left over is',
         (people * hotdogs // 10 + 1) * 10 - people * hotdogs) 