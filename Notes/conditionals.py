# TE 2nd Conitionals
import random 
import time

num = float(input("Enter a number: "))

#If the number is above zero its true, puttign out the statement. 
if num > 0:
    print(f"The number {num} is positive.")
#If the number is below zero its false, putting out a different statement.
elif num < 0:
    print(f"The number is {num} is negative.")
#If the number is zero its false, putting out another different statement.
else:
    print(f"The number {num} is zero.")

print("\n\n")
print("Time to roll!")
time.sleep(1)
number  = random.randint(1,20)
if number == 20:
    print(f"You got the highest number possible! (You rolled a {number})")
elif number > 10:
    print(f"You succeed! (You rolled a {number})")
elif number <= 10:
    print(f"You missed. (You rolled a {number})")
else:
    print(f"That shouldn't be possible. (You rolled a {number})")

statement = False
statement_2 = True