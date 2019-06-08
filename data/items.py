#Item parent class
class Item:
    def __init__(self, name, touched, can_be_held):
        self.name = name
        self.touched = False
        self.can_be_held = can_be_held
        self.destroy = False
    
    def description(self):
        if self.touched is False:
            print("unaltered")
        elif self.touched is True:
            print("altered")
            
    def interact(self):
        if self.touched:
            print("altered")
        else:
            print("unaltered")
    
class phase_door(Item):
    def __init__(self, player, to_phase, message, name, description_string):
        self.name = name
        self.player = player
        self.to_phase = to_phase
        self.message = message
        self.actions = ["go", "go to" "enter", "open"]
        self.description_string = description_string
        self.locked = False
        
    def description(self):
        print(self.description_string)
        
    #this is a one off hack for the front door
    def interact(self):
        for item in self.player.inventory:
            if item.name == 'front door key':
                print("You unlocked the front door!")
                self.start_next_phase()
        
    def start_next_phase(self):
        #are you sure?
        while():
            print(self.message)
            choice = input()
            if choice == "y":
                return True
            elif choice == "n":
                return False
            else:
                print("Try again:")
                
        if self.to_phase is not None:
            self.to_phase.start_phase()
        elif self.to_phase is None:
            #show ending cutscene
            filepath = 'phase3_ending.txt' 
            with open(filepath) as fp: 
                for line in fp:
                    print(line)
                    input()
                    exit()
        
#phase 1 items
class bed (Item):
    def __init__(self):
        self.name = "bed"
        self.can_be_held = False
        self.actions = ["jump on"]
    
    def description(self):
        print("A big comfy bed!")
            
    def interact(self):
        print("You jump onto the bed and bounce around a little")
        
class blanket (Item):
    def __init__(self):
        self.name = "blanket"
        self.can_be_held = False
        self.actions = ["get cozy"]
        self.touched = False
    
    def description(self):
        if self.touched:
            return "A warm blanket, unfolded on the floor."
        else:
            return "A warm blanket, perfect on cold nights. Neatly folded."
            
    def interact(self):
        if self.touched is False:
            print("You get under the blanket and turn around a couple times")
            self.touched = True
        elif self.touched is True:
            print("You do your best to fold the blanket")
            self.touched = False
            
class book_shelf (Item):
    def __init__(self):
        self.name = "book shelf"
        self.can_be_held = False
        self.actions = ["read"]
    
    def description(self):
        return "A shelf filled with books. You can't read."
            
    def interact(self):
        print("...you can't read")
        
class couch (Item):
    def __init__(self):
        self.name = "couch"
        self.can_be_held = False
        self.actions = ["jump on", "sit on"]
        self.touched = False
    
    def description(self):
        if self.touched:
            return "It is comfy and familiar and has some of your fur on it"
        else:
            return "It is comfy and familiar."
            
    def interact(self):
        self.touched = True
        print("You jump up on the couch and lie down for a minute.")
        print("...that's enough of that, time for adventure!")
        
class door (Item):
    def __init__(self, player, needed_key, from_room, to_room):
        self.name = "door"
        self.unlocked = False
        self.can_be_held = False
        self.player = player
        self.needed_key = needed_key
        self.from_room = from_room
        self.to_room = to_room
        self.actions = ["unlock", "enter", "open"]
        
    def description(self):
        if self.unlocked:
            print("It's open! You can go from " + self.from_room.name + " to " + self.to_room.name)
        else:
            print("It's locked")
            
    def interact(self):
        if self.needed_key == "none":
            self.unlocked = True
        #if a key is needed
        if self.unlocked is False:
            #if self.needed_key in self.player.inventory:
            for item in self.player.inventory:
                if item.name == self.needed_key:
                    print("you opened the door!")
                    self.unlocked = True
                    self.change_room()
            else:
                print("you need a key to open this door")
                
        elif self.unlocked is True:
            self.unlocked = True
            self.change_room()
                
    def change_room(self):
        print(self.player.current_room)
        if self.player.current_room == self.from_room:
            self.player.change_room(self.to_room)
            print(self.player.current_room)
        elif self.player.current_room == self.to_room:
            self.player.change_room(self.from_room)
        
class herding_ball (Item):
    def __init__(self):
        self.name = "herding ball"
        self.can_be_held = False
        self.actions = ["play", "roll", "herd"]
    
    def description(self):
        print("A big round ball to push around with your nose.")
            
    def interact(self):
        print("You push the ball around. Just like herding a cow.")
        
class hose (Item):
    def __init__(self):
        self.name = "hose"
        self.can_be_held = False
        self.hose = ["play with", "play"]
    
    def description(self):
        if self.touched:
            print("The hose is uncoiled on the lawn.")
        else:
            print("The wet tube: the hose")
            
    def interact(self):
        if self.touched:
            print("You do your best to put the hose back.")
        else:
            print("You grab the hose and shake it around a little")
            
class key (Item):
    #Key takes room as a param to build its description string
    def __init__(self, name):
        self.name = name
        self.can_be_held = True
        self.can_be_dropped = False
        self.actions = ["use", "unlock"]
    
    def description(self):
        print("This is a key")

    def interact(self):
        print("This is a key, use it to unlock a door...")
            
            
    def update(self):
        #call when you know what room the key unlocks
        self.touched = True
        #self.name = self.unlocks + " key"

class kiddie_pool (Item):
    def __init__(self):
        self.name = "kiddie pool"
        self.can_be_held = False
        self.actions = ["splash", "swim", "jump"]
    
    def description(self):
        print("A shallow pool for you to cool your paws in")
            
    def interact(self):
        print("You leap into the pool and splash around. Feels good on a hot day.")
        
class kibble (Item):
    def __init__(self):
        self.name = "kibble bowl"
        self.can_be_held = False
        self.actions = ["eat", "nom"]
        self.touched = False
    
    def description(self):
        if self.touched:
            return "A bowl of kibble. It's got some crumbs around it."
        else:
            return "Just a bowl of kibble"
            
    def interact(self):
        print("You eat some kibble")
        print("omnonmononmnommm")
        
class saddlebags (Item):
    def __init__(self, Player):
        self.name = "saddlebags"
        self.can_be_held = True
    
    def description(self):
        print("A harness with pockets")
            
    def interact(self):
        #initialize the player's inventory with the front door key
        print("You put the saddlebags on. You have lots of room to carry stuff now!")
        
class tennis_ball (Item):
    def __init__(self):
        self.name = "tennis ball"
        self.can_be_held = True
        self.actions = ["chew", "play", "play with"]
        self.touched = False
    
    def description(self):
        #altered is when you know what door it unlockes
        if self.touched is False:
            return "Green and fuzzy. Full of hours of fun."
        elif self.touched is True:
            return "Still your favorite, but now a little slobbery"
            
    def interact(self):
        print("You grab the ball in your mouth and chew on it some")
        
class trash_can (Item):
    def __init__(self):
        self.name = "trash can"
        self.can_be_held = False
        self.actions = ["sniff"]
    
    def description(self):
        print("A container that you see your person throw things into...")
            
    def interact(self):
        print("Hmm... just paper. Yuck.")
        
class treat (Item):
    def __init__(self):
        self.name = "treat"
        self.can_be_held = True
        self.actions = ["eat", "sniff"]
    
    def description(self):
        print("A meaty snack for a good dog!")
            
    def interact(self):
        print("Tasty!")
        
class tug_rope (Item):
    def __init__(self):
        self.name = "tug rope"
        self.can_be_held = True
        self.actions = ["grab", "chew"]
    
    def description(self):
        print("A nice rope for playing tug of war with.")
            
    def interact(self):
        print("You grab the rope and shake it around a little")
        
class water (Item):
    def __init__(self):
        self.name = "bowl of water"
        self.can_be_held = False
        self.actions = ["drink"]
        self.touched = False
    
    def description(self):
        if self.touched is False:
            return "Just a bowl of water"
        elif self.touched is True:
            return "A bowl of water. It's got some splashes around it."
            
    def interact(self):
        print("You take a long drink")

#Phase 2 Items
class gate (Item):
    def __init__(self, player, from_room, to_room):
        self.name = "gate"
        self.can_be_held = False
        self.player = player
        self.from_room = from_room
        self.to_room = to_room
        self.actions = ["enter", "go through", "open"]
        
    def description(self):
        print("it's a gate between the " + self.from_room + " and " + self.to_room)
        print("enter this gate to go to " + self.to_room)
            
    def interact(self):
        self.change_room()
                
    def change_room(self):
        if self.player.current_room == self.from_room:
            self.player.change_room(self.to_room)
        elif self.player.current_room == self.to_room:
            self.player.change_room(self.from_room)
        
class shovel (Item):
    def __init__(self):
        self.name = "shovel"
        self.can_be_held = True
        self.actions = ["hold", "scoop"]
        self.touched = False
    
    def description(self):
        if self.touched is False:
            return "This shovel looks like it can scoop sand well."
        elif self.touched is True:
            return "Shovel was great at scooping sand, it's a little sandy now though."

    def interact(self):
        print("You test out the shovel's sand scooping abilities.")
        print("Yep, pretty good")

class bucket (Item):
    def __init__(self):
        self.name = "bucket"
        self.can_be_held = False
        self.actions = ["fill", "hold"]
        self.touched = False
    
    def description(self):
        if self.touched is False:
            return "A clean, empty bucket."
        elif self.touched is True:
            return "The bucket is useful for holding things! Maybe you can make a sandcastle with it."

    def interact(self):
        print("You play around with the bucket and get a little sand in it.")

class frisbee(Item):
    def __init__(self):
        self.name = "frisbee"
        self.can_be_held = True
        self.actions = ["chew", "play", "hold"]
        self.touched = False
    
    def description(self):
        if self.touched is False:
            return "Oh look a Frisbee! Maybe you can have someone play fetch with you."
        elif self.touched is True:
            return "This Frisbee has great aerodynamics."

    def interact(self):
        print("You throw the frisbee and it goes far! It would be a lot of fun if someone threw it for you to catch")

class soccer_ball (Item):
    def __init__(self):
        self.name = "soccer ball"
        self.can_be_held = False
        self.actions = ["chew", "play", "push"]
        self.touched = False
    
    def description(self):
        if self.touched is False:
            return "This ball rolls around really well! Seems great to play with."
        elif self.touched is True:
            return "This ball rolls very fast around the grass. Provides great exercise."

    def interact(self):
        print("You push the ball around with your nose.")

class floaty (Item):
    def __init__(self):
        self.name = "floaty"
        self.can_be_held = False
        self.actions = ["float"]
        self.touched = False
    
    def description(self):
        if self.touched is False:
            return "A donut shaped floaty floating in the water."
        elif self.touched is True:
            return "This floaty is the best thing for lazing around in the water!"

    def interact(self):
        print("You slowly put your paw on the floaty to test its firmness.")

class swim_goggles (Item):
    def __init__(self):
        self.name = "swim goggles"
        self.can_be_held = True
        self.actions = ["wear", "hold"]
        self.touched = False
    
    def description(self):
        if self.touched is False:
            return "Oh look a pair of goggles!"
        elif self.touched is True:
            return "These goggles are fitted perfectly for your head, perfect for seeing underwater."

    def interact(self):
        print("You try on the goggles, they fit you well!")

class snorkle (Item):
    def __init__(self):
        self.name = "snorkel"
        self.can_be_held = False
        self.actions = ["wear"]
        self.touched = False
    
    def description(self):
        if self.touched is False:
            return "A snorkle with a long tube at the end."
        elif self.touched is True:
            return "This snorkle is great at helping breathe underwater."

    def interact(self):
        print("You lick the snorkle... you put your mouth in the snorkle.")

class beach_ball (Item):
    def __init__(self):
        self.name = "beach ball"
        self.can_be_held = False
        self.actions = ["play", "push"]
        self.touched = False
    
    def description(self):
        if self.touched is False:
            return "A large, colorful beachball floats on the water."
        elif self.touched is True:
            return "The ball is fun to play with while in a pool! Bounces around well, a little wet though."

    def interact(self):
        print("You push the beach ball a little.")
        
class stick (Item):
    def __init__(self):
        self.name = "stick"
        self.can_be_held = True
        self.actions = ["play", "bite"]
        self.touched = False
    
    def description(self):
        print("The perfect stick for playing with!")

    def interact(self):
        print("You carry the stick around proudly")
        
class squeaky_toy (Item):
    def __init__(self):
        self.name = "squeaky toy"
        self.can_be_held = True
        self.actions = ["play", "bite"]
        self.touched = False
    
    def description(self):
        print("The squeakiest squeaky toy")

    def interact(self):
        print("*SQUEAK*")
        
class map (Item):
    def __init__(self):
        self.name = "map"
        self.can_be_held = True
        self.actions = ["use","read", "open"]
        self.touched = False
        self.phase_door = None #this gets populated
    
    def description(self):
        print("A map to the office your human works at")

    def interact(self):
        print("You read the map. You find a route to your human's office.")
        print("Do you want to go there now?")
        self.phase_door.start_next_phase()
        
class pad_lock (Item):
    def __init__(self):
        self.name = "pad lock"
        self.can_be_held = False
        self.actions = ["touch", "sniff", "yank"]
        self.touched = False

    def description(self):
        if self.touched is False:
            return "A locked pad lock"
        elif self.touched is True:
            return "This pad lock is very difficult to open"

    def interact(self):
        print("You push the pad lock with your nose... you chew around on it, nothing happens.")

class door_mat (Item):
    def __init__(self):
        self.name = "door mat"
        self.can_be_held = False
        self.actions = ["move", "jump", "sniff"]
        self.touched = False

    def description(self):
        if self.touched is False:
            return "This doormat is laying right outside the doors to the office."
        elif self.touched is True:
            return "This doormat is covered in your dog hair, but you realized that it is movable."

    def interact(self):
        print("You walk on top of the door mat in circles to inspect it.")

#Office key is contained under the door mat to unlock the padlock to the office door.
class office_key (Item):
    def __init__(self):
        self.name = "office key"
        self.can_be_held = True
        self.actions = ["hold", "use"]
        self.touched = False

    def description(self):
        if self.touched is False:
            return "This shiny key has tape on it that says OFFICE on it"
        elif self.touched is True:
            return "This key says OFFICE on it, it might be helpful"

    def interact(self):
        print("")

class plant (Item):
    def __init__(self):
        self.name = "plant"
        self.can_be_held = False
        self.actions = ["sniff", "lick"]
        self.touched = False
    
    def description(self):
        if self.touched is False:
            return "A bright, color plant in a nicely painted vase."
        elif self.touched is True:
            return "Looks nice, smells good... tastes horrible."

    def interact(self):
        print("You give the plant a nice whiff.")

class chair (Item):
    def __init__(self):
        self.name = "chair"
        self.can_be_held = False
        self.actions = ["jump on"]
        self.touched = False
    
    def description(self):
        if self.touched is False:
            return "A human chair to wait in."
        elif self.touched is True:
            return "This chair was very comfortable."

    def interact(self):
        print("You step on certain parts of the chair.")

class magazine (Item):
    def __init__(self):
        self.name = "magazine"
        self.can_be_held = True
        self.actions = ["hold", "lick"]
        self.touched = False
    
    def description(self):
        if self.touched is False:
            return "A colorful magazine with a human on the cover."
        elif self.touched is True:
            return "The magazine is a little wet now, the images are becoming distorted."

    def interact(self):
        print("This magazine interests you, you try to find your human in the magazine by flipping through the pages with your nose.")

class snacks (Item):
    def __init__(self):
        self.name = "snacks"
        self.can_be_held = True
        self.actions = ["hold", "eat", "sniff"]
        self.touched = False
    
    def description(self):
        if self.touched is False:
            return "Various snacks are laying around the room."
        elif self.touched is True:
            return "All these snacks are the ones you love to steal back at home! Chips! Fruits! Candy!"

    def interact(self):
        print("You look around at the snacks and see an open bag of chips! You eat a chip - delicious.")

class table (Item):
    def __init__(self):
        self.name = "table"
        self.can_be_held = False
        self.actions = ["jump on"]
        self.touched = False
    
    def description(self):
        if self.touched is False:
            return "A breakroom table with several random things on it."
        elif self.touched is True:
            return ""

    def interact(self):
        print("You circle around the table and look at the several things on top.")

class water_cooler(Item):
    def __init__(self):
        self.name = "water cooler"
        self.can_be_held = False
        self.actions = []
        self.touched = False
    
    def description(self):
        if self.touched is False:
            return ""
        elif self.touched is True:
            return ""

    def interact(self):
                print("")

class vacuum (Item):
    def __init__(self):
        self.name = "vacuum"
        self.can_be_held = False
        self.actions = ["bark", "sniff", "push"]
        self.touched = False
    
    def description(self):
        if self.touched is False:
            return "An evil thing with bright lights and loud noises."
        elif self.touched is True:
            return "This is your worst enemy, you are avoiding this monster at all cost."

    def interact(self):
        print("You try to assert your dominance by standing your ground and barking at the vacuum.")

class spray_bottle (Item):
    def __init__(self):
        self.name = "spray bottle"
        self.can_be_held = True
        self.actions = ["hold", "lick"]
        self.touched = False
    
    def description(self):
        if self.touched is False:
            return "A spray bottle, half-filled with water"
        elif self.touched is True:
            return "This spray bottle sprays well. Provides a huge mist."

    def interact(self):
        print("You place your paw on the handle and a huge mist sprays out. You lick the water dripping out of the nozzle.")

class office_supplies (Item):
    def __init__(self):
        self.name = "office supplies"
        self.can_be_held = True
        self.actions = ["hold", "inspect"]
        self.touched = False
    
    def description(self):
        if self.touched is False:
            return "A pouch filled with several office supplies."
        elif self.touched is True:
            return "This pouch contains pencils, pens, scissors, some paperclips, and a highlighter."

    def interact(self):
        print("You paw through the pouch and look through all the office supplies in the pouch.")

class computer (Item):
    def __init__(self):
        self.name = "computer"
        self.can_be_held = False
        self.actions = []
        self.touched = False
    
    def description(self):
        if self.touched is False:
            return ""
        elif self.touched is True:
            return ""

    def interact(self):
        print("")

class office_chair (Item):
    def __init__(self):
        self.name = "office chair"
        self.can_be_held = False
        self.actions = []
        self.touched = False
    
    def description(self):
        if self.touched is False:
            return ""
        elif self.touched is True:
            return ""

    def interact(self):
        print("")

class notebook (Item):
    def __init__(self):
        self.name = "notebook"
        self.can_be_held = True
        self.actions = ["read", "hold"]
        self.touched = False
    
    def description(self):
        if self.touched is False:
            return ""
        
        elif self.touched is True:
            return ""

#player reads notebook here and it gives a clue
    def interact(self):
        print("")
