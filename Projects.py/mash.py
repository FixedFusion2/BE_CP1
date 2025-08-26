import random

import time

import sys

def slow_print(text, delay=0.1):
       for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

#The random import, imports a library that makes it so you can do certain things that make stuff random.
slow_print("")
print("(If you dont know know how mash works, then get out.)")
print("")
slow_print("Welcome To MASH!")
#All these prints are instructions.
slow_print(" There are some prebuilt options including the Mansion, Apartment, Shack, House. (MASH)")
slow_print(" There are also some bad options placed in there....")
#Making some variables here that make mash possible.
spouse = ["A Witch", "ME", "A Homeless Man"]
numberofchildren = ["12", "50"]
car = ["Bicycle", "Cyber Truck"]
job = ["Grave Digger", "School Janitor", "Homeless Man", "Chat GBT"]
home = ["Mansion", "Apartment", "Shack", "House"]
#These lines of code give the amount of times you have to input a spouse, number of children, car, and job.
for x in range(0, 5):
  choice = input("Now, Enter a spouse: ")
  spouse.append(choice)
for x in range(0, 5):
  choice = input("Enter a number of children you'd like: ")
  numberofchildren.append(choice)
for x in range (0, 5):
  choice = input("Enter a car: ")
  car.append(choice)
for x in range (0, 5):
  choice = input("Enter a job: ")
  job.append(choice)
#These lines of code output the mash options and print them out.
slow_print(" You will mary ")
slow_print(random.choice(spouse))
slow_print(" The number of children you will have is ")
slow_print(random.choice(numberofchildren))
slow_print(" The car you will drive is ")
slow_print(random.choice(car))
slow_print(" The job you get is ")
slow_print(random.choice(job))
slow_print(" You will live in a ")
slow_print(random.choice(home))