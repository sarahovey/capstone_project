import items

class NPC:
    def __init__(self, player):
        self.name = ""
        self.player = player
        self.met = False
        
#Ideally we'd have these completely abstracted out,
#but we have so few npcs that it doesn't matter too much
class cat(NPC):
    def __init__(self):
        self.name = "cat"
        self.description = self.description()
        self.dialogue = self.show_dialogue()
        
    def meet(self):
        #call this when the player meets the npc
        #this way dialogue and description can
        #update accordingly
        self.met = True
        
    def description(self):
        #description can depend on whether or not you've already met the npc
        if self.met:
            print("its your old friend")
        else:
            print("You see your old friend, a big gray cat.")
        
    def show_dialogue(self):
        #check whether or not a player has a certain item
        #or has done something for the npc
        #or something else
        #that can change dialogue
        print ("mrowww")
        
class rusty(NPC):
    def __init__(self):
        self.name = "Rusty"
        self.description = self.description()
        self.dialogue = self.show_dialogue()
        self.met = False
        self.quest_finished = False
        self.concluded_quest = False #this means the npc has acknowledged the quest ended
        self.inventory = []
        
    def interact(self):
        #call this when the player meets the npc
        #this way dialogue and description can
        #update accordingly
        self.show_dialogue()
        self.met = True
        
    def description(self):
        #description can depend on whether or not you've already met the npc
        if self.met:
            print("It's Rusty, your new friend")
        else:
            print("Another Cattle Dog, big and red. Maybe a new friend?")
        
    def is_quest_finished(self):
        #Check if the player has the npc's requested item in their inventoru
        self.quest_finished = self.player.find_item(["tennis ball", "stick", "squeaky toy"])
        
    def show_dialogue(self):
        #check whether or not a player has a certain item
        #or has done something for the npc
        #or something else
        #that can change dialogue
        if self.met:
            if self.is_quest_finished():
                if self.concluded_quest:
                    print("Thanks for bringing me that great toy!")
                    print("Try reading that map to find your human")
                else:
                    print("Wow you brought me something really special!")
                    print("Can we trade for this map I have? I think it would help you find your hooman's work")
                    input()
                    print("[The map has been added to your inventory!]")
                    self.player.inventory.append(self.inventory[0])
                    self.concluded_quest = True
            else:
                print("If you manage to find a fun toy I could play with, could you bring it to me please?")
        else:
            print("Hi new friend! I'm Rusty. I like hanging out in this park and chewing on sticks")
            print("You don't know where I could get a good toy do you?")
            self.met = True
            
class coworker(NPC):
    def __init__(self):
        self.name = "Human's Coworker"
        self.description = self.description()
        self.dialogue = self.show_dialogue()
        self.met = False
        self.quest_finished = False
        self.concluded_quest = False #this means the npc has acknowledged the quest ended
        self.inventory = []
        
    def interact(self):
        #call this when the player meets the npc
        #this way dialogue and description can
        #update accordingly
        self.show_dialogue()
        self.met = True
        
    def description(self):
        #description can depend on whether or not you've already met the npc
        if self.met:
            print("It's another person, your human's coworker")
        else:
            print("A human in the office. Must be your human's coworker.")
        
    def show_dialogue(self):
        print("Hey buddy, are you lost? I'll look at your tags")
        print(".....")
        print("I know your person! I'll take you to them, let's go!")
        self.inventory[0].start_next_phase()
        input()
        