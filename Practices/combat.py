# TE 2nd Combat Program
import random
print("\nWelcome to training, fist I need to know some things about you.\n")

name = input("What is your name: ")
character = input(f"Hello {name}.\nWhat class of fighter are you?\nType 1 if you are a Fighter. \nType 2 if you are a Wizard\nType 3 if you are a Cleric: ")

hit = random.randint(1,16)

fighter = {"Health":10, "Attack": 10, "Defense":10}

wizard = {"Health":5, "Attack": 15, "Defense":10}

cleric = {"Health":15, "Attack": 5, "Defense":10}

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

monster = input("\nDo you want to battle a Goblin (Health 5, Attack 15, Defense 10)\n\n A Bandit (Health 10, Attack 10, Defense 10)\n\nor A Kobold (Health 15, Attack 5, Defense 10)\n\n(Enter 1 for Goblin, 2 for Bandit, and 3 for Cleric):")

if monster == 1:
    print("\nA Goblin attacks you!")
    print(f"The goblins stats are: \n{goblin}")
elif monster == 2:
    print("\nA Bandit attacks you!")
    print(f"The Bandits stats are: \n{bandit}")
elif monster == 3:
    print("\nA Kobold attacks you!")
    print(f"The Kobolds stats are: \n{kobold}")
    
