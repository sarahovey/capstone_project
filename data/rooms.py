import items
import npcs

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
        self.doors = []
        self.original_room = True #denotes position in hub and spoke network of rooms in each phase
        
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
            
        for npc in self.npcs:
            room_description+= preface + npc.name + ". " + npc.npc_description() + " \n"
            
        room_description += "You also see \n"
        for door in self.doors:
            room_description += "a door to " + door.to_room + " \n"
            
        print(room_description)
        
    def short_description(self):
        #short description, used when you enter an already entered room
        print("You are in the living room")
        
    def enter_room(self):
        if self.entered == False:
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
    def __init__(self):
        self.items = self.load_items()
        self.npcs = self.load_npcs()
        self.entered = False
        self.doors = []
        self.original_room = False
        
    def load_items(self):
        hose = items.hose()
        pool = items.kiddie_pool()
        tug_rope = items.tug_rope()
        herding_ball = items.herding_ball()
        self.items = [hose, pool, tug_rope, herding_ball]
        
    def load_npcs(self):
        self.npcs = []
        
    def long_description(self):
        #This builds a long description of all items and their states
        preface = "You see a "
        room_description = ""
        for item in self.items:
            room_description+= preface + item.name + ". " + item.description() + " \n"
        for npc in self.npcs:
            room_description+= preface + npc.name + ". " + npc.npc_description() + " \n"
            
        room_description += "You also see \n"
        for door in self.doors:
            room_description += "a door to " + door.from_room + " \n"
        print(room_description)
        
    def short_description(self):
        print("you are in the back yard")
        
    def enter_room(self):
        if self.entered:
            self.short_description()
        else:
            self.long_description()
            self.entered = True
        
class kitchen(Room):
    def __init__(self):
        self.items = self.load_items()
        self.npcs = self.load_npcs()
        self.entered = False
        self.doors = []
        self.original_room = False
        
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
        
    def long_description(self):
        #This builds a long description of all items and their states
        preface = "You see a "
        room_description = ""
        for item in self.items:
            room_description+= preface + item.name + ". " + item.description() + " \n"
        for npc in self.npcs:
            room_description+= preface + npc.name + ". " + npc.npc_description() + " \n"
            
        room_description += "You also see \n"
        for door in self.doors:
            room_description += "a door to " + door.from_room + " \n"
            
        print(room_description)
        
    def short_description(self):
        print("you are in the kitchen")
        
    def enter_room(self):
        if self.entered:
            self.short_description()
        else:
            self.long_description()
            self.entered = True
        
class office(Room):
    def __init__(self):
        self.items = self.load_items()
        self.npcs = self.load_npcs()
        self.entered = False
        self.doors = []
        self.original_room = False
        
    def load_items(self):
        key_to_bedroom = items.key("bedroom")
        bookshelf = items.book_shelf()
        trashcan = items.trash_can()
        self.items = [key_to_bedroom, bookshelf, trashcan]
        
    def load_npcs(self):
        self.npcs = []
        
    def long_description(self):
        #This builds a long description of all items and their states
        preface = "You see a "
        room_description = ""
        for item in self.items:
            room_description+= preface + item.name + ". " + item.description() + " \n"
        for npc in self.npcs:
            room_description+= preface + npc.name + ". " + npc.npc_description() + " \n"
            
        room_description += "You also see \n"
        for door in self.doors:
            room_description += "a door to " + door.from_room + " \n"
            
        print(room_description)
        
    def short_description(self):
        print("you are in the office")
        
    def enter_room(self):
        if self.entered:
            self.short_description()
        else:
            self.long_description()
            self.entered = True
        
class bedroom(Room):
    def __init__(self):
        self.items = self.load_items()
        self.npcs = ""
        self.entered = False
        self.doors = []
        self.original_room = False
        
    def load_items(self):
        saddlebags = items.saddlebags(self.player)
        bed = items.bed()
        self.items = [saddlebags, bed]
        
    def load_npcs(self):
        self.npcs = []
        
    def long_description(self):
        #This builds a long description of all items and their states
        preface = "You see a "
        room_description = ""
        for item in self.items:
            room_description+= preface + item.name + ". " + item.description() + " \n"
        for npc in self.npcs:
            room_description+= preface + npc.name + ". " + npc.npc_description() + " \n"
            
        room_description += "You also see \n"
        for door in self.doors:
            room_description += "a door to " + door.from_room + " \n"
            
        print(room_description)
        
    def short_description(self):
        print("you are in the bedroom")
        
    def enter_room(self):
        if self.entered:
            self.short_description()
        else:
            self.long_description()
            self.entered = True
        
#Phase 2 rooms
class sand_pit(Room):
    def __init__(self):
        self.items = self.load_items()
        self.npcs = self.load_npcs()
        self.entered = False
        self.original_room = True
        self.gates = []
    
    def load_items(self):
        shovel = items.shovel()
        bucket = items.bucket()
        
        self.items = [shovel, bucket]
    
    def load_npcs(self):
        self.npcs = []
    
    def long_description(self):
        #This builds a long description of all items and their states
        preface = "You see a "
        room_description = ""
        for item in self.items:
            room_description+= preface + item.name + ". " + item.description() + " \n"
        for npc in self.npcs:
            room_description+= preface + npc.name + ". " + npc.npc_description() + " \n"
            
        room_description += "You also see \n"
        for gate in self.gates:
            room_description += "a gate to " + gate.from_room + " \n"
            
        print(room_description)
    
    def short_description(self):
        print("You entered the Sand Box! It is nice and soft in here")
    
    def enter_room(self):
        if self.entered:
            self.short_description()
        else:
            self.long_description()
            self.entered = True

class open_grass(Room):
    def __init__(self):
        self.items = self.load_items()
        self.npcs = self.load_npcs()
        self.entered = False
        self.original_room = False
        self.gates = []
    
    def load_items(self):
        frisbee = items.frisbee()
        soccer_ball = items.soccer_ball()
        tennis_ball = items.tennis_ball()
        squeaky_toy = items.squeaky_toy()
        stick = items.stick()
    
        self.items = [frisbee, soccer_ball, tennis_ball, squeaky_toy, stick]
    
    def load_npcs(self):
        self.npcs = []
        
    def long_description(self):
        #This builds a long description of all items and their states
        preface = "You see a "
        room_description = ""
        for item in self.items:
            room_description+= preface + item.name + ". " + item.description() + " \n"
        for npc in self.npcs:
            room_description+= preface + npc.name + ". " + npc.npc_description() + " \n"
            
        room_description += "You also see \n"
        for gate in self.gates:
            room_description += "a gate to " + gate.to_room + " \n"
            
        print(room_description)
    
    def short_description(self):
        print("You find yourself in a big open field of grass!")
    
    def enter_room(self):
        if self.entered:
            self.short_description()
        else:
            self.long_description()
            self.entered = True

class agility_course(Room):
    def __init__(self):
        self.items = self.load_items()
        self.npcs = self.load_npcs()
        self.entered = False
        self.original_room = False
        self.gates = []
    
    def load_items(self):
        water_bowl = items.water()
        kibbles = items.kibble()
        self.items = [water_bowl, kibbles]
        
    def load_npcs(self):
        rusty = npcs.rusty()
        self.npcs = [rusty]
    
    def long_description(self):
        #This builds a long description of all items and their states
        preface = "You see a "
        room_description = ""
        for item in self.items:
            room_description+= preface + item.name + ". " + item.description() + " \n"
        for npc in self.npcs:
            room_description+= preface + npc.name + ". " + npc.npc_description() + " \n"
            
        room_description += "You also see \n"
        for gate in self.gates:
            room_description += "a gate to " + gate.from_room + " \n"
            
        print(room_description)
    
    def short_description(self):
        print("You are at the agility course!")
    
    def enter_room(self):
        if self.entered:
            self.short_description()
        else:
            self.long_description()
            self.entered = True
class dog_pool(Room):
    def __init__(self):
        self.items = self.load_items()
        self.npcs = self.load_npcs()
        self.entered = False
        self.original_room = False
        self.gates = []
    
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
        for npc in self.npcs:
            room_description+= preface + npc.name + ". " + npc.npc_description() + " \n"
        room_description += "You also see \n"
        for gate in self.gates:
            room_description += "a gate to " + gate.from_room + " \n"
        print(room_description)
    
    def short_description(self):
        print("You find yourself at the edge of the dog pool. Good thing you know how to swim.")
    
    def enter_room(self):
        if self.entered:
            self.short_description()
        else:
            self.long_description()
            self.entered = True
            
class shady_grove(Room):
    def __init__(self):
        self.items = self.load_items()
        self.npcs = self.load_npcs()
        self.entered = False
        self.original_room = False
        self.gates = []
    
    def load_items(self):
        stick = items.stick()
        tennis_ball = items.tennis_ball()
        water = items.water()
        
        self.items = [stick, water, tennis_ball]
    
    def load_npcs(self):
        self.npcs = []
    
    def long_description(self):
        #This builds a long description of all items and their states
        preface = "You see a "
        room_description = ""
        for item in self.items:
            room_description+= preface + item.name + ". " + item.description() + " \n"
            
        for npc in self.npcs:
            room_description+= preface + npc.name + ". " + npc.npc_description() + " \n"
            
        room_description += "You also see \n"
        for gate in self.gates:
            room_description += "a gate to " + gate.from_room + " \n"
        print(room_description)
    
    def short_description(self):
        print("You find yourself at the edge of the dog pool. Good thing you know how to swim.")
    
    def enter_room(self):
        if self.entered:
            self.short_description()
        else:
            self.long_description()
            self.entered = True

#Phase 3 Rooms
class lobby(Room):
    def __init__(self):
        self.items = self.load_items()
        self.npcs = self.load_npcs()
        self.entered = False
        self.original_room = True
        self.doors = []

    def load_items(self):
        plant = items.plant()
        chair = items.chair()
        magazine = items.magazine()

        self.items = [plant, chair, magazine]

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
            print("You stumble upon the entrance of an office. Maybe your owner is here!")

    def enter_room(self):
        if self.entered:
            self.short_description()
        else:
            self.long_description()
            self.entered = True

class break_room(Room):
    def __init__(self):
        self.items = self.load_items()
        self.npcs = self.load_npcs()
        self.entered = False
        self.original_room = False
        self.doors = []

    def load_items(self):
        snacks = items.snacks()
        table = items.table()
        water_cooler = items.water_cooler()
        
        self.items = [snacks, table, water_cooler]

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
        print("This looks like the breakroom, the perfect place to find snacks lying around.")
    
    def enter_room(self):
        if self.entered:
            self.short_description()
        else:
            self.long_description()
            self.entered = True

class supply_closet(Room):
    def __init__(self):
        self.items = self.load_items()
        self.npcs = self.load_npcs()
        self.entered = False
        self.original_room = False
        self.doors = []
    
    def load_items(self):
        vacuum = items.vacuum()
        spray_bottle = items.spray_bottle()
        office_supplies = items.office_supplies()
        
        self.items = [vacuum, spray_bottle, office_supplies]
    
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
        print("You stumble upon the supply closet. Everything useful is stored here.")
    
    def enter_room(self):
        if self.entered:
            self.short_description()
        else:
            self.long_description()
            self.entered = True

class common_area(Room):
    def __init__(self):
        self.items = self.load_items()
        self.npcs = self.load_npcs()
        self.entered = False
        self.original_room = False
        self.doors = []
    
    def load_items(self):
        plant = items.plant()
        chair = items.chair()
        magazine = items.magazine()
        couch = items.couch()
        
        self.items = [plant, chair, magazine, couch]
    
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
        print("You find yourself in the lobby. It's quiet... too quiet.")
    
    def enter_room(self):
        if self.entered:
            self.short_description()
        else:
            self.long_description()
            self.entered = True

class cubicle(Room):
    def __init__(self):
        self.items = self.load_items()
        self.npcs = self.load_npcs()
        self.entered = False
        self.original_room = False
        self.doors = []
    
    def load_items(self):
        computer = items.computer()
        trash_can = items.trash_can()
        office_chair = items.office_chair()
        notebook = items.notebook()
        
        self.items = [computer, trash_can, office_chair, notebook]
    
    def load_npcs(self):
        coworker = npcs.coworker()
        self.npcs = [coworker]
    
    def long_description(self):
        #This builds a long description of all items and their states
        preface = "You see a "
        room_description = ""
        for item in self.items:
            room_description+= preface + item.name + ". " + item.description() + " \n"
        print(room_description)
    
    def short_description(self):
        print("You stumble upon the supply closet. Everything useful is stored here.")
    
    def enter_room(self):
        if self.entered:
            self.short_description()
        else:
            self.long_description()
            self.entered = True
