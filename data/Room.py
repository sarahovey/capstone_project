#Room parent class

class Room:
    def __init__(self, name, connected_rooms, items, npcs, actions, player):
        self.name = "Parent"
        self.connected_rooms = []
        self.items = []
        self.npcs = []
        self.actions = ["load", "look at", "go", "take", "help", "inventory","save", "load"]
        
    #Actions for all rooms
    def look(self):
        #description of all things in the room
        print("description placeholder")
        
    def look_at(self, item):
        print("description of an item")
        
    def go(self, room):
        #base action, will add more in subclass
        print("go towards a landmark")
        
    def take(self, item):
        #base action
        print("take an item")
        
    def help(self):
        #print help messages from xml file
        print("help messages")
        
    def inventory(self, player):
        #call function on player to list inventory
        player.inventory()
        