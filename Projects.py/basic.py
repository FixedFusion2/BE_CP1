import time
def slow_print(text, delay=0.05):
    """Print text slowly, character by character"""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)

slow_print("You wake up in an empty chamber...")
action_1 = input("\nThere is a torch (type TORCH), a tree branch (BRANCH), and a rusty sword (BADSWORD), what do you choose?: \n")
if action_1 == "BADSWORD":
    slow_print("You chose the rusty sword.")
elif action_1 == "BRANCH":
    slow_print("You chose the thick stick.")
elif action_1 == "TORCH":
    slow_print("You chose the torch.")


