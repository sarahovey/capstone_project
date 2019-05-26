#Item parent class
class Item:
    def __init__(self, name, touched, can_be_held):
        self.name = name
        self.touched = False
        self.can_be_held = can_be_held
    
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
        self.actions = ["unlock", "enter"]
        
    def description(self):
        if self.unlocked:
            print("It's open! You can go from " + self.from_room + " to " + self.to_room)
        else:
            print("It's locked")
            
    def interact(self):
        if self.needed_key == "none":
            self.unlocked = True
        if self.unlocked is False:
            if self.needed_key in self.player.inventory:
                print("you opened the door!")
                self.unlocked = True
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
        self.actions = ["use", "unlock"]
    
    def description(self):
        print("This is a key")
        #True is when you know what door it unlocks
        # if self.touched:
        #     print("This key unlocks the " + self.unlocks)
        # else:
        #     print("This is a key")
            
    def interact(self):
        print("This is a key, use it to unlock a door...")
        # if self.touched:
        #     print("This is a key")
        # else:
        #     print("This key unlocks the " + self.unlocks)
            
            
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
        self.name = "bowl of kibble"
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

class buried_treasure(Item):
    def __init_(self):
        self.name = "buried treasure"
        self.can_be_held = True
        #this action to give to a hunan
        self.actions = ["give"]
        self.touched = True
    def description(self):
        if self.touched is False:
            return "Its buried treasure!!! Maybe a humane would like it?"
        else self.touched is True:
            return "A humane wants this, its shiny!"

class stick(Item):
        def __init_(self):
        self.name = "a stick"
        self.can_be_held = False
        #this action to give to a hunan
        self.actions = ["carry"]
        self.touched = False
    def description(self):
        if self.touched is False:
            return "its a stick! yayy!!!"
        else self.touched is True:
            return "this is your favorite stick now."