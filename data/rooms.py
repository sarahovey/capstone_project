import items

#Room parent class
class Room:
    def __init__(self, player):
        self.name = "Parent"
        self.connected_rooms = []
        self.items = []
        self.npcs = []
        self.actions = ["load", "look at", "go", "take", "help", "inventory","save", "load"]
        self.entered = False
        self.player = player
        
    #Actions for all rooms
    def look(self):
        #description of all things in the room
        print("You look around")
        
    def look_at(self, item):
        print("description of an item")
        
    def go(self, room):
        #base action, will add more in subclass
        print("go towards a landmark")
        
    def take(self, item):
        #base action
        print("take an item")
        if self.player.saddlebags is False:
            print("you don't have anything to hold that with!")
        
    def help(self):
        #print help messages from xml file
        print("help messages")
        
    def inventory(self, player):
        #call function on player to list inventory
        player.inventory()
        
    def save(self, player):
        print("saving the game...")
        
    
#Phase 1 rooms    
class living_room(Room):
    def __init__(self):
        self.name = "Living Room"
        self.connected_rooms = self.load_connected_rooms()
        self.items = self.load_items()
        self.npcs = self.load_npcs()
            
        self.load_items()
        self.load_connected_rooms()
        
    def load_connected_rooms(self):
        #for now putting the spawning room in charge of loading all other rooms on the map
        #also passing in what rooms those rooms are connected to
        #and what room a key contained within unlocks
        #gotta be a cleaner way to make this graph, its a damn mess
        
        back_yard = back_yard([self])
        bedroom = bedroom([self], )
        kitchen = kitchen([self], office)
        office = office([self], bedroom)
        self.connected_rooms = [kitchen, back_yard, office, bedroom]
        
    def load_items(self):
        kitchen_key = items.key(kitchen)
        couch = items.couch()
        tennis_ball = items.tennis_ball()
        blanket = items.blanket()
        water_bowl = items.water()
        kibble = items.kibble()
        
        self.items = [kitchen_key, couch, tennis_ball, blanket, water_bowl, kibble]
        
    def load_npcs(self):
        self.npcs = []
        
    def long_description(self):
        #build a description
        #return the string to look(), or enter()
        #you are in [room name], for x in items you see a [item] that is [state]
        print("Long description")
        
    def short_description(self):
        #short description, used when you enter an already entered room
        print("You are in the living room")
        
    def enter_room(self):
        #set the enter flag
        self.entered = True
        #check for any conditional npcs, items, etc
        
        print("you entered room")
        
class back_yard(Room):
    def __init__(self, connected_rooms):
        self.connected_rooms = connected_rooms
        self.items = self.load_items()
        self.npcs = self.load_npcs()

    def load_items(self):
        hose = items.hose()
        pool = items.kiddie_pool()
        tug_rope = items.tug_rope()
        herding_ball = items.herding_ball()
        self.items = [hose, pool, tug_rope, herding_ball]
        
    def load_npcs(self):
        self.npcs = []
        
class kitchen(Room):
    def __init__(self, connected_rooms, key_room):
        self.connected_rooms = connected_rooms
        self.items = self.load_items()
        self.npcs = self.load_npcs()
        self.key_room = key_room #room that the key in here unlocks
        
    def load_items(self):
        #Key to office
        #Treats!
        office_key = items.key(self.key_room)
        treat1 = items.treat()
        treat2 = items.treat()
        treat3 = items.treat()
        
        self.items = [office_key, treat1, treat2, treat3]
        
    def load_npcs(self):
        self.npcs = []
        
class office(Room):
    def __init__(self, connected_rooms, key_room):
        self.connected_rooms = connected_rooms
        self.items = self.load_items()
        self.npcs = self.load_npcs()
        
    def load_items(self):
        key_to_bedroom = items.key("front door")
        bookshelf = items.book_shelf()
        trashcan = items.trash_can()
        self.items = [key_to_bedroom, bookshelf, trashcan]
        
    def load_npcs(self):
        self.npcs = []
        
class bedroom(Room):
    def __init__(self, connected_rooms):
        self.connected_rooms = connected_rooms
        self.items = self.load_items()
        self.npcs = ""
        
    def load_items(self):
        saddlebags = items.saddlebags(self.player)
        bed = items.bed()
        self.items = [saddlebags, bed]
        
    def load_npcs(self):
        self.npcs = []
        
#Phase 2 rooms