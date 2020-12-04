'''
# Logic puzzle time!
# We are going to make a function that determines the winner of a game of rock paper scissors
# The function will ask ask both players to select a choice, the first to win 3 rounds is the champion.  
# The rules of rock paper scissors are:
# Paper beats rock
# Rock beats scissors
# Scissors beats paper
# Two of the same choice is a draw
'''


from getpass import getpass

def rock_paper_scissors():
    score_p1 = 0
    score_p2 = 0
    player1 = input("Player 1 name: ")
    player2 = input("Player 2 name: ")
    print("\nWelcome to rock, paper, scissors! - The first to win 3 rounds is the champion!\n")

    while score_p1 <= 3 and score_p2 <= 3:
        if score_p1 == 3:
            print(player1 + " won 3 rounds, congratulations!!")
            break
        elif score_p2 == 3:
            print(player2 + " won 3 rounds, congratulations!!")   
            break 
        print("Current Score: " + player1 + " = " + str(score_p1) + " ," + player2 + " = " + str(score_p2) + "\n")
        select_p1 = getpass( player1 + ", pick your weapon (rock, paper, scissors): ").lower()
        select_p2 = getpass( player2 + ", pick your weapon (rock, paper, scissors): ").lower()
        if select_p1 == select_p2:
            print("\n It's a draw! - No points, Try again\n")
        elif select_p1 == "paper":
            if select_p2 == "scissors":
                print("\n scissors wins! - Point for " + player2 + "\n")
                score_p2 += 1
            elif select_p2 == "rock":
                print("\n paper wins! - Point for " + player1 + "\n")
                score_p1 += 1
            else:
                print("\n " + player2 + " ,you made an invalid input - Try again \n")
        elif select_p1 == "scissors":
            if select_p2 == "paper":
                print("\n scissors wins! - Point for " + player1 + "\n")
                score_p1 += 1
            elif select_p2 == "rock":
                print("\n rock wins! - Point for " + player2 + "\n")
                score_p2 += 1
            else:
                print("\n " + player2 + " ,you made and invalid input - Try again \n")
        elif select_p1 == "rock":
            if select_p2 == "scissors":
                print("\n rock wins! - Point for " + player1 + "\n")
                score_p1 += 1
            elif select_p2 == "paper":
                print("\n paper wins! - Point for " + player2 + "\n")
                score_p2 += 1
            else:
                print("\n " + player2 + " ,you made an invalid input - Try again \n")
        elif ((select_p1 != "paper") or (select_p1 != "scissors") or (select_p1 != "rock")) and ((select_p2 == "paper") or (select_p2 == "scissors") or (select_p2 == "rock")):
            print("\n " + player1 + " ,you made an invalid input - Try again \n")
        else:
            print("\n both users invalid input - Try again \n")

rock_paper_scissors()