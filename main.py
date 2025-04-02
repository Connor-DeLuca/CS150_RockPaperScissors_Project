import random

score = {'wins':0,'losses':0,'ties':0}

choices = ['rock','paper','scissors']

wantsToPlayAgain = ''

def win():
    global wantsToPlayAgain
    print('You win!')
    score['wins'] = score['wins'] + 1
    wantsToPlayAgain = input('Would you like to play again? Type yes or no: ').lower()

# The user can exit by typing no at the end
while wantsToPlayAgain != 'no':
    useraction = input('Enter rock, paper, or scissors to play: ').lower()
    computeraction = choices[random.randint(0,2)]
    print(computeraction)

    if useraction == 'rock':
        if computeraction == 'scissors':
            win()

    print('The current score is: \n ' + str(score))