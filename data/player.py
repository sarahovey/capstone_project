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
        else:
            print("you tried to hard...")
               
    def interact_npc(self, npc):
        for person in self.current_room:
            if person.name == npc:
                person.interact()
                
    def interact_door(self, target_door):
        for door in self.current_room.doors:
            if door.name = target_door:
                door.interact()
                
    def interact_inventory(self, action, obj):
        if action == "drop":
            #check inventory for the item to drop
            for item in self.inventory:
                if item.name == obj:
                    self.inventory.remove(item)
                    self.current_room.items.append(item)
                    print("you dropped " + obj.name)
        #use an inventory item, 
        #just print the desc if it exists
        elif action == "use":
            for item in self.inventory:
                if item.name == obj:
                    item.description()
        else:
            print("That item isn't in your inventory, you can't use or drop it!")
        
    def interact_item(self, action, obj):
        for item in self.current_room.items:
            if item.name == obj:
                if action == "take":
                    self.inventory.append(item)
                for word in item.actions:
                    if word == action:
                        item.interact()
        
    def save_game(self):
        print("saving")
        
    def load_game(self):
        print("loading")

        