# FL class Shopping List Manager
import time
def slow_print(text, delay=0.05):
    """Print text slowly, character by character"""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)

slow_print("\nShopping list mananger opened.\n")
#Put your shopping list variable here
shopping_list = []


while True:
    print("\nPress 1 to add an item. \nPress 2 to remove an item. \nPress 3 to look at your items. \nPress 4 to exit the program.\n(Whole numeric only accepted.)\n")
    action = int(input("\nChoose an option (1-4): "))

    if action == 1:
        item = input("Add an item to the shopping list: ")
        shopping_list.append(item)
        slow_print(f"{item} added.")
    elif action == 2:
        item = input("Remove an item from the shopping list: ")
        if item in shopping_list:
            shopping_list.remove(item)
            slow_print(f"{item} removed.")
        else:
            slow_print("That item isn't in the shopping list.")
    elif action == 3:
        print(shopping_list)

    elif action == 4:
        slow_print("Goodbye!")
        break
    else:
        slow_print(f"\n{action} is not a valid action.\n")