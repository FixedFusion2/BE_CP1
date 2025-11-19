# TE 2nd Flexible Calculator

#Function fo calculation
# uses *args to accept any number of values (numbers). The function should also accept an optional parameter for the operation to be performed.
def calculate(*args, operation = "sum"):#Parameters for args and operation.
#If statement for operation being set to sum
    if operation == "sum":
        print(sum(args))
        #If statement for operation being set to average 
    elif operation == "average":
        print(sum(args)/len(args))
        #If statement for operation being set to max 
    elif operation == "max":
        print(max(args))
        #If statement for operation being set to min
    elif operation == "min":
        print(min(args))
        #If statement for operation being set to product
    elif operation == "product":
        product = 1
        for num in args:
            product *= num
        print(product)


#While True to keep calculating
while True:

    #Number list to hold number values from user input
    numbers_list = []
    #Welcome to the Flexible Calculator!
    print("Welcome to Flexible Calculator")
    #Available operations: sum, average, max, min, product
    print("Availabe Operations: sum, average, max, min, product")
    #Which operation would you like to perform?
    operation = input("What operation would you like to perform: ")
    #While loop for numbers 
    while True:
        num_entry = input("Enter your numbers (type done when finished.): ")
        if num_entry == "done":#If the user types "done" break the loop
            break
        numbers_list.append(float(num_entry))

    #Call function
    calculate(*numbers_list, operation=operation)
    #Let the user decide if they want to keep calculating or not.
    again = input("Would you like to keep calculating? (Type yes or no): ")
    if again == "no":
        print("Thanks for using the calculator.")
        break


