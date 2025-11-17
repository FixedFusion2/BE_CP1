# TE 2nd What is My Grade?

import time
def slow_print(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)



slow_print("Grade Pertage Formatter Opened.")
print("")
grade = float(input("Enter your grade percent(no percent symbol): "))


if grade > 100:
    slow_print("You are an overachiever.")
elif grade > 93 and grade < 101:
    print("You have an A")
elif grade >= 91:
    print("You have a B+")
elif grade == 90:
    print("You have a B")
elif grade < 90 and grade >=80:
    print("You have a B-")
elif grade < 76 and grade > 70:
    print("You have a C+")
elif grade == 70:
    print("You have a C")
elif grade < 70 and grade > 65:
    print("You have a C-")
elif grade > 60 and grade < 64:
    print("You have a D+")
elif grade > 55 and grade < 51:
    print("You have a D")
elif grade == 50:
    print("You have a D-")
elif grade < 50 and grade > 45:
    print("You have an F")
elif grade <= 44:
    slow_print("How? HOW? how...*sigh*...")
else:
    print("Numeric values only, ya nimrod.")