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
        self.player = player.Player()
        self.start_phases()
        
    #Wake up all the phases    
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
        phase3.rooms[1].npcs[0].inventory.append(end_door) #the ending door/cutscene
        
        self.phases_list = [phase1, phase2, phase3]
        
        #changing this to help with testing, should be phase 1 here for real
        phase1.start_phase()
    
        
    #if the first two words in a 3+ word command are "talk to"
    def player_npc_interaction(self, npc):
        self.player.interact_npc(npc)
        
    #if the first word in a 3+ word command is "open", "unlock", or "enter"
    def player_door_interaction(self, door):
        self.player.interact_door(door)
        
    #if the first word in a 2+ word command is "drop" or "use"
    def player_inventory_interaction(self, action, object):
        self.player.interact_inventory(action, object)
     
    #1 word commands, like help or inventory   
    def player_action(self, action):
        self.player.action(action)
        
    #2+ word command to interact with an item
    def player_item_interaction(self, action, object):
        self.player.interact_item(action, object)
        
    