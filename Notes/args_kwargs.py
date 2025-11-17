# TE 2nd *args and **kwargs
"""def hello(name="honor", age=13):
    return f"Hello {name}. You are {age} years old."
print(hello())#Goes to default values, but can take new info.
print(hello("True",15))#Positional Arugment"""

def hello(last, *names):#Last is first to it goes first on the function call parameters
    for name in names:
        print(f"Hello {name} {last}")#Last has to be the first argument in the list to be assigned to all the names

hello("Harmer","Jaxon", "Jadyn", "Jace", "Lindsey","Emery", "Riley", "Freya")#Start with positional arguments and endwith keyword arguments.
# Tuple is a list that can't be changed

def stats(health = 10, attack = 10):
    print(f"Your stats are: Attack: {attack}, Health: {health}")

print(stats())
print(stats(11,11))