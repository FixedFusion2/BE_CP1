#We try to guess a word and slowly a drawing of someone getting hung appears if they are wrong
print("Welcome to Hangman!")
print("HOW TO PLAY:")
print("")
print("Try to guess a letter to the word if you get it wrong then the game adds a limb to the hangman and once the whole hangman is finished and fully drawn then he dies and you lose.")
print("")
print("To win you guess all the letters right without killing the hangman. Overall to win, save the hangman by guessing the letters right.")

#Slow print function
import time
def slow_print(text, delay=0.05):
    """Print text slowly, character by character"""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
#Libraries to import: random/time (for slow print function)
import random
import time
#Variable needed: Variable for the word selected, list of words, failed attempts, and guess letters
word = ""
wordlist = ["robot", "number", "true", "tunic", "dog", "baby", "answer", "false", "swimmer", "hunter", "hang", "man", "death", "evicted", "marked", "tarp", "fishy", "shark", "money", "billion", "funny", "twenty", "temple", "chicken", "wolf", "shimmer", "mother", "father", "ninja"]
failedAttempts = 0
letterguessed = []
displayWord = ""
play_again = ""
#function to restart pick random word and reset all variables back to the starting point
def restart():
  global word
  global wordlist
  global failedAttempts
  global letterguessed
  global play_again
  word = random.choice(wordlist)
  failedAttempts = 0
  letterguessed = []
  play_again = ""
  game()
#function hung a conditional that checks failed attempts to see how much of the gallows is drawn
def hung():
  if failedAttempts == 0:
    print("________\n|\n|\n|\n|__________")
  elif failedAttempts == 1:
    print("________\n|       O\n|\n|\n|__________")
  elif failedAttempts == 2:
    print("________\n|       O\n|       |\n|\n|__________")
  elif failedAttempts == 3:
    print("________\n|       O\n|       |\\ \n|\n|__________")
  elif failedAttempts == 4:
    print("________\n|       O\n|      /|\\ \n|\n|__________")
  elif failedAttempts == 5:
    print("________\n|       O\n|      /|\\ \n|      / \n|__________")
  elif failedAttempts == 6:
    print("________\n|       O\n|      /|\\ \n|      / \\ \n|__________")
#function blanks for loop that checks to see if each letter in the word is in our guessed letters list if in list display it, if not display an underscore
def display():
  global displayWord
  global play_again
  displayWord = ""
  for x in word:
    if x in letterguessed:
      displayWord = displayWord+x
    else:
      displayWord = displayWord+"_"
  if displayWord == word:
    play_again = input("Press 1 to if you want to restart: ")
    print("Congratulations, you win!")
  print(displayWord)
  if play_again == "1":
    restart()
#function to run the game. Call the function for the gallows, call functions for the blanks, display the guess letters, Create a variable for the user input to let them guess a letter, check if the letter is in the word, if its not then increase the failed attempts by 1. Add the letters to the guessed letter.
#Check to see if game ends! Allow to play again if they want If the game doesn't end we run the function again
def game():
  global letterguessed
  global failedAttempts
  global word
  global displayWord
  global play_again
  hung()
  display()
  print("Letters guessed:", letterguessed)
  letter = input("Enter a SINGLE LETTER that may be in the word: ")
  if letter in letterguessed:
    print("You've already said that letter.")
    game()
  letterguessed.append(letter)
  if letter not in word:
    failedAttempts += 1

  if failedAttempts == 7:
    print("Game Over")
    print("The word was " +word+ ".")
    play_again = input("Press 1 to if you want to restart: ")
    if play_again == "1":
      restart()

  
  game()
    
     
restart()
game()