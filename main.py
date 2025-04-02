import random

score = {'wins':0,'losses':0,'ties':0}

choices = ['rock','paper','scissors']

wantsToPlayAgain = ''

def win():
    global wantsToPlayAgain
    print('You win!')
    score['wins'] = score['wins'] + 1
    # Prints the score
    print('The current score is: \n ' + str(score))
    wantsToPlayAgain = input('Would you like to play again? Type yes or no: ').lower()

def loss():
    global wantsToPlayAgain
    print('You lose!')
    score['losses'] = score['losses'] + 1
    # Prints the score
    print('The current score is: \n ' + str(score))
    wantsToPlayAgain = input('Would you like to play again? Type yes or no: ').lower()

def tie():
    global wantsToPlayAgain
    print('You tied!')
    score['ties'] = score['ties'] + 1
    # Prints the score
    print('The current score is: \n ' + str(score))
    wantsToPlayAgain = input('Would you like to play again? Type yes or no: ').lower()


# The user can exit by typing no at the end
while wantsToPlayAgain != 'no':
    useraction = input('Enter rock, paper, or scissors to play: ').lower()
    computeraction = choices[random.randint(0,2)]
    print(f'The computer chose {computeraction}.')

    if useraction == 'rock':
        if computeraction == 'scissors':
            win()
        if computeraction == 'paper':
            loss()
        if computeraction == 'rock':
            tie()
    elif useraction == 'paper':
        if computeraction == 'rock':
            win()
        if computeraction == 'scissors':
            loss()
        if computeraction == 'paper':
            tie()
    elif useraction == 'scissors':
        if computeraction == 'paper':
            win()
        if computeraction == 'rock':
            loss()
        if computeraction == 'scissors':
            tie()
    else:
        print('Not a valid choice. Please try again.')
        # Loop restarts
