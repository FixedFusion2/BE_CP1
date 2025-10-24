# TE 2nd Combat Program
import random
print("\nWelcome to training, fist I need to know some things about you.\n")

name = input("What is your name: ")
character = input(f"Hello {name}.\nWhat class of fighter are you?\nType 1 if you are a Fighter. \nType 2 if you are a Wizard\nType 3 if you are a Cleric: ")

health = 15
defense = 15
attack = 15
hit = random.randint(1,16)
fighter = print(f"You chose fighter.\nYour stats are:\nHealth, {health+10}\nDefense, {defense-5}\nAttack, {attack+15}")
wizard = print(f"You chose Wizard.\nYour stats are:\nHealth, {health+15}\nDefense, {defense+5}\nAttack, {attack+10}")
cleric = print(f"You chose Cleric.\nYour stats are:\nHealth, {health+10}\nDefense, {defense+15}\nAttack, {attack+5}")
if character == "1":
    print(fighter)
elif character == "2":
    print(wizard)
elif character == "3":
    print(cleric)


def combat():
    monster = random.randint(1,4)
    if monster == 1:
        print("A Goblin attacks you!")
    elif monster == 2:
        print("A bandit attacks you!")
    elif monster == 3:
        print("A Kobold attacks you!")
    
