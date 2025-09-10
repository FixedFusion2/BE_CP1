# TE 2nd Ramdon Numbers
import random

#Example of random numbers
print(random.random()) #Random float 0.0 to 1.0
print(random.randint(1, 10)) #Random integer between 1 and 10
print(random.uniform(1.5, 10.5)) #Random float between 1.5 and 10.5


#Example of random choices
print(random.choice(['apple', 'banana', 'cherry'])) #Random choice from a list
print(random.choice(range(1, 100))) #Random choice from a range
print(random.choices(range(1, 100), k=5)) #Random sample of


#Example of random samples
print(random.sample(range(1, 100), 5)) #Random sample of 5 unique numbers from a range
print(random.sample(['apple', 'banana', 'cherry', 'date', 'fig', 'grape'], 3)) #Random sample of 3 unique fruits from a list


#Example of random shuffle
print(random.shuffle([1, 2, 3, 4, 5])) #Randomly shuffle a list 5 numbers from a range
print(random.shuffle(['apple', 'banana', 'cherry', 'date', 'fig', 'grape'])) #Randomly shuffle a list of fruits

# A method is similar to a function, but it is associated with an object.
# A method is called on an object, and it can access the object's data and modify it
# A function is a standalone piece of code that can be called with arguments and returns a value.

state_one = random.randint(1,10)+random.randint(1,10)
state_two = random.randint(1,10)+random.randint(1,10)
state_three = random.randint(1,10)+random.randint(1,10)

print(f"Your stat optitions are: {state_one} Strength, {state_two} Dexterity, and {state_three} Stealth")

# An argument is a value that is passed to a function or method when it is called.
# An argument can be a variable, a literal, or an expression.
# An argument is used to provide input to a function or method, and it can be used to customize its behavior.
# A parameter is a variable that is defined in a function or method definition.
# A parameter is used to define the input that a function or method can accept.
# A parameter is a placeholder for an argument that will be passed to the function or method when it is called.
# A parameter can have a default value, which is used if no argument is provided when the function or method is called.
# A parameter can also be optional, which means that it can be omitted when the function or method is called.

# The arguments for the randint method are the minimum and maximum values for the random integer.