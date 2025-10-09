import time
def slow_print(text, delay=0.05):
    """Print text slowly, character by character"""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)

slow_print("You wake up in an empty chamber...")
action_1 = input("There is a torch (option 1), a thick stick (option2), and a ")