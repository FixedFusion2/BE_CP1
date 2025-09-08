# TE 2nd Basic Calculator

import time
def slow_print(text, delay=0.05):
    """Print text slowly, character by character"""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)

slow_print("\nBasic Calculator Opened.\n")
slow_print("This calculator can add, subtract, mulityply, divide, integer divide, modulo, and raise numbers.\n")

slow_print("Operations: (+, -, *, /, //, %, **)\n")

equation = slow_print("\n Press 1 to add (+).\n Press 2 to subtract (-).\n Press 3 to multiply (*).\n Press 4 to divide (/).\n Press 5 to integer divide (//).\n Press 6 to modulo (%).\n Press 7 to raise (**).\n")

if equation == "1":
    num = input("Enter your equation:")
    print(eval(num)) 

if equation == "2":
    num = input("Enter your equation:")
    print(eval(num))

if equation == "3":
    num = input("Enter your equation:")
    print(eval(num))

if equation == "4":
    num = input("Enter your equation:")
    print(eval(num))

if equation == "5":
    num = input("Enter your equation:")
    print(eval(num))

if equation == "6":
    num = input("Enter your equation:")
    print(eval(num))

if equation == "7":
    num = input("Enter your equation:")
    print(eval(num))

slow_print("\nThank you for using the Basic Calculator.\n")
slow_print("Goodbye.\n")