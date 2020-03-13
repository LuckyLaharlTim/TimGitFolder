###########################################################################################
# Name: Timothy Oliver
# Date: 15 January 2020
# Description: Make a text-based game where players can explore and get objects; modifications are made from the base source code from class
###########################################################################################
## Additions to this program:
##         addition of multiple new rooms, items, and grabbables;
##         exits above and below pre-existing rooms (multiple floors) and thereby some one-way exits (one hole that does so);
##         another instance where death can occur;
##         a way for players to exit the game with the best outcome
##         (one summary line is the most positive) which involves finding an item or two and going through a specific exit;
##         the ability to check items in one's inventory, see your inventory or a room in its individual print line, and use items that are grabbed;
##         utilizes some puzzles and hints
##        (generally the grabbables in a room are hinted at or outright stated when necessary--like when they are too difficult to describe or involve puzzles to know their presence);
##         on the note of puzzles, a room that changes based on player actions was implemented;
##         changes to responses based on the noun specified were made;
##         there is also a summary line when the player ends the game that also changes based on how they end it;
##         for low-turn-count runs, there is also an action counter and wasted action counter
###########################################################################################
# the blueprint for a room
class Room(object):
	# the constructor
	def __init__(self, name):
		# rooms have a name, exits (e.g., south), exit locations (e.g., to the south is room n),
		# items (e.g., table), item descriptions (for each item), and grabbables (things that can
		# be taken into inventory)
		self.name = name
		self.exits = []
		self.exitLocations = []
		self.items = []
		self.itemDescriptions = []
		self.grabbables = []
		self.grabbableDesc = []
		self.useText = []
		self.activatedText = ""

	# getters and setters for the instance variables
	@property
	def name(self):
		return self._name

	@name.setter
	def name(self, value):
		self._name = value

	@property
	def exits(self):
		return self._exits

	@exits.setter
	def exits(self, value):
		self._exits = value

	@property
	def exitLocations(self):
		return self._exitLocations

	@exitLocations.setter
	def exitLocations(self, value):
		self._exitLocations = value

	@property
	def items(self):
		return self._items

	@items.setter
	def items(self, value):
		self._items = value

	@property
	def itemDescriptions(self):
		return self._itemDescriptions

	@itemDescriptions.setter
	def itemDescriptions(self, value):
		self._itemDescriptions = value

	@property
	def grabbables(self):
		return self._grabbables

	@grabbables.setter
	def grabbables(self, value):
		self._grabbables = value

	@property
	def grabbableDesc(self):
		return self._grabbableDesc

	@grabbableDesc.setter
	def grabbableDesc(self, value):
		self._grabbableDesc = value

	@property
	def useText(self):
		return self._useText

	@useText.setter
	def useText(self, value):
		self._useText = value

	@property
	def activatedText(self):
		return self._activatedText

	@activatedText.setter
	def activatedText(self, value):
		self._activatedText = value

	# adds an exit to the room
	# the exit is a string (e.g., north)
	# the room is an instance of a room
	def addExit(self, exit, room):
		# append the exit and room to the appropriate lists
		self._exits.append(exit)
		self._exitLocations.append(room)

	# adds an item to the room
	# the item is a string (e.g., table)
	# the desc is a string that describes the item (e.g., it is made of wood)
	def addItem(self, item, desc):
		# append the item and description to the appropriate lists
		self._items.append(item)
		self._itemDescriptions.append(desc)

	# adds a grabbable item to the room
	# the item is a string (e.g., key)
	def addGrabbable(self, item, desc, use):
		# append the item, its description, and usage text to the list
		self._grabbables.append(item)
		self._grabbableDesc.append(desc)
		self._useText.append(use)

	# removes a grabbable item from the room
	# the item is a string (e.g., key)
	def delGrabbable(self, item):
		# remove the item from the list
		# personally saw no reason to remove the grab.'s description and use text from the room
		self._grabbables.remove(item)

	# adds an activation phrase to the room given the use
	#  of a specific grabbable to provide hints
	# activationReq is the text that prompts the
	#  room's hidden description to be stated ('appropriate use text')
	def addActivation(self, activationReq):
		if (activationReq == "You try to insert the key somewhere nearby . . . ."):
			self._activatedText =\
			("\nThe key fits into the box's lock. (As expected!)\nYou open it up and see a parachute.")
		elif (activationReq == "You try to hand one bottle to someone nearby and take one for yourself."):
			self._activatedText =\
			("\nThe bottle fits perfectly in the life-sized statue's hand.\nIt shouts a hearty 'Hear! hear!' and a drawer at its feet opens to reveal a jetpack.")
		elif (activationReq == "You use the bright light to get your bearings."):
			self._activatedText =\
			("\nYou can now see in the pitch-black room.\nIt is empty save for a piece of paper in the middle of the floor.")
			self.addItem("paper", "It reads 'Death is victory.'\nYou notice a copy underneath.")
		
		

	# returns a string description of the room
	def __str__(self):
		# first, the room name
		s = "You are in {}.\n".format(self.name)

		# next, the items in the room
		s += "You see: "
		for item in self.items:
			s += item + " "
		s += "\n"

		# next, the exits from the room
		s += "Exits: "
		for exit in self.exits:
			s += exit + " "

		return s

###########################################################################################
# creates the rooms
def createRooms():
	# r1, r2, r3, r4, . . ., r11 are the rooms' object references; names are in format("Room #")
	global currentRoom

	r1 = Room("Room 1")
	r2 = Room("Room 2")
	r3 = Room("Room 3")
	r4 = Room("Room 4")
	r5 = Room("Room 5")
	r6 = Room("Room 6")
	r7 = Room("Room 7")
	r8 = Room("Room 8")
	r9 = Room("Room 9")
	r10 = Room("Room 10")
	r11 = Room("Room 11")
	

	# add exits to room 1
	r1.addExit("east", r2)
	r1.addExit("south", r3)
	r1.addExit("down", r11)

	# add grabbables to room 1
	r1.addGrabbable("key", "Wow! An intricately fashioned skeleton key!", "You try to insert the key somewhere nearby . . . .")

	# add items to room 1
	r1.addItem("chair", "It is a wooden chair.")
	r1.addItem("table", "It is a plastic table with the wrapping still on it. There is a key on top.")
	r1.addItem("stairs", "Creaky wooden stairs. Where could they lead?")

	# add exits to room 2
	r2.addExit("west", r1)
	r2.addExit("south", r4)
	
	# add items to room 2
	r2.addItem("rug", "It is a bear rug.")
	r2.addItem("fireplace", "It is hot with blue flames!!")

	# add exits to room 3
	r3.addExit("east", r4)
	r3.addExit("north", r1)

	# add grabbables to room 3
	r3.addGrabbable("book", "There's a note inside that reads 'Take a leap of faith! Down, might I add.'", "You read the book for a while.")

	# add items to room 3
	r3.addItem("bookshelves", "They are dusty with many empty shelves. One book sticks out to you.")    
	r3.addItem("statue", "It is basic.")
	r3.addItem("desk", "The statue and book are resting on the desk.")

	# add exits to room 4
	r4.addExit("west", r3)
	r4.addExit("north", r2)
	r4.addExit("south", None)
	r4.addExit("up", r5)

	# add grabbables to room 4
	r4.addGrabbable("6-pack", "Perfect for a 'Dilly dilly!' with a friend or two.", "You try to hand one bottle to someone nearby and take one for yourself.")

	# add items to room 4
	r4.addItem("brew_rig", "Some beer is being brewed on it. Maybe you can take a some . . .")

	# add exits to room 5
	r5.addExit("down", r4)
	r5.addExit("north", r6)

	# add grabbables to room 6
	r5.addGrabbable("lantern", "Brightly lit with enough oil for years.", "You use the bright light to get your bearings.")
	r5.addGrabbable("bucket", "Can hold what comes out of your head end or your tail end. . . or something else.", "You put something in the bucket. Doing so is inconsequential.")

	# add items to room 6
	r5.addItem("closet", "Funneled light glows behind it. A lantern placed in a bucket causes the spectacle.") 

	# add exits to room 6
	r6.addExit("west", r8)
	r6.addExit("south", r5)
	r6.addExit("north", r7)

	# add items to room 6
	r6.addItem("trophy-stand", "It sparkles despite the dim lighting of the room.") 
	r6.addItem("window", "Oh, what a joy the outside must be.")

	# add exits to room 7
	r7.addExit("down", r9)
	r7.addExit("south", r6)

	# add items to room 7
	r7.addItem("hole", "Large enough to skydive through. There's no health, what's a small drop?")

	# add exits to room 8
	r8.addExit("east", r6)

	# add grabbables to room 8
	r8.addGrabbable("paper", "It reads 'Death is victory.'", "You think to make a map, but alas, there is no pen!")

	# add exits to room 9
	r9.addExit("west", r10)

	# add grabbables to room 9
	r9.addGrabbable("jetpack", "Already on and ready to use.", "You hear a voice saying: 'This is not the time to use that'.")

	# add items to room 9
	r9.addItem("life-sized statue", "It has an arm outstretched as if making a toast.") 
	r9.addItem("mattress", "The comfiness of it looks inviting.")

	# add exits to room 10
	r10.addExit("east", r9)
	r10.addExit("south", r11)

	# add grabbables to room 10
	r10.addGrabbable("parachute", "Already on and ready to use.", "You hear a voice saying: 'This is not the time to use that'.")

	# add items to room 10
	r10.addItem("coffin", "It has a wrapped up mannequin inside and is surprisingly bright pink.")
	r10.addItem("box", "Has a nice, hefty lock on the front.")

	# add exits to room 11
	r11.addExit("up", r1)
	r11.addExit("north", r10)
	r11.addExit("down", None)

	# add grabbables to room 11
	r11.addGrabbable("witch's hat", "What wisdom the unsmelling trash holds!", "You place the hat on your head and tip it over one eye defiantly.")
	r11.addGrabbable("tree branch", "How powerful you feel from the gift to hide odors!", "You strike a pose and sniff. All negative smells have dissipated.")

	# add items to room 11
	r11.addItem("trash can", "Is so clean you could lick it.")
	r11.addItem("tire", "A simple wheelbarrow tire.")
	r11.addItem("hole", "Large enough to skydive through. There's no health, what's a small drop?")

	currentRoom = r1
	
	

# displays an appropriate "message" when the player dies
# yes, this is intentionally obfuscated!
def death():
	print " " * 17 + "u" * 7
	print " " * 13 + "u" * 2 + "$" * 11 + "u" * 2
	print " " * 10 + "u" * 2 + "$" * 17 + "u" * 2
	print " " * 9 + "u" + "$" * 21 + "u"
	print " " * 8 + "u" + "$" * 23 + "u"
	print " " * 7 + "u" + "$" * 25 + "u"
	print " " * 7 + "u" + "$" * 25 + "u"
	print " " * 7 + "u" + "$" * 6 + "\"" + " " * 3 + "\"" + "$" * 3 + "\"" + " " * 3 + "\"" + "$" * 6 + "u"
	print " " * 7 + "\"" + "$" * 4 + "\"" + " " * 6 + "u$u" + " " * 7 + "$" * 4 + "\""
	print " " * 8 + "$" * 3 + "u" + " " * 7 + "u$u" + " " * 7 + "u" + "$" * 3
	print " " * 8 + "$" * 3 + "u" + " " * 6 + "u" + "$" * 3 + "u" + " " * 6 + "u" + "$" * 3
	print " " * 9 + "\"" + "$" * 4 + "u" * 2 + "$" * 3 + " " * 3 + "$" * 3 + "u" * 2 + "$" * 4 + "\""
	print " " * 10 + "\"" + "$" * 7 + "\"" + " " * 3 + "\"" + "$" * 7 + "\""
	print " " * 12 + "u" + "$" * 7 + "u" + "$" * 7 + "u"
	print " " * 13 + "u$\"$\"$\"$\"$\"$\"$u"
	print " " * 2 + "u" * 3 + " " * 8 + "$" * 2 + "u$ $ $ $ $u" + "$" * 2 + " " * 7 + "u" * 3
	print " u" + "$" * 4 + " " * 8 + "$" * 5 + "u$u$u" + "$" * 3 + " " * 7 + "u" + "$" * 4
	print " " * 2 + "$" * 5 + "u" * 2 + " " * 6 + "\"" + "$" * 9 + "\"" + " " * 5 + "u" * 2 + "$" * 6
	print "u" + "$" * 11 + "u" * 2 + " " * 4 + "\"" * 5 + " " * 4 + "u" * 4 + "$" * 10
	print "$" * 4 + "\"" * 3 + "$" * 10 + "u" * 3 + " " * 3 + "u" * 2 + "$" * 9 + "\"" * 3 + "$" * 3 + "\""
	print " " + "\"" * 3 + " " * 6 + "\"" * 2 + "$" * 11 + "u" * 2 + " " + "\"" * 2 + "$" + "\"" * 3
	print " " * 11 + "u" * 4 + " \"\"" + "$" * 10 + "u" * 3
	print " " * 2 + "u" + "$" * 3 + "u" * 3 + "$" * 9 + "u" * 2 + " \"\"" + "$" * 11 + "u" * 3 + "$" * 3
	print " " * 2 + "$" * 10 + "\"" * 4 + " " * 11 + "\"\"" + "$" * 11 + "\""
	print " " * 3 + "\"" + "$" * 5 + "\"" + " " * 22 + "\"\"" + "$" * 4 + "\"\""
	print " " * 5 + "$" * 3 + "\"" + " " * 25 + "$" * 4 + "\""

###########################################################################################
# START THE GAME!!!
actionCounter = 0       # initialized for final print statement
endState = "completing your Room Adventure"
invalidActions = 0      # counts invalid actions (actions with recognized verbs but result in default responses or non-specific ones)
# for use in various 'verb' methods
inventory = []
inventoryUse = []
inventoryDesc = []

createRooms()
while (True):

	status = "{}\nYou are carrying {}.\n".format(currentRoom, inventory) 

	if ((currentRoom == None) and ((inventory.count("jetpack") < 1) and (inventory.count("parachute") < 1))):       # check's if you go through r4 south exit without parachute/jetpack
	       death()
	       endState = "your DEATH"
	       break
	if ((currentRoom == None) and ((inventory.count("jetpack") > 0) or (inventory.count("parachute") > 0)) and (currentRoom.name == "r4")):
		endState += " with escape to freedom"
		break
	print "================================================"
	print status

	# prompt user for input
	action = raw_input("What would you like to do? ")

	action = action.lower()

	if(action == "quit" or action == "exit" or action == "bye"):            # quitting is not considered a countable action, but all other actions ('verbs') increment an action counter
		break

	# set a default response
	response = "I don't understand. Try using verb noun. Valid verbs are" \
		   " 'go,' 'look,' 'take,' 'check,' and 'use'."

	words = action.split()

	if(len(words) == 2):
		verb = words[0]
		noun = words[1]

		if (verb == "go"):
			actionCounter += 1
			# default response
			response = "Invalid exit."

			# check for valid exits in the room
			found = False
			for i in range(len(currentRoom.exits)):
				# if valid exit is found
				if (noun == currentRoom.exits[i]):
					# change found as applicable
					found = True
					
					# change currentRoom
					currentRoom = currentRoom.exitLocations[i]

					# set appropriate response
					response = "Room changed."

					# no need to check more exits
					break
                        # considers not changing rooms a wasted action (when 'going' somewhere)
			if (found != True):
				invalidActions += 1

		elif (verb == "look"):
			actionCounter += 1
			# default response
			response = "There's nothing like that around from what you can tell. If you're stuck, type 'look room'."            # changed to more generally fit
			
			# check for valid items in the room
			found = False
			for i in range(len(currentRoom.items)):
				# if valid item is found
				if (noun == currentRoom.items[i]):
					# change found as applicable
					found = True
					
					# set response to item's description                                        # set appropriate response
					response = currentRoom.itemDescriptions[i]

					# no need to check more items
					break
			if (noun == "room"):                                                                            # gives player valid nouns to 'look' at or explain anomalies
				found = True
				if (currentRoom.name == "Room 8") and \
				   (currentRoom.activatedText.count\
				   ("You can now see in the pitch-black room.\nIt is empty save for a piece of paper in the middle of the floor.") < 1): # checks if room change activation has occurred; if not, mention darkness
					response = "It is too dark to make out what's in here."

				else:
					response = "You look around and see {}.".format(currentRoom.items)
					
			if (found != True):
				invalidActions += 1

		elif (verb == "take"):
			actionCounter += 1
			# default response
			response = "I do not see that item."                                          # change to fit instance
			
			# check for valid grabbables in the room
			found = False                                       
			for index in range(0, len(currentRoom.grabbables)):
				# if valid grabbable is found
				if (noun == currentRoom.grabbables[index]):
					# change found as applicable
					found = True
					
					# add to inventory
					inventory.append(currentRoom.grabbables[index])
					inventoryDesc.append(currentRoom.grabbableDesc[index])
					inventoryUse.append(currentRoom.useText[index])
					
					# remove grabbable from the room
					currentRoom.delGrabbable(currentRoom.grabbables[index])
					
					# set response to confirmation of grabbable being taken                                        # set appropriate response
					response = "Item grabbed."

					# no need to check more items
					break
			# if no valid grabbable is found
			if (found != True):
				invalidActions += 1
				if (noun in currentRoom.items):                                                 # if the noun was an item in the room (just not grabbable), gives an explanation for wasted action
					response = "It is fixed to the floor, and you cannot pick it up."

		elif (verb == "check"):
			actionCounter += 1
			# default response
			response = "That object cannot be checked. To know what can be checked, type 'check inventory'."

			# check for valid grabbed grabbables in the inventory or for inventory itself
			found = False
			if (noun == 'inventory'):
				found = True
				
				response = "Your current inventory: {}".format(inventory)
			
			for i in range(0, len(inventory)):
				# if valid grabbed grabbable is found
				if (noun == inventory[i]):
					# change found as applicable
					found = True
					
					# set response to appropriate inventory item's description
					response = inventoryDesc[i]

					# no need to check more items
					break
			# if no valid grabbable is found
			if (found != True):
				invalidActions += 1
			


		elif (verb == "use"):
			actionCounter += 1
			
			# default response
			response = "The item cannot be used."
			default = "The item cannot be used." # different instance of same phrase for use in later comparison

			# check for valid noun (grabbed inventory item)
			found = False
			for i in range (0, len(inventory)):                             # checks the noun is in the inventory
				if (noun == inventory[i]):                                      
					response = inventoryUse[i]                      # if so, add's its usage text as the response
					currentRoom.addActivation(response)             # goes to appropriately change the response (based on which item is used)
					response += currentRoom.activatedText
					if (response in inventoryUse):                  # exits loop with no need to check remaining inventory spots
						response += "\nNothing important happened . . . ."
						break
					else:
						found = True
						break
				
			if (found != True):
				invalidActions += 1
				

	# display the response
	
	print "\n{}".format(response)

print "Congratulations on {}!\nYou took {} action(s), {} of which were invalid/wasted actions.\nYou ended the game with {}.".format(endState, actionCounter, invalidActions, inventory)
		

		

	

