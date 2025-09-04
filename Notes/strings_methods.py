# TE 2nd Strings Methods Notes

#.strip() gets rid of any extra spaces before or after the string
#name = input("What is your name? ").strip().title()
#print("Hello " + name +", it is nice to meet you! ")
#.lower() makes its all lowercase
#.upper() makes its all uppercase
#.title() makes the first letter of each word uppercase
#.capitalize() makes the first letter of the first word uppercase
# You can chain methods together
#print("Hello " + name.strip().title() +", it is nice to meet you! ")
#A string can be anything is quotation marks
#You can use single or double quotes, but if you start with one you have to end with the same one
#print('Hello ' + name +", it is nice to meet you! ")

#.find() finds the first instance of a substring and returns the index
#.index() does the same thing but will give an error if it is not found
#.count() counts how many times a substring appears in a string
sentence = "The quick brown fox jumped over the lazy dog!"

word = "brown"

print(sentence.replace("fox", "cat"))

#Methods that allow me to change the content of a string
# .replace() replaces a substring with another substring
# .join() joins a list of strings together with a specified separator
# .split() splits a string into a list of substrings based on a specified separator
# .format() (while out-dated) allows you to insert variables into a string in a specific format
# Now .format can be simplified with f-strings
# f-strings (formatted string literals) allow you to embed expressions inside string literals, using curly braces {}

print(f"The word '{word}' starts at index {sentence.find(word)}")