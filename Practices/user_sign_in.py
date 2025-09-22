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

slow_print("Enter username and password to the database.")
print("")
correct_username = "@username1"
correct_password = "p@ssword2"
username = input("Enter a username: ")
password = input("Enter a password: ")

if username == correct_username:
    slow_print('Correct Username ')
    
    if password == correct_password:
        slow_print('and Correct password, welcome to the database.')
    
    else:
        slow_print('Wrong username or password.')

else:
    slow_print("Wrong username or password.")