# TE 2nd Functions Notes

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

num = 0
def add(x,y):
    return x+y

while num < add(5,5):
    print("Duck")
    print(f"Results is")