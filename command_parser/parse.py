import data
import items
import rooms
import identify

#Receives input from engine and understands what the user is trying to accomplish

#pulls arrays from data.py file
actionList = data.actions
roomList = data.rooms
itemList = data.items
npcList = data.npcs

class Parser:
    def get_action(self, userInput):
        input = userInput.lower()
        input_words = input.split()
        
        action = None

        #First word should be command word
        if input_words:
            command = input_words[0]
        else:
            command = None

        if command is None:
            return "Action Invalid."

        else:
            if command in actionList:
                action = command
                #word is then compared to list of action words to see if it's a valid action command
                #parser then sends action to engine to carryout user action
        
                #searches through the rest of the words to find matches to see what object the
                #commands are intended for. Whether it's a room, item, or character.
        return action

    def get_target(self, userInput):
        input = userInput.lower()
        input_words = input.split()
        
        object = None
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
            object = room
            
        if item is not None:
            object = item
        
        if npc is not None:
            object = npc

        return object
