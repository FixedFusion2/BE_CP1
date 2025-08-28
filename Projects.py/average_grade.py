# TE 2nd Grade Average
import time
import sys

def slow_print(text, delay=0.1):
       for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

print("")
slow_print("Hello")
print("")
slow_print("I'm going to ask you for your grade average.")
print("")
class_1 = float(input("Grade for your first class: "))
class_2 = float(input("Grade for your second class: "))
class_3 = float(input("Grade for your third class: "))
class_4 = float(input("Grade for your fourth class: "))
class_5 = float(input("Grade for your fifth class: "))
class_6 = float(input("Grade for your sixth class: "))
class_7 = float(input("Grade for your seventh class: "))
print("")
numbers = (class_1+class_2+class_3+class_4+class_5+class_6+class_7)
average = numbers/7
print("Your average grade is:", round(average,2))
print("")