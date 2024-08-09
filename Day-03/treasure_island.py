print(
    '''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."/` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
'''
)
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

hall = input(
    "You've stumbled upon a mysterious hall. Do you go left or right? (type 'left' or right') "
)
hall = hall.lower()
if hall == "left":
    river = input(
        "The hall leads to a river. Do you swim or wait to find a boat? (type 'swim' or 'boat') "
    )
    river = river.lower()
    if river == "boat":
        color = input(
            "You come across three doors distinctly colored.. Do you choose the the red, yellow or the blue door? (type 'red', yellow or 'blue) "
        )
        color = color.lower()
        if color == "yellow":
            print("You win!")
        elif color == "red":
            print("You burn to death by fire. Game over.")
        elif color == 'blue':
            print("You have been eaten by beast. Game over.")
        else:
            print('You lose!')
    else:
        print("You were attacked by trout. Game over.")
else:
    print("There was a hole and fell to your death. Game over.")
