# TE 2nd Idiot Proof

import time
import sys

def phone_format(n):
     return format(int(n[:-1]), ",").replace(",", "-") + n[-1] 


def slow_print(text, delay=0.050):
       for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

print("")
slow_print("This program is idiot proof. ")
print("")
name = input("Enter your name: ").strip().title()
phone_number = input("Enter your phone number: ")
gpa = round(float(input("Enter your GPA: ").strip()),2)
print("")
print("Thank you for entering your information.")

print("Your name is " +name+ ".")
phone_format(print("Your phone number is" +phone_number+ "."))
print("Your GPA is "+str(gpa)+"")
print("")