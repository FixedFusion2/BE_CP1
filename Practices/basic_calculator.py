# TE 2nd Basic Calculator

import time
def slow_print(text, delay=0.025):

    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)

print("\nBasic Calculator Opened.\n")
print("This calculator can add, subtract, mulityply, divide, integer divide, modulo, and raise numbers.\n")

print("Operations: (+, -, *, /, //, %, **)\n")

equation = print("\n Press 1 to add (+).\n Press 2 to subtract (-).\n Press 3 to multiply (*).\n Press 4 to divide (/).\n Press 5 to integer divide (//).\n Press 6 to modulo (%).\n Press 7 to raise (**). ")

if equation == "1":
    num = input("Enter the first number you want add:")
    num_2 = input("Enter the second number you want to add:")
    result = float(num) + float(num_2)
    slow_print("The answer is " + str(result) + ".\n")

