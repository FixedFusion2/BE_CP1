# TE 2nd CAESAR CIPHER

#Function that lets you insert message, shift, or change the mode from encode to decode.

def cipher(text, shift, mode):
    result = ""
    #For loop to go through each character one by one
    for char in text: 
        if char.isupper():#Checks for uppercase
            base = ord("A")
            result += chr((ord(char)- base + shift)%26 + base)#Unicode, 65, wraping around the aplhabet
        elif char.islower():#Chekcs for lowercase
            base = ord("a")#Lower case a
            result += chr((ord(char)- base + shift)%26 + base)#Unicode, 65, modula for wraping around the alphabet
        else:
            result += char
    return result


print("\nCaesar Cipher Machine opened.")
choice = input(" \nType 'encode' to encrypt, type 'decode' to decrypt: ")#Inputs for user
message = input("\nEnter your message (only letter values): ")
shift = int(input("\nEnter how many letters do you want to shift: "))

if choice == 'decode':#For decoding
    shift = -shift
print(cipher(message , shift, choice)) 


    







