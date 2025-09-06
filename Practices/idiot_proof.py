# TE 2nd Idiot Proof

import string
import re
import time
import sys

def slow_print(text, delay=0.050):
       for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

slow_print("Student Information Formatter")
print("")
print("")
slow_print("This is idiot proof.")

name = input("What is your name: ").title().split()
phone_number = input("What is your phone number: ").isdigit()
cleaned = phone_number.replace("(", "").replace(")", "").replace("-", "").replace(" ", "")
gpa = input("What is your GPA: ")