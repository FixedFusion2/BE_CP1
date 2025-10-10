# TE 2nd Password Strength Checker

#print statements that explain the password strength checker
print("\nYour password must include the following:")
print("\nAt least 8 characters long")
print("\nContains at least one uppercase letter")
print("\nContains at least one lowercase letter")
print("\nContains at least one number")
print("\nContains at least one special character (!@#$%^&*()_+-=[]{}|;:,.<>?)\n")
#password variable input
password = input("Create your password: ")
#Variable for the points to dettermine how strong their password is.
points = int()
#Loops this peice of code if they want to keep checking their password strength or exit.

    #If statement to check the length, if the length is greater than 8 give one point.
    #If less than 8 points don't add a point.
if len(password) >=8:
    points = +1

    #If statement to check for upper case letters if it has uppercase letter give 1 point,
    #If no  uppercase letters, don't add a point.
elif password.isupper:
    points = +1
    #If statement to aslo check for lower case letters if it has lowercases letters give 1 point,
    #If no lowercase letters, don't add a point.
elif password.islower:
    points = +1
    #If statement to check for numbers if it has numbers, give one point.
    #If it doesn't have a number, don't add a point.
elif password.isdigit:
    points = +1
    #If statement to check for special characters  if there are special characters, add one point.
    #If it doesn't have a special character, don't add a point
elif "("or"!"or"@"or"#"or"$"or"%"or"^"or"&"or"*"or"("or")"or"_"or"+"or"-"or"="or"["or"]"or"}"or"|"or";"or","or"."or"<"or">"or"?":
    points = +1
    #If statement to check if points is 5, if it is, then say: "Very Strong Password"
elif points == 5:
    print("Your password is very strong.")
    #If statement to check if points is 4, if it is, then say: "Strong Password"
elif points == 4:
    print("Your password is strong.")
    #If statement to check if points is 3, if it is, then say: "Moderate Password"
elif points == 3:
    print("Your password is moderate.")
    #If statement to check if points is 2, if it is, then say: "Weak Password"
elif points == 2:
    print("Your password is weak.")
    #If statement to check if points is 1, if it is, then say: "Feable Password"
elif points == 1:
    print("Your password is feable.")
    #If statement to check if points is 0, if it is, then say: "BAD Password"
elif points == 0:
    print("Your password is BAD.")