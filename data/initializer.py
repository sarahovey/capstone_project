import phase
import game

class initializer:
    #how to use:
    #initialize, start parser and start screen will be automatically called
    #validate 1/2 input
    #call load_game with that input, this will return an instance of the current phase / state of the game
    def __init__(self):
        self.parser = 1
        self.current_phase = 1
        self.start_screen()
        self.game = 1
#start up the parser
    def start_parser(self):
        print("starting parser, return an instance")

#display start screen
    def start_screen(self):
        print("Press 1 for new game, 2 for saved game")

#wait for input
    def load_game(self, input):
        if input == "1":
            print("Starting new game...")
            self.game = game.new_game()
            #self.current_phase = phase.Phase1()
            #return self.current_phase
        elif input == "2":
            print("Load saved game")
        else:
            print("unknown game load type")

#load game function
#take input from 
#engine should call initializer.load(input) #can only be new or continue