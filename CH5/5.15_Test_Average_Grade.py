# Prompt the user to enter 5 test scores, then write two functions. One to calculate the average of the test scores
# and another to determine the grade of the score.

# prompt the user to enter 5 test scores
a = int(input('Enter a score for test a: '))
b = int(input('Enter a score for test b: '))
c = int(input('Enter a score for test c: '))
d = int(input('Enter a score for test d: '))
e = int(input('Enter a score for test e: '))

# function to calculate the average of the test scores
def Cal_average(a, b, c, d, e):
    average = (a + b + c + d + e) / 5
    
    # return the average
    return average

# determine the grade of the test score average
def determine_grade(a, b, c, d, e):
    for i in a, b, c, d, e:
        if 90 <= i:
            print('The grade of', i, 'is A')
        elif 80 <= i <= 89:
            print('The grade of', i, 'is B')
        elif 70 <= i <= 79:
            print('The grade of', i, 'is C')
        elif 60 <= i <= 69:
            print('The grade of', i, 'is D')
        elif i < 60:
            print('The grade of', i, 'is F')
            
average = Cal_average(a, b, c, d, e)
print('The average of the test scores is:', average)
determine_grade(a, b, c, d, e)