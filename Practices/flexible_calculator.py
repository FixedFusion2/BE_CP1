# TE 2nd Flexible Calculator
#Welcome to the Flexible Calculator!
print("Welcome to Flexible Calculator")
#Available operations: sum, average, max, min, product
print("Availabe Operations: sum, average, max, min, product")
#Which operation would you like to perform?
operation = input("What operation would you like to perform: ")
while True:
    numbers = input("Enter your numbers (type done when finished): ")
    if numbers == "done":
        break
if operation == "sum":