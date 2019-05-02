"""
engine file starts the game
and progresses the story
#init data/objects?
#init room
#init npcs
#init items
#init parser
"""

#import all files because the engine will use them all
import * from data
import * from command_parser
import * from engine

    """
    1. load the game
        a) load room
        b) load npcs
        c) load items
    d) once that is taken care of 
    
    2. player actions
        a) init command parser to read input
        b) command parser directs data and engine
        c) engine runs whatever command parser does
    3. finish game
    """

print("welcome to poe's adventure!")
print("type in 'start' to begin your doggo adventure")

if(raw_input() == 'start')
    #run game

if(raw_input() == 'quit')
    exit()

#function to read command parser
engine_parser():
    pass