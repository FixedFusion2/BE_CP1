# TE 2nd Squared Numbers

#Use the mapping function to iterate over a list of numbers and return their squared values. Print the original number with its squared value for the user to see.
#Note: You can use this list or make your own list of numbers but your list should have at least 20 items in it.

numbers = [3, 7, 12, 25, 30, 45, 50, 65, 70, 85, 90, 105, 110, 125, 130, 145, 150, 165, 170, 185, 190, 205, 210, 225, 230, 245, 250, 265, 270, 285]#Numbers list

squared = list(map(lambda num: num**2, numbers))#Squared variable with lambda function.

print(f"Original: {numbers[0]}, Squared: {squared[0]}")#Print 1
print(f"Original: {numbers[1]}, Squared: {squared[1]}")#Print 2
print(f"Original: {numbers[2]}, Squared: {squared[2]}")#Print 3
print(f"Original: {numbers[3]}, Squared: {squared[3]}")#Print 4
print(f"Original: {numbers[4]}, Squared: {squared[4]}")#Print 5
print(f"Original: {numbers[5]}, Squared: {squared[5]}")# Print 6
print(f"Original: {numbers[6]}, Squared: {squared[6]}")# Print 7
print(f"Original: {numbers[7]}, Squared: {squared[7]}")# print 8
print(f"Original: {numbers[8]}, Squared: {squared[8]}")#Print 9
print(f"Original: {numbers[9]}, Squared: {squared[9]}")# print 10
print(f"Original: {numbers[10]}, Squared: {squared[10]}")# Print 11
print(f"Original: {numbers[11]}, Squared: {squared[11]}")# Print 12
print(f"Original: {numbers[12]}, Squared: {squared[12]}")# print 13
print(f"Original: {numbers[13]}, Squared: {squared[13]}")# print 14
print(f"Original: {numbers[14]}, Squared: {squared[14]}") # Print 15
print(f"Original: {numbers[15]}, Squared: {squared[15]}")# print 16
print(f"Original: {numbers[16]}, Squared: {squared[16]}")# print 17
print(f"Original: {numbers[17]}, Squared: {squared[17]}")# print 18
print(f"Original: {numbers[18]}, Squared: {squared[18]}")# Print 19
print(f"Original: {numbers[19]}, Squared: {squared[19]}")# Print 20