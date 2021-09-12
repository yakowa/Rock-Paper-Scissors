#===================NOTE===================#
#    ! Created by https://JacobEM.com      #
#       This was coded by JacobEM.com      #
# Please don't claim this as your own work #
#      * Licensed under CC-BY-SA 4.0       #
#          * All rights reserved.          #
#==========================================#
from random import randint

player=str(input('Please choose an option: Rock (r), Paper (p) or Scissors (s) Your answer: '))

if player == 'rock':
    player = 'Rock'

elif player == 'Rock':
    player = 'Rock'

elif player == 'r':
    player = 'Rock'
    
elif player == 'R':
    player = 'Rock'


if player == 'paper':
    player = 'Paper'

elif player == 'Paper':
    player = 'Paper'

elif player == 'p':
    player = 'Paper'

elif player == 'P':
    player = 'Paper'


if player == 'Scissors':
    player = 'Scissors'

elif player == 'scissors':
    player = 'Scissors'

elif player == 's':
    player = 'Scissors'

elif player == 'S':
    player = 'Scissors'


chosen=randint(1,3)

computer=0
if chosen == 1:
    computer = 'Rock'

elif chosen == 2:
    computer = 'Paper'

elif chosen == 3:
    computer = 'Scissors'


print("")
print("---------")
print("Your answer: ")
print(player)
print("---------")
print("Computer's answer: ")
print(computer)
print("---------")
print("")
print(player, 'vs', computer)
