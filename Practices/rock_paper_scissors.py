# TE 2nd Rock, Paper, Scissors!

import random
import time
def slow_print(text, delay=0.05):
    """Print text slowly, character by character"""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)

slow_print("\nWelcome to rock, paper, scissors!\n")

slow_print("\nYou will be going up against Mr. Mainframe!\n")

mr_m = random.randint(1,3)
# 1 beats 3
# 3 beats 2
# 2 beats 1
slow_print("\nPress 1 to use ROCK, Press 2 to use PAPER, Press 3 to use SCISSORS\n")
action = input("\nCHOOSE YOUR FIGHTER (1-3): ")

while True:
    if action == 1 and mr_m == 3:
        slow_print("\nYou played ROCK beating SCISSORS\n")
        slow_print("\nYou beat Mr. Mainframe!\n")
    elif action == 3 and mr_m == 2:
        slow_print("\nYou played SCISSORS beating PAPER\n")
        slow_print("\nYou beat Mr. Mainframe!\n")
    elif action == 2 and mr_m == 1:
        slow_print("\nYou played PAPER beating ROCK\n")
        slow_print("\nYou beat Mr. Mainframe!\n")