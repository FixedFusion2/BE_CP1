# TE 2nd Squared Numbers

#Use the mapping function to iterate over a list of numbers and return their squared values. Print the original number with its squared value for the user to see.
#Note: You can use this list or make your own list of numbers but your list should have at least 20 items in it.

numbers = [3, 7, 12, 25, 30, 45, 50, 65, 70, 85, 90, 105, 110, 125, 130, 145, 150, 165, 170, 185, 190, 205, 210, 225, 230, 245, 250, 265, 270, 285]#Numbers list

squared = list(map(lambda num: num**2, numbers))#Squared variable with lambda function.
for i in range(20):
    print(f"Original: {numbers[i]}, Squared: {squared[i]}")#Prints 1-20.
