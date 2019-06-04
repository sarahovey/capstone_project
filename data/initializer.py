import phase
import game

class initializer:
    #how to use:
    #initialize, start parser and start screen will be automatically called
    #validate 1/2 input
    #call load_game with that input, this will return an instance of the current phase / state of the game
    def __init__(self):
        # self.parser = 1
        # self.current_phase = 1
        self.start_screen()
        self.game = game.Game()
        print("done making the game in initializer")
        
    #start up the parser
    def start_parser(self):
        print("starting parser, return an instance")

    #display start screen
    def start_screen(self):
        game_type = False
        print("Welcome! [word art??] Let's start a new game!")
        input("Press enter to continue")
        # print("Press 1 for new game, 2 for saved game")
        # while game_type is False:
        #     choice = input()
        #     if choice == "1":
        #         #current_phase = self.load_game(choice)
        #         self.load_game(choice)
        #         game_type == True
        #         break
        #     elif choice == "2":
        #         print("No game to load, try starting a new one")
        #         break
        #     else:
        #         print("try again")
        #         break

#wait for input
    # def load_game(self, input):
    #     # if input == "1":
    #     #     print("Starting new game...")
    #     #     self.game.start_phases()
    #     # elif input == "2":
    #     #     print("Loading coming soon... try starting a new game")
    #     # else:
    #     #     print("unknown game load type")
        
    #     print("load game from initializer")
    #     self.game.start_phases()

#load game function
#take input from 
#engine should call initializer.load(input) #can only be new or continue