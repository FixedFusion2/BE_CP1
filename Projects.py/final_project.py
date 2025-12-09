
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
    print("Where in Woods Landing do you want to go next?")
    print("1. The House\n2. The Police Station\n3. The Hotel\n4. David's bar\n5. Bill's Diner\n6. Smith's Supermarket\n7. Arby's\n8. Frank's Farm\n9. The Woods")
    main_location = input("Typer 1-9 to determine where to go: ")
    if main_location == "1":
        the_house()
    if main_location == "2":
        police_station()                      
#FUNCTION Combat

    #combat_active is set to True
    #While combat_active is True
        #PRINT Health: player health    Enemy health: enemy_health
        #PRINT What do you want to do? 1. Punch 2. Use Item 3. Run

        #combat_choice is set to INPUT 1-3

        #IF combat_choice is set to 1
            #Calculate player_damage based on strength and weapon
            #Subtract player_damage from enemy_health
            #PRINT You hit the enemy and did <player_damage> damage
        #ALSO IF choice is set to 2
            #PRINT What item do you want to use?
            #Use item from dictionary backapck
            #update player stats
            #CONTINUE loop
        #ALSO IF choice is set to 3
            #random_escape equals 1
            # PRINT You managed to escape!
            #combat_active is set to FALSE
            #RETURN "escape"
        #ELSE
        #    You failed to escape!
        #enemy_damage is set to 50
        #subtract enemy_damage from player_health
        #PRINT Enemy did <enemy_damage? damage!
        #IF player_health <= 0
            #PRINT You died.
            #combat_active is set to False
            #RETURN "player_dead"
        #IF enemy_health <= 0
            #PRINT You defeated the enemy!
            #combat_active is set to false
            #RETURN "enemy_dead"

#Maybe Function system for changing locations.

#FUNCTION The House
#backpack is set to a DICTIONARY
backpack = {}
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
            police_location = input("Type 1-5 to decide where to go.")
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
                    backpack["Pistol"] = 50
                    print("You see a medpack. Medpack added to beckpack.")
                    backpack['Medpack'] = 50
                    continue
    #ALSO IF police_location is set to 3
            if police_location == "3":
        #PRINT You head to the cells. Newline. The Prisonmates are sleeping.
                print("You Enter the cells\nThe Prisonmates are sleeping.")
                continue
    #ALSO IF police_location is set to 4
            if police_location == "4":
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
        hotel_location = input("Type 1-5 to decide where to go.")
    #IF hotel_location is set to 1
        if hotel_location == "1":
        #PRINT You head to room 201, with the other police officer. You enter the room and find blah blah blah.
            print("You head to room 201, with the other police officer.\nYou enter the room and see a mess, overturned tables, writing on the walls, and pictures of the victim on the walls.")
            continue
    #IF hotel_location is set to 2
        if hotel_location == "2":
        #PRINT You head to the Front Desk, a lady greets you and hands you a record of the guests. Guest Record added to backpack.
            if 'Guest Record' in backpack.keys():
                print("You've already been here and gotten the Guest Record.")
                continue
            else:
                print("You head to the Front Desk, a lady greets you and hands you a record of the guests.\n Guest Record added to packback")
                backpack["Guest Record"] = "A big record of the guests fill this in later along with a way to view the backpack."
                continue
    #IF hotel_location is set to 3
        #PRINT You enter the Laundry room. You find a towel. Towel added to backpack.
    #IF hotel_location is set to 4.
        #PRINT You enter the Janitors room, you see cleaning gear all around, as you walk around you notice a single peice of ripped up paper in a trash can and find a clue. It looks likes a paper from a journal. It says, *I'm meeting up with the Crypts at David's to discuss the elimination of _______*. Clue added to backpack.
    #ELSE
        #PRINT You leave the Hotel.

#FUNCTION David's Bar
    #PRINT You enter David's Bar. David greets you and gives you a beer. Beer added to backpack. who would you like to go to talk to at the bar, or where would you like to go? Newline. 1. Talk to David.Newline. 2. Talk to Stranger in back.Newline. 3. Talk to Henry at the Pool table.Newline. 4. Explore the outside back of the Bar.Newline. 5. Leave the bar.
    #bar_location is set to INPUT type 1-5 to decide where or who to go to.
    #IF bar_location is set to 1
        #PRINT David Greets you. David: "Hello John, how can I help you?"
        #david_choice is set to INPUT 1. "Tell me about the Crypts."" 2."What do you know about the murder?" 3."Nevermind."
        #IF david_choice is set to 1
            #PRINT David: "I saw some sketchy guys out back, you should go ask them."
        #ALSO IF david_choice is set to 2
            #PRINT David: "I don't really know anything but, I've heard rumors. Talk to the guy in the back."
        #ELSE:
            #PRINT David: "Alright."
    #IF bar_location is set to 2
        #PRINT Stranger: "What do you want?"
        #stranger_choice is set to INPUT 1. "I'm here for the crypts." 2. "What do you know about the murder?" 3. "Nevermind."
        #IF stranger_choice is set to 1
            #PRINT Stranger: "I heard they're are having a meeting out back, they're selling the goods."
        #ALSO IF stranger_choice is set to 2
            #PRINT Stranger: "I don't know anything, but I saw some guy running around franks farm."
        #ELSE stranger_choice is set to 3
            #PRINT Stranger: "Go away then."
    #IF bar_location is set to 3
        #PRINT Henry: "Hey john, whats up?"
        #henry_choice is set to INPUT 1. "What do you know about the murder?" 2. "Have you seen any suspicious activity?" 3."Nevermind."
        #IF henry_choice is set to 1
            #PRINT Henry: "Honestly nothing, Its awful what happened though."
        #IF henry_choice is set to 2
            #PRINT Henry: "I was walking around the forest with my dog and I saw a guy run into a shed about 200ft away."
        #IF henry-choice is set to 3
            #PRINT Henry: "Okay."
    #IF bar_location is set to 4
        #PRINT You explore the back and find 3 guys huddled around a dumpster.
        #PRINT A stranger approaches. Stranger: "What are you doing here?"
        #Have combat fight with the items in your inventory.
        #If you win the fight
            #PRINT The strangers run away and drup a peice of paper, and 1 bags of speed steroids, and the pipes tehy were fighting you with.
    #ELSE
        #PRINT You leave the bar.

#FUNCTION Bill Diner
    #PRINT You enter Bill's diner. Where to you want to go to or who do you want to talk to? 1. Bill 2. Ask a stranger.  3. Look out back. 4. Leave the bar.
    #diner_location is set to INPUT Where or who do you want to go to, type 1-4.
    #IF diner_location is set to 1
        #PRINT Bill: "Hello John, what can I do for you?"
        #bill_choice is set to INPUT 1. What do you know about the murder? 2. Have you seen any suspicious acitivity? 3. Can I get a meal? 4. Nevermind
        #IF bill_choice is set to 1
            #PRINT Bill: "I don't know much but that Gang has been hanging around here lately."
        #ALSO IF bill_choice is set to 2
            #PRINT Bill: "I saw a guy hanging around Smith's, grabbing something from a dumpster."
        #ALSO IF bill_choice is set to 3.
            #PRINT Bill: "Sure heres a Hamburger on me!" Hamburger added to Backpack.
        #ELSE
            #PRINT Alright
    #IF diner_location is set to 2
        #PRINT Stranger: "What is it?"
        #stranger1_choice is set to INPUT 1. What do you know about the murder? 2. Have you seen any suspicious activity? 3. Nevermind.
        #IF stranger1_choice is set to 1
            #PRINT Honestly nothing, I terrible what happened to the victim though.
        #ALSO IF stranger1_choice is set to 2
            #PRINT I saw a guy walking around with a gun by a shed in the woods.
        #ELSE:
            #PRINT Okay then.  
    #IF diner_location is set to 3
        #PRINT You enter outback of the diner, there is a group of guys hanging around a dumpster.
        #PRINT Stranger: "Hey what are you do here?!"
        #have a combat fight with items in your inventory if you win you get streength steroid and a clue about the guys in the woods
    #IF diner_location is set to 4
        #PRINT you leave the bar

#FUNCTION Smith Supermarket
    #PRINT You start walking around Smith's Supermarket, you can't go inside because its closed.
    #action_choice is set to INPUT You see a guy hanging around the backdoor what do you do? 1. Attack 2. Follow Him 3. Ask him what he's doing here. 4. Just leave.
    #IF action_choice is set to 1
        #PRINT You attack the man
        #Combat thing, maybe a function? if you win he drops a clue that talks about a meeting in the woods, and he runs away. If you lose you die.
    #IF action_choice is set to 2
        #PRINT You follow him but he goes around a corner and seems to disappear
    #IF action_choice is set to 3
        #PRINT He jumps in surprise and runs away
    #ELSE
        #PRINT You leave smith's supermarket.

#FUNCTION Arbys
    #PRINT You walk to Arby's
    #set arby_choice to INPUT What do you want to do? 1. Grab a Sandwhich 2. Leave
    #IF arby_choice is set to 1
        #PRINT Arby's Employee: "Here you go that will be 7.59", You: "Prices these days are ridiculous." Roast Beef Sandwhich added to backpack.
    #ALSO IF arby_choice is set to 2.
        #PRINT You leave Arby's

#FUNCTION Frank's Farm
    #PRINT You walk in to Frank Farm.
    #farm_location is set to INPUT What do you do? 1. Talk to Frank. 2. Explore The Fields 3. Explore the shed. 4. Leave The Farm
    #IF farm_location is set to 1
        #PRINT You: "Hello Frank" Frank: "Hello John, what can I help you with?"
        #Set frank_choice is set to INPUT 1. What do you know about the murder? 2. Have you seen any suspicious acitivty? 3. Nevermind.
        #IF frank_choice is set to 1
            #PRINT I don't really know anything john.
        #ALSO IF frank_choice is set to 2
            #PRINT I saw man running around my fields, I tried chasing him out but he might be bakc again.
        #ELSE
            #PRINT All right.
    #ALSO IF farm_location is set to 2
        #PRINT You see a man run into the woods with an axe in his hand, the murder weapon...
    #ALSO IF farm_location is set to 3
        #PRINT You find a pitchfork in the shed. Pitchfork added to backpack.
    #ELSE
        #PRINT You leave the farm.

#FUNCTION The Woods
    #PRINT You enter the wodds following the man with the axe. Eventually you see him enter a shed.
    #You see him take off his mask its the ARBY'S MANAGER, Jimmy Franderson. That makes sense, he is the leader of the crypts.
    #PRINT "You: Jimmy Panderson you have the right to remain silent. Anything you say cna and will be used against you in later court."
    #PRINT "Jimmy: I don't think so John"
    #PRINT Jimmy lunges toward you with a Meat Slicer.
    # Combat with Jimmy if his health reaches 0 you win and if your heaolth reaches 0 Jimmy wins and its game over
    #If you win you knocked Jimmy out.
    #The end, maybe more epilogue later but yeah.
        
locater()
        