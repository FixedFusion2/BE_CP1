# TE 2nd Order Up
#Create a program that allows a user to order items off a menu. 
# Menu items need to be stored in a dictionary with their prices as the value. 
# Users need to be able to order a drink, a main course and two side dishes. 
# At the end the program needs to repeat back to the user their full order, and the total cost. 

menu = {"Drinks": {"Rootbeer": 2, "Sprite": 2, "Water": 0, "Coke": 2, "Dr. Pepper": 2}, 
        "Entree": {"Hamburger": 5, "Cheeseburger": 5, "Chicken Salad": 4, "Sandwich": 5}, 
        "Sidedishes": {"Rosemary Fries": 3, "Chips": 2, "Fruit Cup": 3}}

print("Welcome to Aunt Rosey's Diner!")

print("\nMenu:\n")
print("Entrees: Hamburger: $5, Cheeseburger: $5, Chicken Salad: $4, Sandwich $5\n")
print("Sidedishes: Rosemary Fries: $3, Chips: $2, Fruit Cup: $3\n")
print("Drinks: Rootbeer: $2, Sprite: $2, Water: Free, Coke: $2, Dr. Pepper $2\n")

entree = input("Choose your entree (Type: Hamburger, Cheeseburger, Chicken Salad or Sandwhich): ")
sidedish1 = input("Choose one side dish (Type: Rosemary Fries, Chips, or Fruit Cup): ")
sidedish2 = input("Choose another sidedish: ")
drink = input("Choose a drink (Type: Rootbeer, Sprite, Water, Coke, or Dr. Pepper): ")

print(f"The cost of the Entree is {menu["Entree"][entree]} Dollars")
print(f"The cost of the First Dish is {menu["Sidedishes"][sidedish1]} Dollars")
print(f"The cost of the Second Dish is {menu["Sidedishes"][sidedish2]} Dollars")
print(f"The cost of the Drink is {menu["Drinks"][drink]} Dollars")

print(f" {menu["Entree"][entree]} + {menu["Sidedishes"][sidedish1]} + {menu["Sidedishes"][sidedish2]} + {menu["Drinks"][drink]} = ")