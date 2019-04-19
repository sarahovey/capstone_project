#Item parent class

class Item:
    def __init__(self, name, connected_Items, items, npcs, actions, player):
        self.name = "Parent"
        self.items = []
        self.actions = ["look at", "use", "help", "inventory"]
        
    #Actions for all Items        
    def look_at(self, item):
        print("description of an item")
        
    def use(self, Item):
        #base action, will add more in subclass
        print("use this item")
        
    def take(self, item):
        #base action
        print("take an item")
        
    def help(self):
        #print help messages from xml file
        print("help + item name gives you a hint")
        
    def inventory(self, player):
        #call function on player to list inventory
        player.inventory()
        