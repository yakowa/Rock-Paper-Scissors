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
def main():
    def playagain():
        question=input("Do you want to play again? Type: 'Yes' (Y) or 'No' (N)   Your input: ").upper()
        if question == "YES" or question == "Y":
            main()
        else:
            print("kk, baii")
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
            playagain()
        elif user == "Rock" and chosen == "Paper" or user == "Paper" and chosen == "Scissors" or user == "Scissors" and chosen == "Rock":
            print("Game Over! You lost!")
            playagain()
        elif user == "Rock" and chosen == "Scissors" or user == "Paper" and chosen == "Rock" or user == "Scissors" and chosen == "Paper":
            print("Congratulations! You Win!")
            playagain()
main()
