# TE 2nd Mad Lib

import time
import sys

def slow_print(text, delay=0.010):
       for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

adjective = input("Give me an adjective: ")
noun = input("Give me a noun: ")
plural_noun = input("Give me a plural noun: ")
aunt = input("Give mea a person in room (female): ")
adjective_2 =input("Give me another adjective: ")
clothing = input("Give me an article of clothing: ")
noun_2 = input("Give me another noun: ")
city = input("Give me a city: ")
plural_noun_2 = input("Give me another plural noun: ")
adjective_3 = input("Give me another adjective: ")
part_of_body = input("Give me a part of the body: ")
letter = input("Give me a letter of the alphabet: ")
celebtrity = input("Give me a celebrity: ")
plural_noun_3 = input("Give me another plural noun: ")
adjective_4 = input("Give me another adjective: ")
place = input('Give me a place:')
part_of_body_2 = input("Give me another part of the body:")
adjective_5 = input("Give me another adjective: ")
adjective_6 = input("Give me another adjective: ")
verb = input("give me a verb:")
plural_noun_4 = input("Give me another plural noun:")
number  = input("Give me a number:")

slow_print("There are many"+adjective+' ways to choose a/an '+noun+'. To read. '
'First, you could ask for recommendations from your friends and'+plural_noun+'. Just do not ask'+aunt+', she only reads'
+adjective_2+' books with'+clothing+'ripping goddesses on the cover. If your friends and family are no help, try checking out the'
+noun_2+'Review in The'+city+'Times. If the'+plural_noun_2+' featured there are too '+adjective_3+'for your taste, try something a little'
'more low-key. A good place to find a book is to go to your local library and browse the shelves until something catches your'
+part_of_body+'. If you see a book with a cover that has a '+letter+' on it, that means it is a staff pick by'+celebtrity+'. Celebrities are'
+plural_noun_3+' too, so those picks are usually pretty'+adjective_4+'. Of course, if you have a specific book in mind, you can'
'always go to your local'+place+'and ask for it by title, author, or subject. Be sure to also ask for'+part_of_body_2+'if you need help finding a/an'
+adjective_5+'book. And remember, there are no'+adjective_6+'books. Every book is an adventure waiting to happen. All you have to do is'+verb+'it and the world of'
+plural_noun_4+'is yours for the next'+number+'years!')

print("The End")
print("Dumb story by Mr. E")