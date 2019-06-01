#Use this class as an API
#to take a player action: game.player_action(action)
#to interact with an item/npc: game.player)interaction(object)
import phase
import player
import pickle 

class Game:
    def __init__(self):
        self.phases_list = []
        self.player = ""
        
        self.player = player.Player()
        
    def start_phases(self):
        phase1 = phase.Phase1()
        
        self.phases_list = [phase1]
        
    def player_action(self, action):
        self.player.action(action)
        
    def player_interaction(self, obj, action):
        self.player.interact(object, action)
        
    def load_game(self):
        print("are you sure?") #need to find a way to only show this if its being loaded from an in-progress game
        file_name = "saved_game/save_file"
        fp = open(file_name, "r")
        
        #unpickle
        pickle.load(fp)
        
        fp.close
        
    def save_game(self):
        file_name = "saved_game/save_file"
        fp = open(file_name, "w")
        print("saving game...")
        pickle.dump(self, file_name)
        fp.close()
        
    def new_game(self):
        return "new game"
        #start a new phase
        
    
    