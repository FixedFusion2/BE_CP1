# TE 2nd Factorial Calculator

#Define function getting INP
def getting_INP(user_input):
    try:
        num =float(user_input)
    except:
    #If INP can't be turned into float, return False
        return False
    #If float INP-integers INP is not equal to 0, return Flase
    if num - int(num) != 0:
        return False
    
    #If the integers is less than 0, return false
    if int(num) < 0:
        return False
    #Else return True
    return True
#Def function factorial getting NUM
def factorial_getting_NUM(num):
    #Set DON to 1
    done = 1
    #Loop over list stating with NUM, counting down by on 1
    for i in range(num, 0, -1):
        #Set DON to DON multiplied by list item(current),
        done = done * i
    #Return DON
    return done
#Set IN to user input of "What number would you like to factorial?"
factorial = input("What number would you like to factorial: ")
#Loop while function check on IN is FALSE
while getting_INP(factorial) == False:
    #Display invalid user input
    print("Invalid User Input")
    #Set IN to user input of "What number would you like to factorial?"
    factorial = input("What number would you like to factorial: ")
#display factorial is equal to integers
factorial = int(factorial)

#Display result
print(f"{factorial}! is equal to {factorial_getting_NUM(factorial)} ")
