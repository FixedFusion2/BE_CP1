# TE 2nd Who_are_you?
import time
import sys

def slow_print(text, delay=0.1):
       for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

time.sleep(1)
slow_print("Hello")
print("")
time.sleep(1)
name = input("What is your name: ")
time.sleep(1)
age = input("How old are you: ")
time.sleep(1)
color = input("What is your favorite color: ")
time.sleep(1)


print("Your name is",name, ", you are", age, ", your favorite color is", color,".")
print("")