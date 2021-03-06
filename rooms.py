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
        self.name = "living room"
        self.player = player
        self.entered = False
        self.items = []
        self.load_items()
        self.npcs = []
        self.load_npcs()
        self.doors = []
        self.original_room = True #denotes position in hub and spoke network of rooms in each phase
        
    def load_items(self):
        kitchen_key = items.key("kitchen key")
        couch = items.couch()
        tennis_ball = items.tennis_ball()
        blanket = items.blanket()
        water_bowl = items.water()
        kibble = items.kibble()
        
        self.items = [couch, tennis_ball, blanket, water_bowl, kibble, kitchen_key]
        
    def load_npcs(self):
        self.npcs = []
        
    def long_description(self):
        print("You are in the " + self.name)
        print("This is home. A cozy zone")
        print("You see...")
        for item in self.items:
            print("\t- " + item.name + ". " + str(item.description()))
            
        print("You also see...")
            
        for door in self.doors:
            if door.name == "front door":
                print("\t- the front door, outside it lies the whole world!!")
            else:
                print("\t- a door to the " + door.to_room.name)
        
    def short_description(self):
        #short description, used when you enter an already entered room
        print("You are back in the living room")
        print("You see...")
        for door in self.doors:
            print("\t- a door to the " + door.to_room.name)
        
    def enter_room(self):
        if self.entered:
            self.short_description()
        else:
            self.long_description()
            self.entered = True

class back_yard(Room):
    def __init__(self, player):
        self.name = "back yard"
        self.items = []
        self.load_items()
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
        print("You are in the " + self.name)
        print("You love spending time playing in the yard")
        print("You see...")
        for item in self.items:
            print("\t- " + item.name + ". " + str(item.description()))
            
        print("You also see...")
            
        for door in self.doors:
            print("\t- a door to the " + door.from_room.name)
        
    def short_description(self):
        print("you are back in the back yard")
        print("You see...")
        for door in self.doors:
            print("\t- a door to the " + door.from_room.name)
        
    def enter_room(self):
        if self.entered:
            self.short_description()
        else:
            self.long_description()
            self.entered = True
        
class kitchen(Room):
    def __init__(self, player):
        self.name = "kitchen"
        self.items = []
        self.load_items()
        self.npcs = self.load_npcs()
        self.entered = False
        self.doors = []
        self.original_room = False
        
    def load_items(self):
        office_key = items.key("office key")
        treat1 = items.treat()
        treat2 = items.treat()
        treat3 = items.treat()
        
        self.items = [office_key, treat1, treat2, treat3]
        
    def load_npcs(self):
        self.npcs = []
        
    def long_description(self):
        print("You are in the " + self.name)
        print("Your human always makes yummy food in here")
        print("You see...")
        for item in self.items:
            print("\t- " + item.name + ". " + str(item.description()))
            
        print("You also see...")
            
        for door in self.doors:
            print("\t- a door to the " + door.from_room.name)
            
        #print(room_description)
        
    def short_description(self):
        print("you are back in the kitchen")
        print("You see...")
        for door in self.doors:
            print("\t- a door to the " + door.from_room.name)
        
    def enter_room(self):
        if self.entered:
            self.short_description()
        else:
            self.long_description()
            self.entered = True
        
class office(Room):
    def __init__(self, player):
        self.name = "office"
        self.items = []
        self.load_items()
        self.npcs = [] 
        self.load_npcs()
        self.entered = False
        self.doors = []
        self.original_room = False
        
    def load_items(self):
        key_to_bedroom = items.key("bedroom key")
        bookshelf = items.book_shelf()
        trashcan = items.trash_can()
        self.items = [key_to_bedroom, bookshelf, trashcan]
        
    def load_npcs(self):
        self.npcs = []
        
    def long_description(self):
        print("You are in the " + self.name)
        print("This is where the human gets work done")
        print("You see...")
        for item in self.items:
            print("\t- " + item.name + ". " + str(item.description()))
            
        print("You also see...")
            
        for door in self.doors:
            print("\t- a door to the " + door.from_room.name)
        
    def short_description(self):
        print("you are back in the office")
        print("You see...")
        for door in self.doors:
            print("\t- a door to the " + door.from_room.name)
        
    def enter_room(self):
        if self.entered:
            self.short_description()
        else:
            self.long_description()
            self.entered = True
        
class bedroom(Room):
    def __init__(self, player):
        self.name = "bedroom"
        self.items = []
        self.load_items()
        self.npcs = ""
        self.entered = False
        self.doors = []
        self.original_room = False
        
    def load_items(self):
        #saddlebags = items.saddlebags(self.player)
        bed = items.bed()
        key_to_frontdoor = items.key("front door key")
        self.items = [bed, key_to_frontdoor]
        
    def load_npcs(self):
        self.npcs = []
        
    def long_description(self):
        print("You are in the " + self.name)
        print("You always get to sleep in the bed")
        print("You see...")
        for item in self.items:
            print("\t- " + item.name + ". " + str(item.description()))
            
        print("You also see...")
            
        for door in self.doors:
            print("\t- a door to the " + door.from_room.name)
        
    def short_description(self):
        print("you are back in the bedroom")
        print("You see...")
        for door in self.doors:
            print("\t- a door to the " + door.from_room.name)
        
    def enter_room(self):
        if self.entered:
            self.short_description()
        else:
            self.long_description()
            self.entered = True
        
#Phase 2 rooms
class sand_pit(Room):
    def __init__(self, player):
        self.name = "sand pit"
        self.items = []
        self.load_items()
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
        print("You are in the " + self.name)
        print("This seems like a good spot to dig a hole!")
        print("You see...")
        for item in self.items:
            print("\t- " + item.name + ". " + str(item.description()))
            
        print("You also see...")
            
        for gate in self.gates:
            print("\t- a door to the " + gate.from_room.name)
        
    
    def short_description(self):
        print("You are back in the sand pit")
        print("You see...")
        for gate in self.gates:
            print("\t- a door to the " + gate.from_room.name)
    
    def enter_room(self):
        if self.entered:
            self.short_description()
        else:
            self.long_description()
            self.entered = True

class open_grass(Room):
    def __init__(self, player):
        self.name = "open grass"
        self.items = []
        self.load_items()
        self.npcs = []
        self.load_npcs()
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
        print("You are in the " + self.name)
        print("It's a big grassy field that's nice and soft on your paws")
        print("You see...")
        for item in self.items:
            print("\t- " + item.name + ". " + str(item.description()))
            
        print("You also see...")
            
        for gate in self.gates:
            print("\t- a door to the " + gate.to_room.name)
    
    def short_description(self):
        print("You are back in the open grassy field")
        print("You see...")
        for gate in self.gates:
            print("\t- a door to the " + gate.to_room.name)
    
    def enter_room(self):
        if self.entered:
            self.short_description()
        else:
            self.long_description()
            self.entered = True

class agility_course(Room):
    def __init__(self, player):
        self.name = "agility course"
        self.items = []
        self.player = player
        self.load_items()
        self.npcs = []
        self.load_npcs()
        self.entered = False
        self.original_room = False
        self.gates = []
    
    def load_items(self):
        water_bowl = items.water()
        kibbles = items.kibble()
        self.items = [water_bowl, kibbles]
        
    def load_npcs(self):
        rusty = npcs.rusty(self.player)
        rusty.inventory.append(items.map())
        self.npcs = [rusty]
        
    
    def long_description(self):
        print("You are in the " + self.name)
        print("You see lots of equipment to do agility training")
        print("You see...")
        for item in self.items:
            print("\t- " + item.name + ". " + str(item.description()))
            
        for npc in self.npcs:
               print("\t- " + npc.name + ". " + str(npc.description()))
            
        print("You also see...")
            
        for gate in self.gates:
            print("\t- a door to the " + gate.from_room.name)
    
    def short_description(self):
        print("You are back in the agility course!")
        print("You see...")
        for gate in self.gates:
            print("\t- a door to the " + gate.from_room.name)
    
    def enter_room(self):
        if self.entered:
            self.short_description()
        else:
            self.long_description()
            self.entered = True

class dog_pool(Room):
    def __init__(self, player):
        self.name = "dog pool"
        self.items = []
        self.load_items()
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
        print("You are in the " + self.name)
        print("There is a huge swimming pool for you to padle around in")
        print("You see...")
        for item in self.items:
            print("\t- " + item.name + ". " + str(item.description()))
            
        print("You also see...")
            
        for gate in self.gates:
            print("\t- a door to the " + gate.from_room.name)
    
    def short_description(self):
        print("You are back in the dog pool!")
        
        print("You see...")
        for gate in self.gates:
            print("\t- a door to the " + gate.from_room.name)
    
    def enter_room(self):
        if self.entered:
            self.short_description()
        else:
            self.long_description()
            self.entered = True
            
class shady_grove(Room):
    def __init__(self, player):
        self.name = "shady grove"
        self.items = []
        self.load_items()
        self.npcs = []
        self.load_npcs()
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
        print("You are in the " + self.name)
        print("More grassy area, this time covered by big shady trees")
        print("You see...")
        for item in self.items:
            print("\t- " + item.name + ". " + str(item.description()))
            
        print("You also see...")
            
        for gate in self.gates:
            print("\t- a door to the " + gate.from_room.name)
    
    def short_description(self):
        print("You are back in the shady grove")
        print("You see...")
        for gate in self.gates:
            print("\t- a door to the " + gate.from_room.name)
        
    
    def enter_room(self):
        if self.entered:
            self.short_description()
        else:
            self.long_description()
            self.entered = True

#Phase 3 Rooms
class lobby(Room):
    def __init__(self, player):
        self.name = "lobby"
        self.items = []
        self.load_items()
        self.npcs = []
        self.load_npcs()
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
        print("You are in the " + self.name)
        print("This is the entrance to the office building that the map sent you to")
        print("You see...")
        for item in self.items:
            print("\t- " + item.name + ". " + str(item.description()))
            
        print("You also see...")
            
        for door in self.doors:
            print("\t- a door to the " + door.to_room.name)

    def short_description(self):
        print("You are back in the lobby")
        print("You see...")
        for door in self.doors:
            print("\t- a door to the " + door.to_room.name)

    def enter_room(self):
        if self.entered:
            self.short_description()
        else:
            self.long_description()
            self.entered = True

class break_room(Room):
    def __init__(self, player):
        self.name = "break room"
        self.items = []
        self.load_items()
        self.npcs = []
        self.load_npcs()
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
        print("You are in the " + self.name)
        print("This is where all the people eat their lunch. You suspect there may be snacks in here... but you're a good dog.")
        print("You see...")
        for item in self.items:
            print("\t- " + item.name + ". " + str(item.description()))
            
        print("You also see...")
            
        for door in self.doors:
            print("\t- a door to the " + door.from_room.name)
    
    def short_description(self):
        print("You are back in the breakroom.")
        print("You see...")
        for door in self.doors:
            print("\t- a door to the " + door.from_room.name)
    
    def enter_room(self):
        if self.entered:
            self.short_description()
        else:
            self.long_description()
            self.entered = True

class supply_closet(Room):
    def __init__(self, player):
        self.name = "supply closet"
        self.items = []
        self.load_items()
        self.npcs = []
        self.load_npcs()
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
        print("You are in the " + self.name)
        print("There are lots of paper supplies and pens in here")
        print("You see...")
        for item in self.items:
            print("\t- " + item.name + ". " + str(item.description()))
            
        print("You also see...")
            
        for door in self.doors:
            print("\t- a door to the " + door.from_room.name)
    
    def short_description(self):
        print("You are back in the supply closet.")
        print("You see...")
        for door in self.doors:
            print("\t- a door to the " + door.from_room.name)
    
    def enter_room(self):
        if self.entered:
            self.short_description()
        else:
            self.long_description()
            self.entered = True

class common_area(Room):
    def __init__(self, player):
        self.name = "common area"
        self.items = []
        self.load_items()
        self.npcs = []
        self.load_npcs()
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
        print("You are in the " + self.name)
        print("This is where people hang out... no one seems to be paying attention")
        print("You see...")
        for item in self.items:
            print("\t- " + item.name + ". " + str(item.description()))
        
        for npc in self.npcs:
               print("\t- " + npc.name + ". " + str(npc.description()))
        
        print("You also see...")
            
        for door in self.doors:
            print("\t- a door to the " + door.from_room.name)
            
    def short_description(self):
        print("You are back in the break room")
        print("You see...")
        for door in self.doors:
            print("\t- a door to the " + door.from_room.name)
    
    def enter_room(self):
        if self.entered:
            self.short_description()
        else:
            self.long_description()
            self.entered = True

class cubicle(Room):
    def __init__(self, player):
        self.name = "cubicle"
        self.items = []
        self.load_items()
        self.npcs = []
        self.load_npcs()
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
        print("You are in the " + self.name)
        print("This is where one person works alone in their cube of shame... It's very grey in here")
        print("You see...")
        for item in self.items:
            print("\t- " + item.name + ". " + str(item.description()))
        
        for npc in self.npcs:
               print("\t- " + npc.name + ". " + str(npc.description()))
        
        print("You also see...")
            
        for door in self.doors:
            print("\t- a door to the " + door.from_room.name)
    
    def short_description(self):
        print("You are back in the cubicle")
        print("You see...")
        for door in self.doors:
            print("\t- a door to the " + door.from_room.name)
    
    def enter_room(self):
        if self.entered:
            self.short_description()
        else:
            self.long_description()
            self.entered = True
