import data
import items
import rooms

#Receives input from engine and understands what the user is trying to accomplish

#pulls arrays from data.py file into here
actionList = data.actions
roomList = data.rooms
itemList = data.items
npcList = data.npcs

class Parser:
    def __init__(self):
        self.action = None
        self.object = None
        self.preposition = None
    
    def get_action(self, userInput):
        input = userInput.lower()
        input_words = input.split()
        
        #First word should be command word
        if input_words:
            command = input_words[0]
        else:
            command = None

        if command is None:
            print("Please enter a command.")
            return 0

        else:
            if command in actionList:
                self.action = command
                #word is then compared to list of action words to see if it's a valid action command
                #parser then sends action to engine to carryout user action
        
                #searches through the rest of the words to find matches to see what object the
                #commands are intended for. Whether it's a room, item, or character.
                
                #checks to see there is also a preposition for the engine to add onto the string that's displayed to the player
                for word in input_words:
                    if word in prepositionList:
                        self.preposition = word
                
            else:
                print("Action Invalid.")
                return 0
            
        return self.action

    def get_target(self, userInput):
        input = userInput.lower()
        input_words = input.split()
        
        room = None
        item = None
        npc = None
        
        for word in input_words:
            if word in roomList:
                room = word

            if word in itemList:
                item = word

            if word in npcList:
                npc = word
            
        #after identifying the object, parser will let the engine know what actions & objects were
        #engine will then need to determine if the action on the object is valid & doable.

        if room is not None:
            self.object = room
            
        if item is not None:
            self.object = item
        
        if npc is not None:
            self.object = npc

        if self.object is None:
            print("Target object doesn't exist, please try command again on a valid object. It may be a room, item, or NPC.")
            return 0
            
        else:
            return self.object

    def print_command(self):
        if self.action is not None and self.object is not None:
                if self.preposition is not None:
                    string_display = "Doge %s %s %s." % (self.action, self.preposition, self.object)

                else:
                    string_display = "Doge %s %s." % (self.action, self.object)
