import random

score = {'wins':0,'losses':0,'ties':0}

choices = ['rock','paper','scissors']

wantsToPlayAgain = ''
# The user can exit by typing nothing
while wantsToPlayAgain != 'no':
    useraction = input('Enter rock, paper, or scissors to play. Type nothing to exit the program.').lower()
    computeraction = choices[random.randint(0,2)]
    print(computeraction)

    if useraction == 'rock':
        if computeraction 