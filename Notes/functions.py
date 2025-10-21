# TE 2nd Functions Notes
# Imported libraries
# set global variables
#Global variables can be read anywhere
#Local varibales can omnly be used in a fucntion.
num = 0
player_hp = 100
monster_hp = 100


#Write your function
def attack(dmg):
    return player_hp - dmg



#Write the rest of your code
print(f"You have been attacked! Your hp is now {attack(15)}")
def fun():#Define your function with def and then name your function and add parenthesis
    print("Hewwo")#Put what you want inside of your function
    print("DIS IS FWUN")

fun()#Call your function by stating the name and placing the parenthesis, this is how you now its a function

#Functions are helpful for repetition
fun()
fun()
fun()
#Functions are modular meaning they are reusable
#Abstratcing something means making it more general instead of specific.
#Functions are abstract
def add(x,y):
    print(f"{x} + {y} = {x+y}")

add(5,5)


#A return statement is used within a function to send a value back to the part of the code that called the function.
#Return statements can be used to exit a file or send a value back to the function.

#num = 0
#def add(x,y):
    #return x+y

#while num < add(5,5):
    #print("Duck")
    #print(f"Results is")
    


