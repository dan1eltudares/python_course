'''
# Logic puzzle time!
# We are going to make a function that determines the winner of a game of rock paper scissors
# The function will accept two arguments and return which object (rock, paper, or scissors) wins
# The rules of rock paper scissors are:
# Paper beats rock
# Rock beats scissors
# Scissors beats paper
# Two of the same choice is a draw
# Examine the test cases below to see example inputs and outputs before beginning! 
'''

# First case, without challenge mode:
def rock_paper_scissors(player1,player2):
    if player1 == 'paper' and player2 == 'scissors':
        return 'scissors win!'
    elif player1 == 'scissors' and player2 == 'rock':
        return 'rock wins!'
    elif player1 == 'rock' and player2 == 'paper':
        return 'paper wins!'
    elif player1 == 'rock' and player2 == 'rock':
        return 'draw!'
    elif player1 == 'paper' and player2 == 'paper':
        return 'draw!'
    elif player1 == 'scissors' and player2 == 'scissors':
        return 'draw!'
    else:
        return 'invalid input'


# Second case, with challenge mode:
def rock_paper_scissors(player1,player2):
    if (player1 == 'paper' and player2 == 'scissors') or (player1 == 'scissors' and player2 == 'paper'):
        return 'scissors win!'
    elif (player1 == 'scissors' and player2 == 'rock') or (player1 == 'rock' and player2 == 'scissors'):
        return 'rock wins!'
    elif (player1 == 'rock' and player2 == 'paper') or (player1 == 'paper' and player2 == 'rock'):
        return 'paper wins!'
    elif player1 == 'rock' and player2 == 'rock':
        return 'draw!'
    elif player1 == 'paper' and player2 == 'paper':
        return 'draw!'
    elif player1 == 'scissors' and player2 == 'scissors':
        return 'draw!'
    else:
        return 'invalid input'

# challenge mode with nested IF:
def rock_paper_scissors(player1,player2):
    if player1 == 'paper':
        if player2 == 'scissors':
            return 'scissors win!'
        elif player2 == 'paper':
            return 'draw!'
        elif player2 == 'rock':
            return 'paper wins!'
    elif player1 == 'scissors':
        if player2 == 'rock':
            return 'rock wins!'
        elif player2 == 'scissors':
            return 'draw!'
        elif player2 == 'paper':
            return 'scissors win!'
    elif player1 == 'rock':
        if player2 == 'paper':
            return 'paper wins!'
        elif player2 == 'rock':
            return 'draw!'
        elif player2 == 'scissors':
            return 'rock wins!'
    else:
        return 'invalid input'


print(rock_paper_scissors('paper', 'scissors') == 'scissors win!')
print(rock_paper_scissors('scissors', 'rock') == 'rock wins!')
print(rock_paper_scissors('rock', 'paper') == 'paper wins!')
print(rock_paper_scissors('rock', 'rock') == 'draw!')
print(rock_paper_scissors('paper', 'paper') == 'draw!')
print(rock_paper_scissors('scissors', 'scissors') == 'draw!')
# Challenge mode! Uncomment these tests if you want, and write code that passes the earlier tests and these!
#  HINT: nested if statements help a lot here ;)
print(rock_paper_scissors('scissors', 'paper') == 'scissors win!')
print(rock_paper_scissors('rock', 'scissors') == 'rock wins!')
print(rock_paper_scissors('paper', 'rock') == 'paper wins!')
print(rock_paper_scissors('papaya', 'rockette') == 'invalid input')
print(rock_paper_scissors('apple', 'sword') == 'invalid input')