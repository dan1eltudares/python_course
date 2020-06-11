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









print(rock_paper_scissors('paper', 'scissors') == 'scissors win!')
print(rock_paper_scissors('scissors', 'rock') == 'rock wins!')
print(rock_paper_scissors('rock', 'paper') == 'paper wins!')
print(rock_paper_scissors('rock', 'rock') == 'draw!')
print(rock_paper_scissors('paper', 'paper') == 'draw!')
print(rock_paper_scissors('scissors', 'scissors') == 'draw!')
# Challenge mode! Uncomment these tests if you want, and write code that passes the earlier tests and these!
#  HINT: nested if statements help a lot here ;)
#print(rock_paper_scissors('scissors', 'paper') == 'scissors win!')
#print(rock_paper_scissors('rock', 'scissors') == 'rock wins!')
#print(rock_paper_scissors('paper', 'rock') == 'paper wins!')
#print(rock_paper_scissors('papaya', 'rockette') == 'invalid input')
#print(rock_paper_scissors('apple', 'sword') == 'invalid input')