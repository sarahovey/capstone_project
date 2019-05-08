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

# some sort class or function here

while(1):
    #initializing files that user wont see
    the_initializer() #class that initializes everything, runs commander_parser() and start_game()

    #instance of command_parser

    if(raw_input() == "quit")
        

# start screen
    # load, new game

#new game 
#call init function
    #make all the phase 1 objects
    #current_phase  = phase1()

    #init parser?
    #classes for intro slash whatever we need to load, they come as its coded along
#intro scene
    #calling intro class/ init intro object
    #character c reation
    #pick good boy or good girl
    #flavortext, intro stuff

#once in the game....
#loop
    #check *something* about player state to see if something different needs to be printed
        #for example, if player enters a new room, need to check whether or not we've been there before
        #and then print appropriate thing, and so on
    #if something *is* different, call the appropriate function
    #otherwise, ask for user input
    #(back to the path...)
    #enter room
    #call 

    #sub-loop
    # ask for user input
        #take raw input -> parser
        #print whatever the parser gives back
    


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