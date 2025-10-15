#Practice with functions

def room_1():
    print("You are in a room")
    print("This is the cool room")

def room_2():
    print("You are in another room")
    print("This is the lame room")


choice = input("You enter a big room do you go to the left or the right: ").lower()

if choice == "left":
    room_1()
elif choice == "right":
    room_2()
else:
    print("That is an invalid action.")