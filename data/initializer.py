import phase
import game
import test_parser

class initializer:
    #how to use:
    #initialize, start parser and start screen will be automatically called
    #validate 1/2 input
    #call load_game with that input, this will return an instance of the current phase / state of the game
    def __init__(self):
        self.start_screen()
        self.game = game.Game()
        self.parser = test_parser.Parser(self.game)
        print("done making the game in initializer")
        
    #start up the parser
    def start_parser(self):
        print("starting parser, return an instance")

    #display start screen
    def start_screen(self):
        game_type = False
        print("Welcome! [word art??] Let's start a new game!")
        input("Press enter to continue")