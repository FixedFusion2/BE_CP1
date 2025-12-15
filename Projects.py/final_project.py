import random
#backpack is set to a DICTIONARY
backpack = {}
pistol_ammo = 6
#enemy names and health dicitonary
enemy = {"name":"Unknown Thug","health": 50, "attack": 15, "description": "Thug hired by the crypts leader.", "loot":{"pipe": 30, "speed_drugs": 30}}
player = {"name": "John", "health": 100, "strength": 10, "speed": 20, "backpack":backpack}
jimmy = {"name": "Jimmy", "Health": 120, "attack": 30, "description": "The leader of the criminal gang, The Crypts, and the local Arby's Manager.", "loot": "meat slicer"}
jimmy_defeated = False
diner_enemy = {"name": "Uknown", "Health": 50, "attack": 25, "description": "A thug outisde the diner guarding a dumpster.", "loot":{"pipe": 30, "strength_drugs": 1, "clue": "Lets meet up with J in the w----"}}
enemy2 = {"Thug":{"name":"Unknown Thug","health": 60, "attack": 25, "description": "Thug hired by the crypts leader.", "loot":{"pipe": 30,"clue3":"Meet up in woods on ------."}}}
weapons_damage = {"baseball-bat": 30, "Pistol": 40, "Pitchfork": 30, "pipe": 30}
#Woods landing missouri is the name of the town

#     ____      ____                     __          _____                          __   _                    ____    ____                        __                    
#    |_  _|    |_  _|                   |  ]        |_   _|                        |  ] (_)                  |_   \  /   _|                      |  ]                   
#      \ \  /\  / / .--.    .--.    .--.| |  .--.     | |      ,--.   _ .--.   .--.| |  __   _ .--.   .--./)   |   \/   |  __   _   _ .--.   .--.| | .---.  _ .--. 
#       \ \/  \/ // .'`\ \/ .'`\ \/ /'`\' | ( (`\]    | |   _ `'_\ : [ `.-. |/ /'`\' | [  | [ `.-. | / /'`\;   | |\  /| | [  | | | [ `/'`\]/ /'`\' |/ /__\\[ `/'`\]                                                             
#        \  /\  / | \__. || \__. || \__/  |  `'.'.   _| |__/ |// | |, | | | || \__/  |  | |  | | | | \ \._//  _| |_\/_| |_ | \_/ |, | |    | \__/  || \__., | |     
#         \/  \/   '.__.'  '.__.'  '.__.;__][\__) ) |________|\'-;__/[___||__]'.__.;__][___][___||__].',__`  |_____||_____|'.__.'_/[___]    '.__.;__]'.__.'[___]                                                        
#                                                                                                   ( ( __))                                                                                                                                             
#                                                 .........                                          
#                                              -%%%%%%%%%%%%+.                                       
#                                             :%%%%%%%%%%%%%#+.                                      
#                                            .*%%%%%%%%%%%%%%%-.                                     
#                                            #%%%%%%%%%%%%%%%%%:                                     
#                                           .::=#%%%%%%%%%%#=::..                                    
#                                      .=*#%**:...       .....+*%%**:.                               
#                                   ..+%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#:                              
#                                       .:+*%%%%%%%%%%%%%%%%%%%%#+=..                                                           
#                                          :%*   ..:-===:..   .%#.                                   
#                                          :%*....            .%#.                                   
#                                          .#%:%..           .%%:                                    
#                                          .:%%-%-. ...      +%+                                     
#                                            :%%*-%*=..   .:%%=.                                     
#                                          .-#%-%%%++--=+#%%+.                                       
#                                       .=%%%-. ..-+*##**+....                                       
#                                     .-%%%%#                                                        
#                                   .:%%%%%...                                                       
#                                  .%%%%%:...                                                        
#                                .#%%%%-..                                                           
#                              .+%%%%+....                                                           
#                              :-%%*....                                                             
#                               .....                                                                
#FUNCTION Location switchers
def locater():
    while True:
        print("Where in Woods Landing do you want to go next?")
        print("1. The House\n2. The Police Station\n3. The Hotel\n4. David's bar\n5. Bill's Diner\n6. Smith's Supermarket\n7. Arby's\n8. Frank's Farm\n9. The Woods")
        main_location = input("Type i, to access inventory. Type 1-9 to determine where to go: ")
        if main_location == "1":
            the_house()
        elif main_location == "2":
            police_station()
        elif main_location == "3":
            the_hotel()
        elif main_location == "4":
            davids_bar()
        elif main_location == "5":
            bill_diner()
        elif main_location == "6":
            smith_market()
        elif main_location == "7":
            arbys()
        elif main_location == "8":
            franks_farm()
        elif main_location == "9":
            the_woods()
        elif main_location == "i":
            see_backpack()
def see_backpack():
    print(backpack)
#Item Slection
def use_item(player):
    backpack = player["backpack"]
    if not backpack:
        print("Your backpack is empty.")
        return
    for item, amount in backpack.items():
        print(f"{item}:{amount}")
    choice = input("Choose an item to use: ").strip().lower()
    #Medpacks
    if choice == "medpack" and "Medpack" in backpack:
        if backpack.get("Medpack", 0) > 0:
            player["health"] += 25
            backpack["Medpack"] -= 1
            print("You use a medpack and heal 25 HP.")
        else:
            print("You have no medpacks.")
    #Strength
    elif choice in ["strength_drugs", "strength_drug"] and "strength_drugs" in backpack:
        if backpack.get("strength_drugs", 0) > 0:
            backpack["strength_drugs"] -=1
            print("You take a strength drug. Punch damage increased.")
        else:
            print("You have none.")
    #Speed
    elif choice in ["speed_drugs", "speed_drug"] and "speed_drugs" in backpack:
        if backpack.get("speed_drugs", 0) > 0:
            backpack["speed_drugs"] -= 1
            print("You take a speed drug. Escape chance boosted.")
        else:
            print("you have none.")
    else:
        print("You can't use that item.")

#FUNCTION Combat
def combat(player,enemy):
    global pistol_ammo
    print(f"A {enemy['name']} attacks you.")
    print({enemy["description"]})
    enemy_hp = enemy.get("health", enemy.get("Health"))
    #Combat loop
    while player["health"] > 0 and enemy_hp > 0:
        print(f"\nYour HP: {player['health']} | {enemy['name']} HP: {enemy_hp}")
        print("Actions:\n1. Punch\n2. Run\n3. Use item\n4. Use Weapon")
        attack = input("Choose what do to. Type 1-4: ")
        #Punch
        if attack == "1":
            strength_bonus = backpack.get("strength_drugs", 0)
            damage = 5 + (strength_bonus * 3)
            print(f"You punch the {enemy['name']} and do {damage}.")
            enemy_hp -= damage
        #Run
        elif attack == "2":
            speed_bonus = backpack.get("speed_drugs", 0)
            escape_chance = 30 + (speed_bonus * 15)
            if random.randint(1,100) <= escape_chance:
                print("You escaped.")
                return "escaped"
            else:
                print(f"You try to run but the {enemy['name']} stops you.")
        #Use Item
        elif attack == "3":
            use_item(player)
        elif attack == "4":
            print("Weapons in your backpack:")
            for item in player["backpack"]:
                if item in weapons_damage:
                    if item == "Pistol":
                        print(f"Items: {item} ({pistol_ammo} shots)")
                    else:
                        print(f"Items: {item}")
            weapon_choice = input("Type the weapon you want to use: ").strip()
            if weapon_choice in player["backpack"] and weapon_choice in weapons_damage:
                if weapon_choice  == "Pistol":
                    if pistol_ammo <= 0:
                        print("You're out of ammo.")
                    else:
                        pistol_ammo -= 1
                        damage = weapons_damage["Pistol"]
                        print(f"You fire the pistol ({pistol_ammo} shots left) and do {damage} to {enemy["name"]}")
                        enemy_hp -= damage
                else:        
                    damage = weapons_damage[weapon_choice]
                    print(f"You use {weapon_choice} and do {damage} damage to {enemy['name']}.")
                    enemy_hp -= damage
            else:
                print("You don't have that weapon.")
    #Enemy turn befroe chicking if player died.
        if enemy_hp > 0:
            dmg = enemy["attack"]
            print(f"The {enemy['name']} does {dmg} damage.")
            player["health"] -= dmg
        #Outcome
    if player["health"] <= 0:
        print("You died.")
        return "dead"
    else:
        print(f"You defeated the {enemy['name']}.")
        return "victory"




#Maybe Function system for changing locations.

#FUNCTION The House
def the_house():

	#PRINT You Enter the House. What do you want to explore? Newline. 1. The Bedroom Newline. 2. The Living Room Newline. 3. The Basement Newline. 4. The Attic Newline. 5. The Kitchen Newline. 6. The loft. Newline. 7. Leave the house.
    # #house_location is Set to INPUT type 1-7 to decide where to look.
    print("You Enter the House. What do you want to explore?")
    while True:
        print("\n1. The Bedroom \n2. The Living Room \n3. The Basement \n4. The Attic\n5. The Kitchen \n6. The loft. \n7. Leave the house.")
        house_location = input("Type 1-7, to decide where to look: ")
        #IF house_location is set to 1
        if house_location == "1":
            #PRINT You explore the bedroom. Newline You find a baseball bat. Newline. Baseball bat added to backpack.
            if "baseball-bat" in backpack.keys():
                print("You've already been here, there is nothing here.")
                continue
            else:
                print("You explore the bedroom.\nYou find a baseball bat.\nBaseball bat added to backpack")
                backpack["baseball-bat"] = 30
                continue
	#ALSO IF house_location is set to 2
        elif house_location == "2":
		#PRINT You explore the living room, the scene of the crime. Newline The murder victim is still on the floor. Newline. You find a clue next to the murder victim. Newline. A crumpled piece of paper is in the pocket of the victim. It's a message from the local gang. Newline Its says: *You better watch out, you know what you did. - The Crypts.* Newline. Clue added to backpack. Newline. “She was involved with the Crypts?”
            if "Clue1" in backpack.keys():
                print("You've already been here, there is nothing here.")
                continue
            else:
                print("You explore the living room, the scene of the crime.\nThe murder victim is still on the floor.\nYou find a clue next to the murder victim.\nA crumpled piece of paper is in the pocket of the victim. \nIt's a message from the local gang.\nIts says: *You better watch out, you know what you did. - The Crypts.*\n“She was involved with the Crypts?\nClue1 added to backpack.”")
                backpack["Clue1"] = "*You better watch out, you know what you did. - The Crypts.*"
                continue
		#PRINT Clue added to backpack.
	#ALSO IF house_location is set to 3
        elif house_location == "3":
		#PRINT You explore the basement. There are cardboard boxes everywhere. There is a medpack on the floor. Newline Medpack added to backpack.
            if "Medpack" in backpack.keys():
                print("You've already been here, there is nothing here.")
                continue
            else:
                print("You explore the basement.\nThere are cardboard boxes everywhere.\nThere is a medpack on the floor.\nMedpack added to backpack.")
                backpack["Medpack"] = 50
                continue
	#ALSO IF house_location is set to 4
        elif house_location == "4":
		#PRINT You explore the attic. It's very dusty up here.
            print("You explore the attic. It's very dusty up here.\nThere are old boxes everywhere")
            continue
	#ALSO IF house_location is set to 5
        elif house_location == "5":
		#PRINT You explore the kitchen. You go to the fridge and find coffee. Newline Coffee added to the backpack.
            if "Coffee" in backpack.keys():
                print("You've already been here, there is nothing here.")
                continue
            else:
                print("You explore the kitchen. You go to the fridge and find coffee.\nCoffee added to the backpack.")
                backpack["Coffee"] = 15
                continue
	#ALSO IF house_location is set to 6
        elif house_location == "6":
		#PRINT You explore the loft. Nothing is here.
            print("You explore the loft. Nothing is here.")
            continue
	#ELSE
        else:
		#PRINT You leave the house.
            print("You leave the house.")
            break
            #Call Locations functions
    locater()

#FUNCTION Police Station
def police_station():
        #PRINT You enter the Police Station. Where do you want to go? Newline 1. Your office. Newline 2. The Armory. Newline 3. The cells. Newline 4. The Interrogation rooms. Newline 5. Leave the police station.
        print("You enter the Police Station. Where do you want to go?\n1. Your office.\n2. The Armory.\n 3. The cells.\n4. The Interrogation rooms.\n5. Leave the police station.")
        while True:
            #police_location is set to INPUT type 1-5 to decide where to go to.
            police_location = input("Type 1-5 to decide where to go: ")
            #IF police_location is set to 1
            if police_location == "1":
                #PRINT You head to your office. There isn't much here.
                print("You enter to your office. There isn't much here.")
                continue
            #ALSO IF police_location is set to 2
            elif police_location == "2":
                #PRINT You head to the armory. You see a pistol. Pistol added to backpack. You see a medpack. Medpack added to beckpack.
                if 'Pistol' in backpack.keys() and 'Medpack' in backpack.keys():
                    print("You've already been here and gotten the pistol and Medpack.")
                    continue
                else:
                    print("You enter to the armory. You see a pistol.\nPistol added to backpack. ")
                    backpack["Pistol"] = 40
                    print("You see a medpack. Medpack added to beckpack.")
                    backpack['Medpack'] = 50
                    continue
    #ALSO IF police_location is set to 3
            elif police_location == "3":
        #PRINT You head to the cells. Newline. The Prisonmates are sleeping.
                print("You Enter the cells\nThe Prisonmates are sleeping.")
                continue
    #ALSO IF police_location is set to 4
            elif police_location == "4":
        #PRINT You head to the interrogation rooms. No one is here.
                print("You enter the interrogation rooms. Noe one is here.")
                continue
    #ELSE
            else:
        #PRINT You leave the police station
                print("You leave the police station.")
                break
        locater()
#FUNCTION The Hotel
def the_hotel():
    #PRINT You enter the Hotel. You are greeted by a police officer telling you they found the room of the murder in room 201. Where do you want to go? Newline. 1. Room 201. Newline. 2. The Front Desk .Newline. 3. The Laundry Room. Newline. 4. The Janitors Room.Newline. 5. Leave the Hotel
    print("You enter the Hotel. You are greeted by a police officer telling you they found the room of the murder in room 201. Where do you want to go?\n1. Room 201.\n2. The Front Desk\n3. The Laundry Room.\n4. The Janitors Room.\n5. Leave the Hotel")
    while True:
    #hotel_location is set to INPUT type 1-5 to decide where to go to.
        hotel_location = input("Type 1-5 to decide where to go: ")
    #IF hotel_location is set to 1
        if hotel_location == "1":
        #PRINT You head to room 201, with the other police officer. You enter the room and find blah blah blah.
            print("You head to room 201, with the other police officer.\nYou enter the room and see a mess, overturned tables, writing on the walls, and pictures of the victim on the walls.")
            continue
    #IF hotel_location is set to 2
        elif hotel_location == "2":
        #PRINT You head to the Front Desk, a lady greets you and hands you a record of the guests. Guest Record added to backpack.
            if 'Guest Record' in backpack.keys():
                print("You've already been here and gotten the Guest Record.")
                continue
            else:
                print("You head to the Front Desk, a lady greets you and hands you a record of the guests.\n Guest Record added to packback")
                backpack["Guest Record"] = "A big record of the guests fill this in later along with a way to view the backpack."
                continue
    #IF hotel_location is set to 3
        elif hotel_location == "3":
        #PRINT You enter the Laundry room. You find a towel. Towel added to backpack.
            if "Towel" in backpack.keys():
                print("You've already been here. Theres nothing here.")
                continue
            else:
                print("You enter the Laundry room. You find a towel. Towel added to backpack.")
                backpack["Towel"] = 2
                continue
    #IF hotel_location is set to 4.
        elif hotel_location == "4":
        #PRINT You enter the Janitors room, you see cleaning gear all around, as you walk around you notice a single peice of ripped up paper in a trash can and find a clue. It looks likes a paper from a journal. It says, *I'm meeting up with the Crypts at David's to discuss the elimination of _______*. Clue added to backpack.
            if "Clue2" in backpack.keys():
                print("You've already been here, and gotten the clue.")
                continue
            else:
                print("You enter the Janitors room.\nYou see cleaning gear all around, as you walk around you notice a single peice of ripped up paper in a trash can and find a clue.\nIt looks likes a paper from a journal.\nIt says, *I'm meeting up with the Crypts at David's to discuss the elimination of _______*. Clue added to backpack.")
                backpack["Clue2"] = "*I'm meeting up with the Crypts at David's to discuss the elimination of _______*"
                continue    
    #ELSE
        else:
        #PRINT You leave the Hotel.
            print("You leave the Hotel.")
            break
    locater()

#FUNCTION David's Bar
def davids_bar():
    #PRINT You enter David's Bar. David greets you and gives you a beer. Beer added to backpack. who would you like to go to talk to at the bar, or where would you like to go? Newline. 1. Talk to David.Newline. 2. Talk to Stranger in back.Newline. 3. Talk to Henry at the Pool table.Newline. 4. Explore the outside back of the Bar.Newline. 5. sk for a beer. 6. Leave the bar.
    print("\nWho would you like to go to talk to at the bar, or where would you like to go?\n1. Talk to David.\n2. Talk to Stranger in back\n3. Talk to Henry at the Pool table.\n4. Explore the outside back of the Bar.\n5. Leave the bar.")
    while True:
    #bar_location is set to INPUT type 1-5 to decide where or who to go to.
        bar_location = input("Type 1-5 to decide where or who to go: ")
    #IF bar_location is set to 1
        if bar_location == "1":
            while True:
            #PRINT David Greets you. David: "Hello John, how can I help you?"
                print("David Greets you. David: *Hello John, how can I help you?*")
            #david_choice is set to INPUT 1. "Tell me about the Crypts."" 2."What do you know about the murder?" 3."Nevermind."
                david_choice = input("1. *Tell me about the Crypts.*\n2. *What do you know about the murder?*\n3. *Can I get a beer?*\n4. *Nevermind.* : ")
            #IF david_choice is set to 1
                if david_choice == "1":
                #PRINT David: "I saw some sketchy guys out back, you should go ask them."
                    print("David: *I saw some sketchy guys out back, you could go ask them.")
                    continue
            #ALSO IF david_choice is set to 2
                elif david_choice == "2":
                #PRINT David: "I don't really know anything but, I've heard rumors. Talk to the guy in the back."
                    print("David: *I don't really know anything but, I've heard rumors. Talk to the guy in the back.*")
                    continue
                elif david_choice == "3":
                    if "Beer" in backpack.keys():
                        print("David already gave me a beer. I should do something else.")
                        continue
                    else:
                        print("Heres a beer on the house.")
                        print("Beer added to backpack.")
                        backpack["Beer"] = 30
                        continue
            #ELSE:
                else:
                #PRINT David: "Alright."
                    print("David: *Alright, come ask me again if you need anything else.*")
                    break
            continue
    #IF bar_location is set to 2
        elif bar_location == "2":
        #PRINT Stranger: "What do you want?"
            print("Stranger: *What do you want?")
            while True:
        #stranger_choice is set to INPUT 1. "I'm here for the crypts." 2. "What do you know about the murder?" 3. "Nevermind."
                stranger_choice = input("1. *I'm here for the cyrpts.*\n2. *What do you know about the murder?*\n3. *Nevermind*: ")
        #IF stranger_choice is set to 1
                if stranger_choice == "1":
            #PRINT Stranger: "I heard they're are having a meeting out back, they're selling the goods."
                    print("Stranger: *I heard they're are having a meeting out back, they're selling the goods.")
                    continue
        #ALSO IF stranger_choice is set to 2
                elif stranger_choice == "2":
            #PRINT Stranger: "I don't know anything, but I saw some guy running around franks farm."
                    print("I don't know anything, but I saw some guy running around franks farm. ")
                    continue
        #ELSE stranger_choice is set to 3
                else:
            #PRINT Stranger: "Go away then."
                    print("Stranger: *Go away then.*")
                    break
            continue
    #IF bar_location is set to 3
        elif bar_location == "3":
        #PRINT Henry: "Hey john, whats up?"
            print("Henry: *Hey John, whats up?")
            while True:
        #henry_choice is set to INPUT 1. "What do you know about the murder?" 2. "Have you seen any suspicious activity?" 3."Nevermind."
                henry_choice = input("1. *What do you know about the murder?*\n2. *Have you seen any suspicious activity?*\n3. *Nevermind*: ")
        #IF henry_choice is set to 1
                if henry_choice == "1":
            #PRINT Henry: "Honestly nothing, Its awful what happened though."
                    print("Henry: *Honestly nothing, its awful what happened though.*")
                    continue
        #IF henry_choice is set to 2
                elif henry_choice == "2":
            #PRINT Henry: "I was walking around the forest with my dog and I saw a guy run into a shed about 200ft away."
                    print("Henry: *I was walking around the woods with my dog and I saw a guy run back into a shed about 200ft away.*")
                    continue
        #IF henry-choice is set to 3
                else:
            #PRINT Henry: "Okay."
                    print("Okay.")
                    break
            continue
    #IF bar_location is set to 4
        elif bar_location == "4":
        #PRINT You explore the back and find 3 guys huddled around a dumpster.
            if "speed_drugs" in backpack.keys():
                print("You've already been here.")
                continue
            else:
                print("You explore the back and find 3 guys huddled around a dumpster.")
                print("A stranger approaches.\nStranger: *What are you doing here?*")
                combat(player,enemy)
            #PRINT A stranger approaches. Stranger: "What are you doing here?"
            #Have combat fight with the items in your inventory.
                result = combat(player,enemy)
                if result == "victory":
                    print("The strangers run away and drop some pipes and speed steroids.")
                    backpack["speed_drugs"] = backpack.get("speed_drugs", 0) + 1
                    backpack["pipe"] = backpack.get("pipe", 0) + 1
                    continue
                elif result == "dead":
                    print("You have died. Game over.")
                    return
                elif result == "escaped":
                    print("The strangers run away.")
                    continue
        #If you win the fight
            #PRINT The strangers run away and drup a peice of paper, and 1 bags of speed steroids, and the pipes tehy were fighting you with.
    #ELSE
        else:
        #PRINT You leave the bar.
            print("You leave the bar.")
            break

#FUNCTION Bill Diner
def bill_diner():
    #PRINT You enter Bill's diner. Where to you want to go to or who do you want to talk to? 1. Bill 2. Ask a stranger.  3. Look out back. 4. Leave the bar.
    print("You enter Bill's diner.")
    while True:
        print("Where to you want to go to or who do you want to talk to?\n1. Bill\n2. Ask a stranger.\n3. Look out back.\n4. Leave the bar : ")
        #diner_location is set to INPUT Where or who do you want to go to, type 1-4.
        diner_location = input("Decide where or who to go to. Type 1-4: ")
        #IF diner_location is set to 1
        if diner_location == "1":
            #PRINT Bill: "Hello John, what can I do for you?"
            print("Bill: *Hello John, what can I do for you?*")
            while True:
                #bill_choice is set to INPUT 1. What do you know about the murder? 2. Have you seen any suspicious acitivity? 3. Can I get a meal? 4. Nevermind
                bill_choice = input("1. *What do you know about the murder?* 2. *Have you seen any suspicious acitivity?* 3. *Can I get a meal?* 4. *Nevermind?* : ")
                #IF bill_choice is set to 1
                if bill_choice == "1":
                    #PRINT Bill: "I don't know much but that Gang has been hanging around here lately."
                    print("Bill: *I don't know much, but that Gang has been hanging around here lately.*")
                    continue
                #ALSO IF bill_choice is set to 2
                elif bill_choice == "2":
                    #PRINT Bill: "I saw a guy hanging around Smith's, grabbing something from a dumpster."
                    print("Bill: *I saw a guy hanging around Smith's, grabbing something from a dumpster.")
                    continue
                #ALSO IF bill_choice is set to 3.
                elif bill_choice == "3":
                    #PRINT Bill: "Sure heres a Hamburger on me!" Hamburger added to Backpack.
                    if "Hamburger" in backpack.keys():
                        print("I've already gotten a burger from Bill, I should do something else.")
                        continue
                    else:
                        print("Bill: *Sure heres a hamburger on me!*\nHamburger added to backpack.")
                        backpack["Hamburger"] = 25
                        continue
                #ELSE
                else:
                    #PRINT Alright
                    print("Bill: *Okay then.*")
                    break
            continue
        #IF diner_location is set to 2
        elif diner_location == "2":
            #PRINT Stranger: "What is it?"
            print("Stranger: *What is it?*")
            while True:
                #stranger1_choice is set to INPUT 1. What do you know about the murder? 2. Have you seen any suspicious activity? 3. Nevermind.\
                stranger1_choice = input("1. *What do you know about the murder?*\n*2. Have you seen any suspicious activity?*\n3. *Nevermind.*")
                #IF stranger1_choice is set to 1
                if stranger1_choice == "1":
                    #PRINT Honestly nothing, I terrible what happened to the victim though.
                    print("Stranger: *Honestly nothing, I terrible what happened to the victim though.*")
                    continue
                #ALSO IF stranger1_choice is set to 2
                elif stranger1_choice == "2":
                    #PRINT I saw a guy walking around with a gun by a shed in the woods.
                    print("Stranger: *I saw a guy walking around with a weapon I couldn't make out by a shed in the woods.*")
                    continue
                #ELSE:
                else:
                    #PRINT Okay then.
                    print("Stranger: *Okay then...*")
                    break
            continue
        #IF diner_location is set to 3
        elif diner_location == "3":
            if "strength_drugs" in backpack.keys():
                print("You've already been here.")
                continue
            else:
                #PRINT You enter outback of the diner, there is a group of guys hanging around a dumpster.
                print("You enter outback of the diner, there is a group of strangers hanging around a dumpster.")
                print("A stranger approaches.\nStranger: *Hey, what are you doing here?!*")
                combat(player, diner_enemy)

                #PRINT Stranger: "Hey what are you do here?!"
                #have a combat fight with items in your inventory if you win you get streength steroid and a clue about the guys in the woods
                result = combat(player,diner_enemy)
                if result == "victory":
                    print("The strangers run away dropping a clue, strength steroids, and the pipes they fought with.")
                    backpack["strength_drugs"] = backpack.get("strength_drugs", 0) + 1
                    backpack["pipe"] = backpack.get("pipe", 0) + 1
                    backpack["clue"] = backpack.get("clue", 0) + 1
                    continue
                elif result == "dead":
                    print("You have died. Game over.")
                    return
                elif result == "escaped":
                    print("You run away from the strangers. You managed to escape.")
                    continue    
        #IF diner_location is set to 4
        else:
            #PRINT you leave the bar
            print("You leave the bar.")
        break
    locater()

#FUNCTION Smith Supermarket
def smith_market():
    #PRINT You start walking around Smith's Supermarket, you can't go inside because its closed.
    print("You start walking around Smith's Supermarket, and you find you can't go inside because its closed.")
    #action_choice is set to INPUT You see a guy hanging around the backdoor what do you do? 1. Attack 2. Follow Him 3. Ask him what he's doing here. 4. Just leave.
    if "clue3" in backpack.keys():
        print("You've already been here.")
        locater()
    else:
        action_choice = input("You see a guy hanging around the backdoor of Smith's, what do you do?\n1. Attack\n2. Follow Him\n3. Ask him what he's doing here.\n4. Just leave.")
        #IF action_choice is set to 1
        if action_choice == "1":
            #PRINT You attack the man
            print("You attack the man.")
            #Combat thing, maybe a function? if you win he drops a clue that talks about a meeting in the woods, and he runs away. If you lose you die.
            combat(player,enemy2["Thug"])
            result = combat(player, enemy2["Thug"])
            if result == "victory":
                print("You defeat the stranger and he runs away dropping a clue.")
                backpack["clue"] = backpack.get("clue3", 0) + 1
                locater()
            elif result == "dead":
                    print("You have died. Game over.")
                    return
            elif result == "escaped":
                print("You run away from the strangers. You managed to escape.")
                locater()
        #IF action_choice is set to 2
        #Then go to locater()
            locater()
        elif action_choice == "2":
            #PRINT You follow him but he goes around a corner and seems to disappear
            print("You follow him, but he goes around a corner and seems to disappear...")
            locater()
        #IF action_choice is set to 3
        elif action_choice == "3":
            #PRINT He jumps in surprise and runs away
            print("He jumps in surprise and runs away.")
            locater()
        #ELSE
        else:
            #PRINT You leave smith's supermarket.
            print("You leave Smith's Supermarket.")
        locater()

#FUNCTION Arbys
def arbys():
    #PRINT You walk to Arby's
    print("You wak to Arby's.")
    while True:
        #set arby_choice to INPUT What do you want to do? 1. Grab a Sandwhich 2. Leave
        arby_choice = input('What would you like to do?\n1. Grab a Sandwhich\n2. Leave: ')
        #IF arby_choice is set to 1
        if arby_choice == "1":
            if "Roast Beef Sandwhich" in backpack.keys():
                print("I've already ordered a sandwhich, I need to get back to work.")
                continue
            #PRINT Arby's Employee: "Here you go that will be 7.59", You: "Prices these days are ridiculous." Roast Beef Sandwhich added to backpack.
            else:
                print("Arby's Employee: *Here you go that will be 7.59*, You: *Prices these days are ridiculous.*\nRoast Beef Sandwhich added to backpack.")
                backpack["Roast Beef Sandwhich"] = 25
            continue

        #ALSO IF arby_choice is set to 2.
        elif arby_choice == "2": 
            #PRINT You leave Arby's
            print("You leave Arby's.")
            break
    locater()

#FUNCTION Frank's Farm
def franks_farm():
    #PRINT You walk in to Frank Farm.
    print("You walk into Frank's Farm.")
    #farm_location is set to INPUT What do you do? 1. Talk to Frank. 2. Explore The Fields 3. Explore the shed. 4. Leave The Farm
    while True:
        farm_location = input("What do you want to do?\n1. Talk to Frank. 2. Explore The Fields 3. Explore the shed. 4. Leave The Farm: ")
        #IF farm_location is set to 1
        if farm_location == "1":
            #PRINT You: "Hello Frank" Frank: "Hello John, what can I help you with?"
            print("You: *Hello Frank*, Frank: *Hello John, what can I help you with?*")
            #Set frank_choice is set to INPUT 1. What do you know about the murder? 2. Have you seen any suspicious acitivty? 3. Nevermind.
            while True:
                frank_choice = input("*1.What do you know about the murder?*\n*2. have you seen any suspicious activity?*\n*3.Nevermind.*")
                #IF frank_choice is set to 1
                if frank_choice == "1":
                    #PRINT I don't really know anything john
                    print("Frank: *I don't really know anythign John.*")
                    continue
                #ALSO IF frank_choice is set to 2
                elif frank_choice == "2":
                    #PRINT I saw man running around my fields, I tried chasing him out but he might be bakc again.
                    print("Frank: *I saw man running around my fields, I tried chasing him out but he might be back again...*")
                    continue
                #ELSE
                else:
                    #PRINT All right.
                    print ("*Alright then.*")
                    break
            continue
        #ALSO IF farm_location is set to 2
        elif farm_location == "2":
            #PRINT You see a man run into the woods with an axe in his hand, the murder weapon...
            print("You see a man run into the woods with an axe in his hand, the murder weapon...")
            continue
        #ALSO IF farm_location is set to 3
        elif farm_location == "3":
            if "Pitchfork" in backpack.keys():
                print("You've already been here adn gotten the pitchfork.")
                continue
            else:
                #PRINT You find a pitchfork in the shed. Pitchfork added to backpack.
                print("You find a pitchfork in the shed. Pitchfork added to backpack.")
                backpack["Pitchfork"] = 30
                continue
        #ELSE
        else:
            #PRINT You leave the farm.
            print("You leave the farm.")
            break
    locater()

#FUNCTION The Woods
def the_woods():
    global jimmy_defeated
    #PRINT You enter the wodds following the man with the axe. Eventually you see him enter a shed.
    print("You enter the woods following the man with the axe. Eventually you see him enter a shed.")
    #You see him take off his mask its the ARBY'S MANAGER, Jimmy Franderson. That makes sense, he is the leader of the crypts, thats why the Arby's was so empty when I was there. He was meeting with the crypts.
    print("You see him take off his mask its the ARBY'S MANAGER, Jimmy Franderson.\nThat makes sense, he is the leader of the crypts, thats why the Arby's was so empty when I was there.\nHe was meeting with the crypts.")
    #PRINT "You: Jimmy Panderson you have the right to remain silent. Anything you say can and will be used against you in later court."
    print("You: *Jimmy Panderson you have the right to remain silent.*\n*Anything you say can and will be used against you in later court.*")
    #PRINT "Jimmy: I don't think so John"
    print("Jimmy: *I don't think so so John.*")
    #PRINT Jimmy lunges toward you with a Meat Slicer.
    print("Jimmy lunges at ytou with a Meat Slicer.")
    # Combat with Jimmy if his health reaches 0 you win and if your heaolth reaches 0 Jimmy wins and its game over
    #If you win you knocked Jimmy out.
    #The end, maybe more epilogue later but yeah.
    result = combat(player, jimmy)
    if result == "victory":
        print("You have knocked out Jimmy, and officially solved the woods landing murder.")
        jimmy_defeated = True
        play_again()
    elif result == "dead":
            print("You have died. Game over.")
            return

def start():
    print("You get handed the case of the Woods landing murder.")
    print("After driving for a while you reach woods landing.")
    locater()

def play_again():
    print("You would you like to play again?")
    again = input("Type yes or no: ").lower()
    if again == "yes":
        start()
    else:
        exit()
start()