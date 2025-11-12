# TE 2nd Order Up
#Create a program that allows a user to order items off a menu. 
# Menu items need to be stored in a dictionary with their prices as the value. 
# Users need to be able to order a drink, a main course and two side dishes. 
# At the end the program needs to repeat back to the user their full order, and the total cost. 
import time
def slow_print(text, delay=0.1):
    """Print text slowly, character by character"""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)

def diner():
        menu = {"Drinks": {"Rootbeer": 2, "Sprite": 2, "Water": 0, "Coke": 2, "Dr. Pepper": 2}, 
                "Entree": {"Hamburger": 5, "Cheeseburger": 5, "Chicken Salad": 4, "Sandwich": 5}, 
                "Sidedishes": {"Rosemary Fries": 3, "Chips": 2, "Fruit Cup": 3}}

        print("\nMenu:\n")
        print("Entrees: Hamburger: $5, Cheeseburger: $5, Chicken Salad: $4, Sandwich $5\n")
        print("Sidedishes: Rosemary Fries: $3, Chips: $2, Fruit Cup: $3\n")
        print("Drinks: Rootbeer: $2, Sprite: $2, Water: Free, Coke: $2, Dr. Pepper $2\n")

        entree = input("Choose your entree (Type: Hamburger, Cheeseburger, Chicken Salad or Sandwich): ")
        sidedish1 = input("Choose one side dish (Type: Rosemary Fries, Chips, or Fruit Cup): ")
        sidedish2 = input("Choose another sidedish: ")
        drink = input("Choose a drink (Type: Rootbeer, Sprite, Water, Coke, or Dr. Pepper): ")

        print(f"The cost of the Entree is {menu["Entree"][entree]} Dollars")
        print(f"The cost of the First Dish is {menu["Sidedishes"][sidedish1]} Dollars")
        print(f"The cost of the Second Dish is {menu["Sidedishes"][sidedish2]} Dollars")
        print(f"The cost of the Drink is {menu["Drinks"][drink]} Dollars")

        print(f" {menu["Entree"][entree]} + {menu["Sidedishes"][sidedish1]} + {menu["Sidedishes"][sidedish2]} + {menu["Drinks"][drink]} =  {menu["Entree"][entree] + menu["Sidedishes"][sidedish1] + menu["Sidedishes"][sidedish2] + menu["Drinks"][drink]} Dollars")

        tip = int(input("Would you like to add a $0, $1, $5 tip? (Type 0, 1, 5, 10, 10000): "))

        if tip == 0:
                print(f"Your total is {menu["Sidedishes"][sidedish2]} + {menu["Drinks"][drink]} =  {menu["Entree"][entree] + menu["Sidedishes"][sidedish1] + menu["Sidedishes"][sidedish2] + menu["Drinks"][drink]+tip}")
                slow_print("You didn't give me a tip, my family will starve this winter.")
        elif tip == 1:
                print(f"Your total is {menu["Sidedishes"][sidedish2]} + {menu["Drinks"][drink]} =  {menu["Entree"][entree] + menu["Sidedishes"][sidedish1] + menu["Sidedishes"][sidedish2] + menu["Drinks"][drink]+tip}")
                print("Thanks for the tip!")
        elif tip == 5:
                print(f"Your total is {menu["Sidedishes"][sidedish2]} + {menu["Drinks"][drink]} =  {menu["Entree"][entree] + menu["Sidedishes"][sidedish1] + menu["Sidedishes"][sidedish2] + menu["Drinks"][drink]+tip}")
                slow_print("Thank you so much!")

        elif tip == 10:
                print(f"Your total is {menu["Sidedishes"][sidedish2]} + {menu["Drinks"][drink]} =  {menu["Entree"][entree] + menu["Sidedishes"][sidedish1] + menu["Sidedishes"][sidedish2] + menu["Drinks"][drink]+tip}")
                print("Thank you so much, this is great!")

        elif tip == 10000:
                print(f"Your total is {menu["Sidedishes"][sidedish2]} + {menu["Drinks"][drink]} =  {menu["Entree"][entree] + menu["Sidedishes"][sidedish1] + menu["Sidedishes"][sidedish2] + menu["Drinks"][drink]+tip}")
                slow_print("H-How? W-WWHAT? THANK YOU, THANK YOU. MY FAMILY WON'T STARVE AT ALL THIS WINTER. You see my wife has cancer and one of my children has the flu, now I'll be able to afford 1/10 of the medical bills! THANK YOU SO MUCH!")
        else:
                print("I didn't understand what you said.")

slow_print("Welcome to Aunt Rosey's Diner!")
buy = input("Would you like to order? (type yes or no): ")
if buy == "yes":
      diner()
if buy == "no":
       print("Okay thats fine.")
       exit()