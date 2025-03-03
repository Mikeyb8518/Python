# Write a program that will take file "answers.txt" and compare it to the correct answers
# also if the user gets less than 15 answers wrong, print the user failed the exam

# Correct answers function holding a list of correct answers
def correct_answers():
    correct_list = ['A', 'C', 'A', 'A', 'D', 'B', 'C', 'A', 'C', 'B',
                    'A', 'D', 'C', 'A', 'D', 'C', 'B', 'B', 'D', 'A']
    return correct_list

# Function that takes the file and compares it to the correct answers
def compare_answers():
    answers_list = []
    object_file = open('answers.txt', 'r')
    for i in object_file:
        i = i.rstrip('\n')
        answers_list.append(i)
    return answers_list

# Function to check the number of wrong answers
def check(correct_list, answers_list):
    # set the count to 0
    count = 0
    print(correct_list)
    print(answers_list)
    # loop through the list of answers and compare them to the correct answers
    wrong_answers =[]
    for i in range(20):
        if correct_list[i] == answers_list[i]:
            count += 1
        else:
            wrong_answers.append(i)
            count += 0
    if count < 15:
        print("You failed the exam")
    else:
        print("You passed")
    
    print("The number of correctly answered questions is: ", count)
    print("The number of incorrectly answered questions is: ", 20 - count)
    print("The question numbers of the wrong answers are: ", wrong_answers)
    
# Main function
def main():
    correct_list = correct_answers()
    answers_list = compare_answers()
    check(correct_list, answers_list)
main()