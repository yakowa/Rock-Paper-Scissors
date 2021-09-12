#===================NOTE===================#
#    ! Created by https://JacobEM.com      #
#       This was coded by JacobEM.com      #
# Please don't claim this as your own work #
#      * Licensed under CC-BY-SA 4.0       #
#          * All rights reserved.          #
#==========================================#
from random import randint

player=input('Please choose an option: Rock, Paper or Scissors Your answer: ')

chosen=randint(1,3)

computer=0
if chosen == 1:
    computer = 'Rock'

elif chosen == 2:
    computer = 'Paper'

else:
    computer = 'Scissors'

print(player, 'vs', computer)
