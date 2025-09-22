# TE 2nd What is My Grade?

import time
def slow_print(text, delay=0.05):
    """Print text slowly, character by character"""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)



slow_print("Grade Pertage Formatter Opened.")
print("")
grade = float(input("Enter your grade percent(no percent symbol): "))


if grade >= 100:
    slow_print("You are an overachiever.")
elif grade >= 93:
    print("You have an A")
elif grade >= 90:
    print("You have a B+")
elif grade == 90:
    print("You have a B")
elif grade <=90:
    print("You have a B-")
elif grade >=70:
    print("You have a C+")
elif grade == 70:
    print("You have a C")
elif grade <=70:
    print("You have a C-")
elif grade >= 60:
    print("You have a D+")
elif grade == 60:
    print("You have a D")
elif grade >= 60:
    print("You have a D-")
elif grade >= 50:
    print("You have an F+")
elif grade == 50:
    print("You have an F")
elif grade <= 50:
    slow_print("How? HOW? how...*sigh*...")