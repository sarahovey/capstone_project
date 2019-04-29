import identify

#items.py - parses depending on item
#rooms.py - parses depending on room location


#Receives input from engine and understands what the user is trying to accomplish

def main(userInput, currentRoom):
    input = userInput.lower()
    inputWords = input.split()

    #First word should be command word
    if inputWords:
        actionWord = inputWords[0]
    else:
        actionWord = "null"

    if actionWord is "null"
        return "Action Invalid."

    else:
        action = identify.identifyAction(actionWord,     )
        #word is then compared to list of action words to see if it's a valid action command
        #parser then sends action to engine to carryout user action

        
        #searches through the rest of the words to find matches to see what object the
        #commands are intended for. Whether it's a room, item, or character.
    for word in inputWords:
        nextRoom = identify.identifyRoom(word,     )
        currentItem = identify.identifyItem(word,    )
        currentNPC = identify.identifyNPC(word,    )
        #after identifying the object, parser will let the engine know what actions & objects were
        #engine will then need to determine if the action on the object is valid & doable.


