# Create a game of rock, paper, scissor. It will ask the user to enter their choice
# and then randomly select the computer's choice. It will then determine the winner
# and display the result.
import random
# create a class that will set up the game
def set_up(): 
    # set up the choices for the user and the computer
    n = random.randrange(1, 4)
    com = ''
    if n == 1:
        com = 'rock'
    elif n == 2:
        com = 'paper'
    else:
        com = 'scissor'
    choice = input('Choose and enter one among \'rock\', \'scissors\' or'
                       '\'paper\': ')
    print(com)
    return com, choice
# create a function that will determine the winner
def rule(com, choice):
    while com == choice:
        com, choice = set_up()
    else:
        if com == 'rock' and choice == 'scissors':
            print('Computer wins!')
        elif com == 'scissors' and choice == 'rock':
            print('You wins!')
        elif com == 'paper' and choice == 'scissors':
            print('You wins!')
        elif com == 'scissors' and choice == 'paper':
            print('Computer wins!')
        elif com == 'rock' and choice == 'paper':
            print('You wins!')
        elif com == 'paper' and choice == 'rock':
            print('Computer wins!')
        elif com == choice:
            print('It\'s a tie!')
# call the set_up function to start the game
def main():
    com, choice = set_up()
    rule(com, choice)
main()