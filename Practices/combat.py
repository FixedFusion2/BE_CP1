# TE 2nd Combat Program
import random
print("\nWelcome to training, fist I need to know some things about you.\n")

name = input("What is your name: ")
character = input(f"Hello {name}.\nWhat class of fighter are you?\nType 1 if you are a Fighter. \nType 2 if you are a Wizard\nType 3 if you are a Cleric: ")


#Player Classes
fighter = {"Health":10, "Attack": 10, "Defense":10}

wizard = {"Health":5, "Attack": 15, "Defense":10}

cleric = {"Health":15, "Attack": 5, "Defense":10}

#Moster Classes
kobold = {"Health":15, "Attack": 5, "Defense":10}

goblin = {"Health": 5, "Attack": 15, "Defense": 10}

bandit = {"Health": 10, "Attack": 10, "Defense": 10}


if character == "1":
    print("\nYou chose Fighter!")
    print(f"Your stats are:\n{fighter}")
elif character == "2":
    print("\nYou chose Wizard!")
    print(f"Your stats are:\n{wizard}")
elif character == "3":
    print("\nYou chose Cleric!")
    print(f"Your stats are:\n{cleric}")
else:
    print("Invalid choice! Defaulting to Fighter.")
    player = fighter
    player["Name"] = "Fighter"

#Monster Selection
monster_choice = input(
    "\nDo you want to battle a:\n"
    "1 - Goblin (Health 5, Attack 15, Defense 10)\n"
    "2 - Bandit (Health 10, Attack 10, Defense 10)\n"
    "3 - Kobold (Health 15, Attack 5, Defense 10)\n"
    "Enter your choice: "
)

if monster_choice == 1:
    monster = goblin
elif monster_choice == 2:
    monster = bandit
elif monster_choice == 3:
    monster = goblin   
else:
    print("Invalid choice defaulting to golbin!")
    monster = goblin

#Random who goes first
turn = random.choice(["player", "monster"])
print("\nYou move first!" 
      
if turn == "player" else f"\nThe {monster['Name']} moves first!")

#Player Turn
def player_turn():
    print("\nYour turn. What do you want to do?")
    print("1-Normal Attack")
    print("2-Wild Attack (Double dammage but hurt yourself)")
    print("3-Heal (+8 HP)")
    print("4-Flee (Chance to escape)")

    choice = input(">")

    if choice == "1":
        hit = random.randint(1,20)
        if hit >= monster ["Defense"]:
            damage = random.randint(1, player["Attack"])
            monster["Health"] -= damage
            print(f"You hit {monster["Name"]} for {damage} damage!")
        else:
            print("You missed!")

    elif choice == "2":
        hit = random.randint(1,20)
        if hit >= monster["Defense"]:
            damage = random.randint(1,player["Attack"])*2
            monster ["Health"] -= damage
            recoil = random.randint(2,5)
            player["Health"] -= recoil
            print(f"You go wild! Deal {damage} but take {recoil} recoil damage.")
        else:
            print(f"You swing wildly and miss!")

    elif choice == "3":
        heal = 8
        player["Health"] += heal
        print(f"You drink a potion and heal {heal} HP!")


    elif choice == "4":
        if random.random() < 0.4:
            print("You escaped successfully!")
            return "fled"
        else:
            print("You failed to flee!")


    else:
        print("Invalid choice! You lose your turn.")

    return "continue"


#Monster Turn
def monster_turn():
    print(f"\nThe {monster["Name"]} attacks!")
    hit = random.randint(1,20)
    if hit >= player["Defense"]:
        damage = random.randint(1,monster["Attack"])
        player["Health"] -= damage
        print(f"The {monster["Name"]} hits you for {damage} damage!")
    else:
        print(f"The {monster["Name"]} missed!")  


#Main game loop
while player["Health"] >0 and monster["Health"] > 0:
    if turn == "player":
        result = player_turn()
        if result == "fled":
            break
    else:
        monster_turn()
        turn = "player"

    print(f"\nYour HP: {player["Health"]} | {monster["Name"]} HP: {monster["Health"]} ")


#End of battle
if player["Health"] <= 0:
    print(f"\nYou were defeated by the {monster["Name"]}!")
elif monster["Health"] <= 0:
    print(f"You defeated the {monster["Name"]}! Victory!")
else:
    print("\nYou escaped the battles safely!")      