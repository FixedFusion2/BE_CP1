# TE 2nd While Loops Notes
import time
import random
# for loop
num = 1
break_point = random.randint(1,30)
#for num in range(1,12):# After the "num in" the range (1,2) is the the end/break condition
    #print(num)


#while num <= 20:# End/break conditions
    #print(num)
    #num+=1

# For loops have a definite iterations, for loops have range.
# While loops have indefinite iteration (usually you will end it eventually).
# While loops don't have a built in stop.
# While loops have a defined iteratio annd an increase iterator.
print("")

#Infinite loops (Don't usually do this)

while num <= 20:
    print(num)
    time.sleep(0.25)
    if num == break_point:
        break#Fixed loop
    num += 1 #fixed loop
else:#Else will only happen if we end the loop by meeting a condition 
    #not reaching 20 from break_point
    print("The loop exited by meeting a condition.")

print("The loop is over!")

count = 0  # Initialize the counter

while count <= 30:
    print(count)
    count += 2  # Increment the counter by 2 in each iteration

count_1 = 0
while count_1 <= 10:
    print(count_1)
    count_1+=1