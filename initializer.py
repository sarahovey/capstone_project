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
        
    #start up the parser
    def start_parser(self):
        print("starting parser, return an instance")

    #display start screen
    def start_screen(self):
        game_type = False
        print("""
  ____    _  _____ _____ _     _____   ____   ___   ____ 
 / ___|  / \|_   _|_   _| |   | ____| |  _ \ / _ \ / ___|
| |     / _ \ | |   | | | |   |  _|   | | | | | | | |  _ 
| |___ / ___ \| |   | | | |___| |___  | |_| | |_| | |_| |
 \____/_/   \_\_|   |_| |_____|_____| |____/ \___/ \____|
                                                         
    _    ______     _______ _   _ _____ _   _ ____  _____ 
   / \  |  _ \ \   / / ____| \ | |_   _| | | |  _ \| ____|
  / _ \ | | | \ \ / /|  _| |  \| | | | | | | | |_) |  _|  
 / ___ \| |_| |\ V / | |___| |\  | | | | |_| |  _ <| |___ 
/_/   \_\____/  \_/  |_____|_| \_| |_|  \___/|_| \_\_____|
                                                          
                  Let's start a new game!
            """)
        input("Press enter to continue")