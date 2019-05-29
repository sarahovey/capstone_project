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
        #go to an item or door
        #if a door, will try to unlock it
        #if an item, then print the description
        print("go towards a landmark")
        #see if it's an item, npc, room/door
        #beeline straight to room if its in this phase
        #if its an object "what do you want to do? investigate, take?"
        #
        
    def take(self, item):
        #base action
        print("take an item")
        if "saddlebags" not in self.inventory:
            print("you don't have anything to hold that with!")
        if item.can_be_held is False:
            print("you can't pick it up")
            
        self.inventory.append(item)
        
    def help(self):
        #print help messages from xml file
        return "help messages"
        
    def check_inventory(self):
        for item in self.inventory:
            print(item.name)
            print(item.description)
            
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
            
    def interact(self, obj, action):
        print("you interacted with an object")
        #check if object is an item or npc
        #check if action is a player action
        
        print("interact with an item, is it a room, object, or npc?")
        print("return -1 if nothing can be done on the current room, some object, or npc")
        
    def save_game(self):
        print("saving")
        
    def load_game(self):
        print("loading")

        