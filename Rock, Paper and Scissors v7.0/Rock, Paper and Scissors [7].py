#===================NOTE===================#
#    ! Created by https://JacobEM.com      #
#       This was coded by JacobEM.com      #
# Please don't claim this as your own work #
#      * Licensed under CC-BY-SA 4.0       #
#          * All rights reserved.          #
#==========================================#
# [ -=- ] Imports [ -=- ] #

from random import randint
from time import *
import sys

# [ -=- ] Start Up [ -=- ] #

print('Welcome to Rock, Paper or Scissors!\n')

def Main():

    # [ -=- ] Defining Answers [ -=- ] #
    def UserAnswer():
        global UserChoice
        User = input('\nRock, Paper or Scissors?\n>>> ').lower()
        if User[0] == 'r':
            User = 'Rock'
        elif User[0] == 'p':
            User = 'Paper'
        elif User[0] == 's':
            User = 'Scissors'
        elif User[0] != 'r' or User[0] != 'p' or User[0] != 's':
            print('Invalid Responce! Please only enter Rock, Paper or Scissors!')
            Turn()
        UserChoice = User
    def ComputerAnswer():
        global ComputerChoice
        Computer = randint(1, 3)
        if Computer == 1:
            Computer = 'Rock'
        elif Computer == 2:
            Computer = 'Paper'
        elif Computer == 3:
            Computer = 'Scissors'
        else:
            ComputerAnswer()
        ComputerChoice = Computer

    # [ -=- ] Displaying The Result [ -=- ] #

    def ResultDisplay():
        print(f'\n{UserChoice} VS {ComputerChoice}!')

    # [ -=- ] Calculating The Result [ -=- ] #

    def Result():
        global UserChoice, ComputerChoice
        if UserChoice[0] == 'R' and ComputerChoice[0] == 'S' or UserChoice[0] == 'P' and ComputerChoice[0] == 'R' or UserChoice[0] == 'Scissors' and ComputerChoice[0] == 'Paper':
            ResultDisplay()
            print('You Win!')
        elif UserChoice[0] == 'R' and ComputerChoice[0] == 'P' or UserChoice[0] == 'P' and ComputerChoice[0] == 'S' or UserChoice[0] == 'S' and ComputerChoice[0] == 'R':
            ResultDisplay()
            print('You Lose!')
        elif UserChoice[0] == 'R' and ComputerChoice[0] == 'R' or UserChoice[0] == 'P' and ComputerChoice[0] == 'P' or UserChoice[0] == 'S' and ComputerChoice[0] == 'S':
            ResultDisplay()
            print('Draw!')
        else:
            sys.exit('There was an internal error! Please contact the developer or restarrt the program!')

    # [ -=- ] Turn [ -=- ] #
    def Turn():
        ComputerAnswer()
        UserAnswer()
        Result()
    Turn()


Main()
