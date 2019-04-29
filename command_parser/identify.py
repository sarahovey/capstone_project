import items
import room

#The functions here will be used to identify the names of rooms, items, or npcs within user inputs.
#After identifying, it will return only the name of the identified object for data purposes

#Identifies actions the user intends to do
def identifyAction(userInput, actionList):
    for action in actionList:
        if action in userInput:
            return action
        else:
            return "Action Invalid."

#Identifies specific room within user input
def identifyRoom(userInput, roomList):
    for room in roomList:
        if room in userInput:
            return room

#Identifies specific item within user input
def identifyItem(userInput, itemList):
    for item in itemList:
        if item in userInput:
            return item

#Identifies NPC type within user input
def identifyNPC(userInput, npcList):
    for npc in npcList:
        if npc in userInput:
            return npc


