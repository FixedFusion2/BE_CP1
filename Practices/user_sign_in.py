# TE 2nd User Sign In

#Instructions:

# Write a program that asks a user for their username and their. 
# If the username and the password match the ones given in the program 
# it welcomes the user to the program. 
# Otherwise it tells the user that their login credentials were invalid. 

import time
def slow_print(text, delay=0.05):
    """Print text slowly, character by character"""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)

slow_print("Welcome to the database.")
print("")

username = input("Enter a username: ")
password = input("Enter a password: ")