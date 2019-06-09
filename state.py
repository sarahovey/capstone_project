#keep state here
import json

class State:
    def __init__(self, player, phase):
        self.name = "state"
        
    def save_game(self):
        print("saving...")
        # https://stackoverflow.com/questions/19795012/how-to-convert-a-list-to-jsonarray-in-python
        #put everythin into a file as a json object
        #player- inventory
        #game- phase
        #rooms- entered
        # with open("save_file", 'wb') as outfile:
        # for room in self.phase.rooms:
        #     #save the room and its state
        #     #room:state
            
        #         json.dump(row, outfile)
        #items- interacted with
        #npcs- met
        
    def load_game(self):
        print("load_game")
        #present 3 save slots, the player can choose the name or position of the slot to load.
        #here that save file will be retrieved and we will need to initialize
        #call the load game or new game loader
        #if player selects new game, call 
        
        #if player selects continue, read the save file