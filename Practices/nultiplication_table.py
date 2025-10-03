# TE 2nd Multiplication Table
import time
def slow_print(text, delay=0.05):
    """Print text slowly, character by character"""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)


slow_print("\nMultiplication Table Opened\n")
nums = int(input('Please enter a positive integer between 1 an 30: '))
for row in range(1, nums + 1):
    for col in range(1, nums + 1):
        print(row * col, end = "\t")
    print()
