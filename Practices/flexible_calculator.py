# TE 2nd Flexible Calculator

#Function fo calculation
# uses *args to accept any number of values. Operation for operation.
def calculate(*args, operation = "sum"):#Parameters for args and operation.
#If statement for operation being set to sum
    if operation == "sum":
        print(sum(args))#Showing the output
        #If statement for operation being set to average 
    elif operation == "average":
        print(sum(args)/len(args))#Showing the output
        #If statement for operation being set to max 
    elif operation == "max":
        print(max(args))#Showing the output
        #If statement for operation being set to min
    elif operation == "min":
        print(min(args))#Showing the output
        #If statement for operation being set to product
    elif operation == "product":
        product = 1#variable for product to start
        for num in args:
            product *= num
        print(product)#Showing the output


#While True to keep calculating
while True:

    #Number list to hold number values from user input
    numbers_list = []
    #Welcome to the Flexible Calculator!
    print("Welcome to Flexible Calculator.")
    #Available operations: sum, average, max, min, product
    print("Availabe Operations: sum, average, max, min, product.")
    #Which operation would you like to perform?
    operation = input("What operation would you like to perform: ")
    #While loop for numbers 
    while True:
        numbers = input("Enter your numbers (type done when finished): ")
        if numbers == "done":#If the user types "done" break the loop
            break
        numbers_list.append(float(numbers))

    #Call function
    calculate(*numbers_list, operation=operation)
    #Let the user decide if they want to keep calculating or not.
    again = input("Would you like to keep calculating? (Type yes or no): ")#Again variable for checking if they want to keep calculating.
    if again == "no":#If no break while loop
        print("Thanks for using the calculator.")#Showing the output
        break


