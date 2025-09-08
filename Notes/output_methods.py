# TE 2nd Formatted Output Methods

name = "Jake"
age = 21
grade = .75
money = 2500

print("\nHello {}, you are {:,} years old, that is really old! You have a {:%} in this class. You have ${:.2f} that is a lot of money\n".format(name, age, grade, money))# :,.2f = comma and 2 decimal places
# :% = percentage
# :, = comma
# :.2f = 2 decimal places
# :d = integer
# :s = string
# :f = float
# :c = character
# :e = scientific notation
# :b = binary
# The format method is outdated, use f-strings instead.
# An f-string is a string that is prefixed with the letter 'f' or 'F'.
# The f also means other things like format.
# To make an f-string, you put an 'f' or 'F' before the opening quotation mark of a string literal.
# Then you can use curly braces {} to evaluate variables and expressions inside the string.
# You can also use the same format specifiers as the format method inside the curly braces.`
# f-strings allow you to embed expressions inside string literals, using curly braces {}.
print(f"\nHello {name}, you are {age:b} years old in binary, that is really old! You have a {grade:%} in this class. You have ${money:.2f} that is a lot of money\n")