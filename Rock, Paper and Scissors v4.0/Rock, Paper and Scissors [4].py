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
if user == "Rock" and chosen == "Rock":
    sys.exit("Game Over! It was a draw!")
elif user == "Rock" and chosen == "Paper":
    sys.exit("Game Over! You lost!")
elif user == "Rock" and chosen == "Scissors":
    sys.exit("Congratulations! You Win!")

elif user == "Paper" and chosen == "Rock":
    sys.exit("Congratulations! You Win!")
elif user == "Paper" and chosen == "Paper":
    sys.exit("Game Over! It was a draw!")
elif user == "Paper" and chosen == "Scissors":
    sys.exit("Game Over! You lost!")

elif user == "Scissors" and chosen == "Rock":
    sys.exit("Game Over! You lost!")
elif user == "Scissors" and chosen == "Paper":
    sys.exit("Congratulations! You Win!")
elif user == "Scissors" and chosen == "Scissors":
    sys.exit("Game Over! It was a draw!")
