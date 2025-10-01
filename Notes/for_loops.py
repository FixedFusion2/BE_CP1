# TE 2nd For Loops
import time
nums = [6,51,1,94,351,946,5489,4,654,684]

# num is the current instance of the loop
# nums completes the loop for every item in the list
# The a for loop lets you do the exact same thing to every item in a group or list.
for num in nums:
    print(nums)

# To iterate, is to repeat
# An iterator is something that is keeping track of what is repeating.
# An iteration is one instance of a loop
#Range is a built in  function that is going to return a list.
for x in range(1,10):
    print(x)
time.sleep(3)
print("Count by twos below: ")
for x in range(2,11,2):# This 2 at teh end will have it count by 2's.
    print(x)
time.sleep(3)
print("Count down")
for x in range(10,0,-1):#Count by negative 1 has it go backwards
    print(x)
time.sleep(3)
#Range is not incluse so it won't include 10 at the end of the print statements