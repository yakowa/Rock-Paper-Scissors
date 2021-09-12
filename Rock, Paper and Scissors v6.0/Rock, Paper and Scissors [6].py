#===================NOTE===================#
#    ! Created by https://JacobEM.com      #
#       This was coded by JacobEM.com      #
# Please don't claim this as your own work #
#      * Licensed under CC-BY-SA 4.0       #
#          * All rights reserved.          #
#==========================================#
from random import randint
import random
import sys

# Added on 30/01/2021
global databaseLocationDirectory
databaseLocationDirectory = {
    "results": "C:\\[Desktop]\\[Programming]\\[Projects]\\Rock Paper Scissors\\Rock, Paper and Scissors v6.0\\results.txt",
}

def main():
    results=open(databaseLocationDirectory["results"], "a")
    def playagain():
        question=input("Do you want to play again? Type: 'Yes' (Y) or 'No' (N)   Your input: ").upper()
        if question == "YES" or question == "Y":
            main()
        else:
            results.write("\n--------------\nNew Session.\n--------------\n")
            results.close()
            sys.exit("kk, bai")
    while True:
        chosen="none"
        RPS=randint(1,3)
        if RPS == 1:
            chosen = "Rock"
        elif RPS == 2:
            chosen = "Paper"
        elif RPS == 3:
            chosen = "Scissors"
        user=str(input("Please select Rock (R), Paper (P) or Scissors (S)! Your answer: "))
        if user == "r" or user == "R" or user == "rock":
            user = "Rock"
        elif user == "p" or user == "P" or user == "paper":
            user = "Paper"
        elif user == "s" or user == "S" or user == "scissors":
            user = "Scissors"
        else:
            sys.exit("Error: That is not an acceptable answer!")
        print("------------")
        print("Your answer:", user)
        print("------------")
        print("Computer's answer:", chosen)
        print("------------")
        if user == "Rock" and chosen == "Rock" or user == "Paper" and chosen == "Paper" or user == "Scissors" and chosen == "Scissors":
            print("Game Over! It was a draw!")
            results.write("\nDraw\n")
            results.close()
            playagain()
        elif user == "Rock" and chosen == "Paper" or user == "Paper" and chosen == "Scissors" or user == "Scissors" and chosen == "Rock":
            print("Game Over! You lost!")
            results.write("\nLose\n")
            results.close()
            playagain()
        elif user == "Rock" and chosen == "Scissors" or user == "Paper" and chosen == "Rock" or user == "Scissors" and chosen == "Paper":
            print("Congratulations! You Win!")
            results.write("\nWin\n")
            results.close()
            playagain()
main()
