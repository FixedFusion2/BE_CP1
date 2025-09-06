# TE 2nd Idiot Proof

import time
def slow_print(text, delay=0.05):
    """Print text slowly, character by character"""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)

slow_print("Student Information Formatter Opened.")
print("")
print("")
slow_print("This is idiot proof.")
print("")
name = input('\nWhat is your name: ').strip().title()
print("")
gpa = round(float(input("What is your GPA: ")),1)
print("")
phone_number = input("What is your phone number: ")
phone_number = f"{phone_number[:3]} {phone_number[3:6]} {phone_number[6:]}"
print("")
slow_print("Your name is: "+name)
print("")
slow_print("Your GPA is: ",gpa)
print("")
slow_print("Your phone number is "+phone_number)