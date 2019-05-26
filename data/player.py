import rooms
class Player:
    def __init__(self):
        self.name = "player"
        self.inventory = []
        #self.active_inventory = isActive()
        self.current_room = rooms.living_room
        
    # def isActive(self):
    #     if "saddlebags" in self.inventory:
    #         self.active_inventory = True
    #     else:
    #         self.active_inventory = False
   
    # def find_saddlebags(self):
    #     #player can start adding to their inventory 
    #     self.active_inventory = True
        
    def change_room(self, new_room):
        self.current_room = new_room
        
        
    def interact(self):
        print("interact with an item, is it a room, object, or npc?")
        print("return -1 if nothing can be done on the current room, some object, or npc")
        