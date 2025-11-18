# TE 2nd Flexible Calculator

#Function fo calculation
# uses *args to accept any number of values (numbers). The function should also accept an optional parameter for the operation to be performed.
def calculate():
#If statement for operation being set to sum
    if operation == "sum":
        print(sum(numbers))
        #If statement for operation being set to average 
    if operation == "average":
        print(sum(numbers)/len(numbers))
        #If statement for operation being set to max 
    if operation == "max":
        print(max(numbers))
        #If statement for operation being set to min
    if operation == "min":
        print(min(numbers))
        #If statement for operation being set to product
    if operation == "product":
        print(numbers * numbers)


#Welcome to the Flexible Calculator!
print("Welcome to Flexible Calculator")
#Available operations: sum, average, max, min, product
print("Availabe Operations: sum, average, max, min, product")
#Which operation would you like to perform?
operation = input("What operation would you like to perform: ")
#While loop for numbers 
while True:
    numbers = str(input("Enter your numbers (type done when finished): "))
    if numbers == "done":#If the user types "done" break the loop
        break
calculate()

