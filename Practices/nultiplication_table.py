# TE 2nd Multiplication Table

nums = int(input('Please enter a positive integer between 1 an 30: '))
for row in range(1, nums + 1):
    for col in range(1, nums + 1):
        print(row * col, end = "\t")
    print()
