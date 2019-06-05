import rooms
class Player:
    def __init__(self):
        self.name = "player"
        self.inventory = []
        self.current_room = rooms.living_room
        self.actions = ["look around", "take"]
        
    def look_around(self):
        self.current_room.long_description()
        
    def look_at(self, item):
        item.description()
        
    def go(self, landmark):
        if landmark.name == "door" or landmark.name == "gate":
            landmark.change_room()
        else:
            landmark.description()
        
    def take(self, item):
        # if "saddlebags" not in self.inventory:
        #     print("you don't have anything to hold that with!")
        if item.can_be_held is False:
            print("you can't pick it up")
            
        self.inventory.append(item)
        
    def doors(self):
        print("You are in " + self.current_room)
        for door in self.current_room:
            print("There is a door between " + door.from_room + " and " + door.to_room + "\n")
        
    def help(self):
        #print help messages from xml file
        return "help messages"
        
    def check_inventory(self):
        for item in self.inventory:
            print(item.name)
            print(item.description)
            
    #Get a list of item names (strings) to see if the player has one or mroe in inventory
    def find_item(self, items):
        for item in self.inventory:
            if item.name in items:
                return True
            else:
                return False
            
    def save(self, player):
        print("saving the game...")
        
    def change_room(self, new_room):
        self.current_room = new_room
        self.current_room.long_description()
        
    def action(self, action):
        print("you took an action")
        #should refactor this to define a list of synonyms for each player action
        if action == "look":
            self.look_around()
        elif action == "inventory":
            print("")
        elif action == "help" :
            print("some help messages")
            
            
    def check_if_item(self, object):
        target
        for item in current_room.items:
            if item.name == object:
                target = item
                
        return target
                
    def check_if_npc(self, object):
        target
        for npc in current_room.npcs:
            if npc.name == object:
                target = npc
        return target
                
    def interact(self, action, object):
        target = self.check_if_item()
        if target is None:
            target = self.check_if_npc()
        if target is None:
            print("I didn't understand what you wanted to do")
            
        target.interact()
            
        
        
        
        
            
        
        
        print("interact with an item, is it a room, object, or npc?")
        print("return -1 if nothing can be done on the current room, some object, or npc")
        
    def save_game(self):
        print("saving")
        
    def load_game(self):
        print("loading")

        