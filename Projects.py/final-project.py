#FUNCTION The House
    #backpack is set to a LIST
	#PRINT You Enter the House. What do you want to explore? Newline. 1. The Bedroom Newline. 2. The Living Room Newline. 3. The Basement Newline. 4. The Attic Newline. 5. The Kitchen Newline. 6. The loft. Newline. 7. Leave the house.
	#house_location is Set to INPUT type 1-7 to decide where to look.
	#IF house_location is set to 1
		#PRINT You explore the bedroom. Newline You find a baseball bat. Newline. Baseball bat added to backpack.
	#ALSO IF house_location is set to 2
		#PRINT You explore the living room, the scene of the crime. Newline The murder victim is still on the floor. Newline. You find a clue next to the murder victim. Newline. A crumpled piece of paper is in the pocket of the victim. It's a message from the local gang. Newline Its says: *You better watch out, you know what you did. - The Crypts.* Newline. Clue added to backpack. Newline. “She was involved with the Crypts?”
		#PRINT Clue added to backpack.
	#ALSO IF house_location is set to 3
		#PRINT You explore the basement. There are cardboard boxes everywhere. There is a medpack on the floor. Newline Medpack added to backpack.
	#ALSO IF house_location is set to 4
		#PRINT You explore the attic. It's very dusty up here. Newline You find a box with a bunch of drugs in plastic bags. Newline “She must’ve been involved with the Crypts.”
	#ALSO IF house_location is set to 5
		#PRINT You explore the kitchen. You go to the fridge and find coffee. Newline Coffee added to the backpack.
	#ALSO IF house_location is set to 6
		#PRINT You explore the loft. Nothing is here.
	#ELSE
		#PRINT You leave the house.

#FUNCTION Police Station
	#PRINT You enter the Police Station. Where do you want to go? Newline 1. Your office. Newline 2. The Armory. Newline 3. The cells. Newline 4. The Interrogation rooms. Newline 5. Leave the police station.
    #police_location is set to INPUT type 1-5 to decide where to go to.
    #IF police_location is set to 1
        #PRINT You head to your office. There isn't much here.
    #ALSO IF police_location is set to 2
        #PRINT You head to the armory. You see a pistol. Pistol added to backpack. You see a medpack. Medpack added to beckpack. You see handcuffs. Handcuffs added to backpack.
    #ALSO IF police_location is set to 3
        #PRINT You head to the cells. Newline. The Prisonmates are sleeping.
    #ALSO IF police_location is set to 4.
        #PRINT You head to the interrogation rooms. No one is here.
    #ELSE
        #PRINT You leave the police station

#FUNCTION The Hotel
    #PRINT You enter the Hotel. You are greeted by a police officer telling you they found the room of the murder in room 201. Where do you want to go? Newline. 1. Room 201. Newline. 2. The Front Desk .Newline. 3. The Laundry Room. Newline. 4. The Janitors Room.Newline. 5. Leave the Hotel
    #hotel_location is set to INPUT type 1-5 to decide where to go to.
    #IF hotel_location is set to 1
        #PRINT You head to room 201, with the other police officer. You enter the room and find blah blah blah.
    #IF hotel_location is set to 2
        #PRINT You head to the Front Desk, a lady greets you and hands you a record of the guests. Guest Record added to backpack.
    #IF hotel_location is set to 3
        #PRINT You enter the Laundry room. You find a towel. Towel added to backpack.
    #IF hotel_location is set to 4.
        #PRINT You enter the Janitors room, you see cleaning gear all around, as you walk around you notice a single peice of ripped up paper in a trash can and find a clue. It looks likes a paper from a journal. It says, *I'm meeting up with the Crypts at David's to discuss the elimination of _______*. Clue added to backpack.
    #ELSE
        #PRINT You leave the Hotel.

#FUNCTION David's Bar