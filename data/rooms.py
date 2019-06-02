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
    
#Phase 1 rooms    
class living_room(Room):
    def __init__(self, player):
        self.name = "Living Room"
        self.player = player
        self.entered = False
        self.items = []
        self.load_items()
        self.npcs = self.load_npcs()
        
    def load_items(self):
        kitchen_key = items.key("kitchen")
        couch = items.couch()
        tennis_ball = items.tennis_ball()
        blanket = items.blanket()
        water_bowl = items.water()
        kibble = items.kibble()
        
        self.items = [couch, tennis_ball, blanket, water_bowl, kibble]
        
    def load_npcs(self):
        self.npcs = []
        
    def long_description(self):
        #This builds a long description of all items and their states
        preface = "You see a "
        room_description = ""
        for item in self.items:
            room_description+= preface + item.name + ". " + item.description() + " \n"
        print(room_description)
        
    def short_description(self):
        #short description, used when you enter an already entered room
        print("You are in the living room")
        
    def enter_room(self):
        if self.entered == False:
            #show game starting text, hacky to put it here but w/e
            # print("The sun gently shines through the curtains, waking you up.")
            # print("hit enter to start playing")
            filepath = 'intro_flavor.txt' 
            with open(filepath) as fp: 
                for line in fp:
                    print(line)
                    input()
            #long description
            self.long_description()
            #set the enter flag
            self.entered = True
        #check for any conditional npcs, items, etc related to the first time entering
            #long description, etc
        
        
    def check_room_state(self):
        #this will be fleshed out later, it will be useful for rooms where npcs move around
        #and things change
        print("check to see if something is new in the room that needs to be shown to the player")
        print("for example, is there a new npc here? have we enterd this room before?")
        if not self.entered:
            self.enter_room()
        
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
    def __init__(self, connected_rooms):
        self.connected_rooms = connected_rooms
        self.items = self.load_items()
        self.npcs = self.load_npcs()
        
    def load_items(self):
        #Key to office
        #Treats!
        office_key = items.key("office")
        treat1 = items.treat()
        treat2 = items.treat()
        treat3 = items.treat()
        
        self.items = [office_key, treat1, treat2, treat3]
        
    def load_npcs(self):
        self.npcs = []
        
class office(Room):
    def __init__(self, connected_rooms):
        self.connected_rooms = connected_rooms
        self.items = self.load_items()
        self.npcs = self.load_npcs()
        
    def load_items(self):
        key_to_bedroom = items.key("bedroom")
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
<<<<<<< HEAD
class dog_park(Room):
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

class digging_pit(Room):
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
=======
class sand_pit(Room):
    def __init__(self, connected_rooms):
        self.connected_rooms = connected_rooms
        self.items = self.load_items()
        self.npcs = self.load_npcs()
    
    def load_items(self):
        shovel = items.shovel()
        bucket = items.bucket()
        sand = items.sand()
        
        self.items = [shovel, bucket, sand]
    
    def load_npcs(self):
        self.npcs = []
    
    def long_description(self):
        #This builds a long description of all items and their states
        preface = "You see a "
            room_description = ""
            for item in self.items:
                room_description+= preface + item.name + ". " + item.description() + " \n"
        print(room_description)
    
    def short_description(self):
        print("You entered the Sand Box! It is nice and soft in here")
    
    def enter_room(self):
        if self.entered == False:
            filepath = 'intro_flavor.txt'
            with open(filepath) as fp:
                for line in fp:
                    print(line)
                    input()
        
            self.long_description()
    
        self.entered = True

def check_room_state(self):

class open_grass(Room):
    def __init__(self, connected_rooms):
        self.connected_rooms = connected_rooms
        self.items = self.load_items()
        self.npcs = self.load_npcs()
    
    def load_items(self):
        frisbee = items.frisbee()
        soccer_ball = items.soccer_ball()
        tennis_ball = items.tennis_ball()
    
        self.items = [frisbee, soccer_ball, tennis_ball]
    
    def load_npcs(self):
        self.npcs = []
    
    def long_description(self):
        #This builds a long description of all items and their states
        preface = "You see a "
        room_description = ""
        for item in self.items:
            room_description+= preface + item.name + ". " + item.description() + " \n"
        print(room_description)
    
    def short_description(self):
        print("You find yourself in a big open field of grass!")
    
    def enter_room(self):
        if self.entered == False:
            filepath = 'intro_flavor.txt'
                with open(filepath) as fp:
                    for line in fp:
                        print(line)
                        input()
        
            self.long_description()
    
        self.entered = True

    def check_room_state(self):
>>>>>>> master

class agility_course(Room):
    def __init__(self, connected_rooms):
        self.connected_rooms = connected_rooms
        self.items = self.load_items()
<<<<<<< HEAD
        self.npcs = ""
        
    def load_items(self):
        saddlebags = items.saddlebags(self.player)
        bed = items.bed()
        self.items = [saddlebags, bed]
        
    def load_npcs(self):
        self.npcs = []

class doggie_pool(Room):
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
=======
        self.npcs = self.load_npcs()
    
    def load_items(self):
    #mmmm unsure what items we want here
    
    def load_npcs(self):
        self.npcs = []
    
    def long_description(self):
        #This builds a long description of all items and their states
        preface = "You see a "
        room_description = ""
        for item in self.items:
            room_description+= preface + item.name + ". " + item.description() + " \n"
        print(room_description)
    
    def short_description(self):
        print("You are at the agility course!")
    
    def enter_room(self):
        if self.entered == False:
            filepath = 'intro_flavor.txt'
                with open(filepath) as fp:
                    for line in fp:
                        print(line)
                        input()
        
            self.long_description()
    
        self.entered = True

def check_room_state(self):

class dog_pool(Room):
    def __init__(self, connected_rooms):
        self.connected_rooms = connected_rooms
        self.items = self.load_items()
        self.npcs = self.load_npcs()
    
    def load_items(self):
        floaty = items.floaty()
        swim_goggles = items.swim_goggles()
        snorkle = items.snorkle()
        beach_ball = items.beach_ball()
    
        self.items = [floaty, swim_goggles, snorkle, beach_ball]
    
    def load_npcs(self):
        self.npcs = []
    
    def long_description(self):
        #This builds a long description of all items and their states
        preface = "You see a "
        room_description = ""
        for item in self.items:
            room_description+= preface + item.name + ". " + item.description() + " \n"
        print(room_description)
    
    def short_description(self):
        print("You find yourself at the edge of the dog pool. Good thing you know how to swim.")
    
    def enter_room(self):
        if self.entered == False:
            filepath = 'intro_flavor.txt'
                with open(filepath) as fp:
                    for line in fp:
                        print(line)
                        input()
        
            self.long_description()
    
        self.entered = True

def check_room_state(self):
>>>>>>> master
