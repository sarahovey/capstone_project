#Use this class as an API
#to take a player action: game.player_action(action)
#to interact with an item/npc: game.player)interaction(object)
import phase
import player
import pickle 
import items 

class Game:
    def __init__(self):
        self.phases_list = []
        self.player = ""
        
        self.player = player.Player()
        self.start_phases()
        
    def start_phases(self):
        phase1 = phase.Phase1(self.player)
        phase2 = phase.Phase2(self.player)
        phase3 = phase.Phase3(self.player)
        
        #set up the phase doors
        message1 = "Are you sure you want to go out the front door?"
        front_door_description = "The front door.... outside lies.... the whole world!"
        front_door = items.phase_door(self.player, phase2, message1, "front door", front_door_description)
        phase1.spawn_point.doors.append(front_door)
        
        message2 = "Do you want to use the map to go to your human's office?"
        map_description = "a map to your human's office"
        map_door  = items.phase_door(self.player, phase3, message2, "map", map_description)
    
        phase2.rooms[3].npcs[0].inventory[0].phase_door = map_door #this is so janky im sorry
        
        #this door just triggers the end cutscene
        message3 = "Are you ready to see your human?"
        end_description = "time to see your human!"
        end_door = items.phase_door(self.player, None, message3, "the end", end_description)
        phase3.rooms[1].npcs[0].inventory.append(end_door)
        
        self.phases_list = [phase1, phase2, phase3]
        
        phase1.start_phase()
        
    def player_action(self, action):
        self.player.action(action)
        
    def player_interaction(self, obj, action):
        self.player.interact(object, action)
        
    def load_game(self):
        print("Not yet!")
        # print("are you sure?") #need to find a way to only show this if its being loaded from an in-progress game
        # file_name = "saved_game/save_file"
        # fp = open(file_name, "r")
        
        # #unpickle
        # pickle.load(fp)
        
        # fp.close
        
    # def save_game(self):
    #     print("Coming soon!")
    #     # file_name = "saved_game/save_file"
    #     # fp = open(file_name, "w")
    #     # print("saving game...")
    #     # pickle.dump(self, file_name)
    #     # fp.close()
        
    # def new_game(self):
    #     return "new game"
    #     self.phases_list[0].start_phase(self.player)
    #     #start a new phase
        
    
    