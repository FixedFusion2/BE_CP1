# TE 2nd Mapping

numbers = [12,3,2143,34,32,45,43,54,6,7]
"""divided = []

for num in numbers: 
    divided.append(num/2)"""

"""def divide(number):
    return number/2
"""

divided = list(map(lambda num: num/2, numbers))

print(divided)

"""for i, num in enumerate(numbers):
    print(f"{num} divided by 2 is {divided[i]}.")"""