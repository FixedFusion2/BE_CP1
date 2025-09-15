# TE 2nd The Crew

import time
def slow_print(text, delay=0.025):

    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)

slow_print("\n The Crew Shares")
slow_print("\n You get to decide the shares of money among the crew members.\n")
slow_print("The crew earned a whole bunch of money on the last outing (an input in dollars), but the captain didn't have time to divvy it all up before release everyone to port. \nHe gave each member of the crew 500 dollars for the evening and then sat down with his first mate to properly divide the shares. (a share is an equal portion of treasure) \nThe captain of the crew gets 7 shares\nThe first mate gets 3 shares \nEach member of the crew then gets 1 share but the crew members have all already received $500.\n")

total_treasure = float(input("\nHow much money did the crew make (solid number, no commas)?: "))
crew_members = int(input("\nHow many crew members are there (not including the captain and first mate(solid number, no commas))?: "))
single_share = total_treasure / (10+crew_members)
captain_share = single_share * 7
first_mate_share = single_share * 3
crew_share = single_share - 500

print("\nThe toatl treasure is: $", total_treasure)
print("\n A single share is: $", single_share)
print('\nThere are', crew_members, 'crew members')
print('\nThe captain gets $', captain_share)
print('\nThe first mate gets $', first_mate_share)
print('\nEach crew member gets $', crew_share),"This does not include the $500 they already received."




