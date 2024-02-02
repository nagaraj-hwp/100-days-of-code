print('''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to the Treasure Island.")
print("Your mission is to find the treasure")
print("Choose wisely")

direction = input("Do you wanna choose left or right? \n").lower()
if direction == "right":
    print("There is a assasin to the right side wrong choice, Game over")
elif direction == "left":
    print("You choose left")
    transport = input(
        "You have reached lake, you wanna swim or wait for the boat? \n").lower()
    if transport == "swim":
        print("Oh! bad choice, lake is full of crocodiles, game over")
    elif transport == "wait":
        print("Good Choice, You have reached the doors")
        door = input("select between 3 doors, red, blue or yellow? \n").lower()
        if door == "red":
            print(
                "You have choose red door, there is a beast behind the door, Game Over.")
        elif door == "blue":
            print("You have choose blue door, Its full of fire, Game Over.")
        elif door == "yellow":
            print(
                "You have choose Yellow door, There is a chest of gold and diamonds, You won.")
        else:
            print("Your chosen door doesn't exist, You are fired, Game Over.")
    else:
        print("You get attacked by an angry trout. Game Over.")
else:
    print("Your fell into a hole, Game Over.")
