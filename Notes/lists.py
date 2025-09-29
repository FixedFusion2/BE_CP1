# TE 2nd List Notes

# A list is a complex data type
my_family = ["Victor", "Jenedy", "True", "Honor", "Joy"]

random_names = ["Jackson,", "Albert", "Rosy", 3.15, 10, True]

print(random_names)

print(random_names[3]) #Starts at 0 so jackson = 0 and 3.15 = 3
print(len(random_names))

random_names[0] = ["Fredrick"]
print(random_names[0])
random_names.remove("Albert")
# List (changable, ordered)
# Tuple (not changable, ordered)
classes = ("Bard", "Monk", "Barbarian", "Paladin")
# Set (changable, not ordered)
fruit = {"Apple", "Orange", "Strawberry"}
print(fruit)
random_names.insert(2, "Amazing")