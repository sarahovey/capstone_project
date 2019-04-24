#Item parent class
class Item:
    def __init__(self, name, state, can_be_held):
        self.name = name
        self.state = False
        self.can_be_held = can_be_held
    
    def description(self):
        if self.state is False:
            print("unaltered")
        elif self.state is True:
            print("altered")
            
    def interact(self):
        if self.state is False:
            print("unaltered")
        elif self.state is True:
            print("altered")
       
#Item child classes
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
    
    def description(self):
        if self.state is False:
            print("A warm blanket, perfect on cold nights. Neatly folded.")
        elif self.state is True:
            print("A warm blanket, unfolded on the floor.")
            
    def interact(self):
        if self.state is False:
            print("You get under the blanket and turn around a couple times")
            self.state = True
        elif self.state is True:
            print("You do your best to fold the blanket")
            self.state = False
            
class book_shelf (Item):
    def __init__(self):
        self.name = "book shelf"
        self.can_be_held = False
        self.actions = ["read"]
    
    def description(self):
        print("A shelf filled with books. You can't read.")
            
    def interact(self):
        print("...you can't read")
        
class couch (Item):
    def __init__(self):
        self.name = "couch"
        self.can_be_held = False
        self.actions = ["jump on", "sit on"]
    
    def description(self):
        if self.state is False:
            print("It is comfy and familiar.")
        elif self.state is True:
            print("It is comfy and familiar and has some of your fur on it")
            
    def interact(self):
        print("You jump up on the couch and lie down for a minute.")
        print("...that's enough of that, time for adventure!")
        
class door (Item):
    def __init__(self, player, needed_key, from_room, to_room):
        self.name = "door"
        self.state = False
        self.can_be_held = False
        self.player = player
        self.needed_key = needed_key
        self.from_room = from_room
        self.to_room = to_room
        self.actions = ["unlock", "enter"]
        
    def description(self):
        if self.state is False:
            print("It's locked")
        elif self.state is True:
            print("It's open! You can go from " + self.from_room + " to " + self.to_room)
            
    def interact(self):
        if self.state is False:
            if self.needed_key in self.player.inventory:
                print("you opened the door!")
            else:
                print("you need a key to open this door")
        
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
        if self.state is False:
            print("The wet tube: the hose")
        elif self.state is True:
            print("The hose is uncoiled on the lawn.")
            
    def interact(self):
        if self.state is False:
            print("You grab the hose and shake it around a little")
        elif self.state is True:
            print("You do your best to put the hose back.")
            
class key (Item):
    #Key takes room as a param to build its description string
    def __init__(self, Room):
        self.name = "key"
        self.unlocks = Room.name
        self.can_be_held = True
        self.actions = ["use", "unlock"]
    
    def description(self):
        #True is when you know what door it unlocks
        if self.state is False:
            print("This is a key")
        elif self.state is True:
            print("This key unlocks the " + self.unlocks)
            
    def interact(self):
        if self.state is False:
            print("This is a key")
        elif self.state is True:
            print("This key unlocks the " + self.unlocks)
            
    def update(self):
        #call when you know what room the key unlocks
        self.state = True
        self.name = self.unlocks + " key"

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
        self.name = "kibble"
        self.can_be_held = False
        self.actions = ["eat", "nom"]
    
    def description(self):
        if self.state is False:
            print("A bowl of kibble")
        elif self.state is True:
            print("A bowl of kibble. It's got some crumbs around it.")
            
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
    
    def description(self):
        #altered is when you know what door it unlockes
        if self.state is False:
            print("Green and fuzzy. Full of hours of fun.")
        elif self.state is True:
            print("Still your favorite, but now a little slobbery")
            
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
        self.name = "water"
        self.can_be_held = False
        self.actions = ["drink"]
    
    def description(self):
        if self.state is False:
            print("A bowl of water")
        elif self.state is True:
            print("A bowl of water. It's got some splashes around it.")
            
    def interact(self):
        print("You take a long drink")