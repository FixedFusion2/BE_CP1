# TE 2nd Basic Calculator

import time
def slow_print(text, delay=0.025):

    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)

print("\nBasic Calculator Opened.\n")
print("This calculator can add, subtract, mulityply, divide, integer divide, modulo, and raise numbers.\n")

print("Operations: (+, -, *, /, //, %, **)\n")

num1 = float(input("Enter your first number: "))
num2 = float(input("Enter your second number: "))       
print("\nSelect an operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")
print("5. Integer Division (//)")
print("6. Modulo (%)")
print("7. Exponents (**)")
        
equation = input("\nEnter your operation (1-7): ")

if equation == "1":
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif equation == "2":
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif equation == "3":
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif equation == "4":
    result = num1 / num2
    print(f"{num1} / {num2} = {result}")
elif equation == "5":
    result = num1 // num2
    print(f"{num1} // {num2} = {result}")
elif equation == "6":
    result = num1 % num2
    print(f"{num1} % {num2} = {result}")
elif equation == "7":
    result = num1 ** num2
    print(f"{num1} ** {num2} = {result}")