# TE 2nd The Crew

import time
def slow_print(text, delay=0.025):

    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)

slow_print("\n The Crew Shares")
slow_print("\n You get to decide the shares of money among the crew members.\n")
slow_print("The crew earned a whole bunch of money on the last outing (an input in dollars), but the captain didn't have time to divvy it all up before release everyone to port. \nHe gave each member of the crew 500 dollars for the evening and then sat down with his first mate to properly divide the shares.  \nThe captain of the crew gets 7 shares\n (equal portions of the treasure) \nThe first mate gets 3 shares \nEach member of the crew then gets 1 share but the crew members have all already received $500.")

total_treasure = float(input("\nHow much money did the crew make on the last outing? (in dollars): "))
crew_members = int(input("How many crew members are there (not including the captain and first mate)?: "))
total_shares = 7 + 3 + crew_members
share_value = total_treasure / total_shares

