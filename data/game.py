#Use this class as an API
#to take a player action: game.player_action(action)
#to interact with an item/npc: game.player)interaction(object)
import phase
import player

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
        
    def player_interaction(self, obj):
        self.player.interact(object, )
        
    def load_game(self):
        return "unpickled save file"
        
    def new_game(self):
        return "new game"
    
    